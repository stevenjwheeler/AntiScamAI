import json
import error_reporter
import logger

def loadPhrases(phrase):
    try:
        with open("phrases.json") as phrasesfile:
            data = json.load(phrasesfile)
            print ("[   ] Loading phrases:", phrase)
            logger.log("Loading phrases: {0}".format(phrase))
            contents = data[phrase]
            phrasesfile.close()
            return contents
    except:
        print("[!!!] COULD NOT LOAD PHRASES:", phrase)
        error_reporter.reportError("App could not load phrases: {0}".format(phrase))
        logger.log("App could not load phrases: {0}".format(phrase))