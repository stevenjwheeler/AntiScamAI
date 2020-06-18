#TODO:
# POTENTIALLY REPLACE THE GOOGLE TTS WITH IBM WATSON TTS

#print information
print("AntiScamAI - V1.0.0 (Dark Void)\nby Steven Wheeler\n")

#import additional files
import api_loader
import gcred_loader
import error_reporter
import logger
import exit_routine
import phrase_loader
import record_engine

#start boot
logger.log("Started booting.")

#prepare exit routine
exit_routine.listenForExit()

#enable google services
gcred_loader.appCredentials()

#load wit.api key
witapikey = api_loader.loadKey()

#declare microphone
microphone = record_engine.setMicrophone(3) # Mic index number

#initialize recognition engine
recognition = record_engine.setRecognitionSettings()

#load phrases
random_filler = phrase_loader.loadPhrases("random_filler")

#start listen and response engine
record_engine.listen(microphone, witapikey, recognition, random_filler)