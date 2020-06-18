from threading import Thread
from queue import Queue, Empty
import speech_recognition as sr
import os
import time
import random
import wit_response_engine
import gvoice_response_engine
import error_reporter
import logger

def setMicrophone(indexnumber):
    audio_input_device = indexnumber
    return audio_input_device

def setRecognitionSettings():
    recognition = sr.Recognizer()
    recognition.pause_threshold = 1 # seconds of silence considers phrase done
    recognition.non_speaking_duration = 0.2 # seconds on each side of recording
    return recognition

def listen_loop(queue, microphone, recognition):
    with sr.Microphone(device_index=microphone) as source:
        print("[   ] Starting listening thread")
        logger.log("Starting listening thread.")
        logger.log("Boot completed.")
        while True:
            print("[   ] Listening for new sentence")
            audio = recognition.listen(source)
            queue.put(audio) #add captured data to the queue

def listen(microphone, witapikey, recognition, random_filler):
    audio_queue = Queue() #initialize queue for audio data
    print("[   ] Starting voice engine")
    logger.log("Starting voice engine.")
    listen_thread = Thread(target=listen_loop, args=[audio_queue, microphone, recognition], daemon=True)
    listen_thread.start()

    while True:
        try:
            audio = audio_queue.get(block=True,timeout=random.randrange(3,8))
        except Empty:
                #send filler content if no speaking is occuring
                try:
                    print("[   ] Speaking filler")
                    gvoice_response_engine.synthesize_text(random.choice(random_filler))
                except:
                    print("[!!!] SPEAKING FILLER FAILED - IS random_filler NOT LOADED?")
                    error_reporter.reportError("App could not speak filler")
                    logger.log("App could not speak filler.")
                    
        else:
            try:
                #recognise mic audio using wit.ai
                start = time.time()
                wit_response = recognition.recognize_wit(audio, key=witapikey, show_all=True)
                end = time.time() - start

                wit_response_engine.respond(wit_response, end)
                
            #errors
            except sr.UnknownValueError:
                print("[!!!] WIT.AI COULD NOT UNDERSTAND THE AUDIO")
                error_reporter.reportError("Wit.ai could not understand the provided audio")
                logger.log("Wit.ai could not understand the provided audio.")
            except sr.RequestError as e:
                print("[!!!] COULD NOT REQUEST RESULTS FROM WIT.AI; {0}".format(e))
                error_reporter.reportError("App was unable to connect to Wit.ai: {0}".format(e))
                logger.log("App was unable to connect to Wit.ai: {0}".format(e))