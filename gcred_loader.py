import os
import logger

def appCredentials():
    try:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcreds.json"
        print("[   ] Google application credentials loaded")
        logger.log("Google application credentials loaded.")
    except:
        print("[!!!] COULD NOT READ GCREDS.JSON")
        logger.log("Could not read gcreds.json.")