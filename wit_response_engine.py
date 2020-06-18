import gvoice_response_engine
import error_reporter
import logger

def respond(wit_response, time):
    if wit_response['_text']:
        try:
            text = wit_response['_text']
            intent = wit_response['entities']['intent'][0]['value']
            intentconfidence = "{0:.0f}%".format(wit_response['entities']['intent'][0]['confidence'] * 100)
            sentiment = wit_response['entities']['sentiment'][0]['value']
            sentimentconfidence = "{0:.0f}%".format(wit_response['entities']['sentiment'][0]['confidence'] * 100)
            processingtime = "{0:.2f}".format(time)

            print("[   ] Wit.ai response: ")
            print("            TEXT:", text)
            print("            PERCEIVED INTENT:", intent)
            print("            INTENT CONFIDENCE:", intentconfidence)
            print("            PERCEIVED SENTIMENT:", sentiment)
            print("            SENTIMENT CONFIDENCE:", sentimentconfidence)
            print("            PROCESSING TIME:", processingtime, "seconds")

            #AUDIO PROCESSING HERE

            print("[   ] Speaking response")
        except:
            print("[!!!] Could not parse the wit response")
            error_reporter.reportError("App could not parse the wit response")
            logger.log("App could not parse the wit response.")
        try:
            gvoice_response_engine.synthesize_text(wit_response['_text'])
        except:
            print("[!!!] Could not produce or play sound")
            error_reporter.reportError("App could not produce or play sound")
            logger.log("App could not produce or play sound.")