import json
#event stores the event
#eventcomes as dictionary
def lambda_handler(event, context):
    # TODO implement
    responseVar = 'Hi {},Welcome to lamda'.format(event['name'])
    return {
        "statusCode": 200,
        "body": json.dumps(responseVar)
    }