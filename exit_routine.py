from signal import signal, SIGINT
import logger

def exitroutine(signal_received, frame):
    print("[!!!] CTRL-C DETECTED - ENDING PROCESS")
    logger.log("Ctrl-C was detected, ending process.")
    exit()

def listenForExit():
    signal(SIGINT, exitroutine)