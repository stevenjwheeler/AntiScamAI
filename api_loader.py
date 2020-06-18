import error_reporter
import logger

def loadKey():
    #load wit.ai API key
    try:
        keyfile = open("key.txt", "r")
    except:
        print("[!!!] NO API KEY TO LOAD - PLACE WIT.AI KEY IN KEY.TXT")
        error_reporter.reportError("App could not find an WIT.AI API key to load")
        logger.log("App could not find an Wit.ai API key to load.")
        exit()

    key = keyfile.read()
    keyfile.close()
    if len(key) == 32:
        print("[   ] Wit.ai api key loaded")
        logger.log("Wit.ai API key loaded.")
        return key
    else:
        print("[!!!] API KEY IS MALFORMED")
        error_reporter.reportError("Wit.ai API key is malformed")
        logger.log("Wit.ai API key is malformed.")
        exit()
    