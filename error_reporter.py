from google.cloud import error_reporting

def reportError(message):
    error=error_reporting.Client()
    error.report(message)