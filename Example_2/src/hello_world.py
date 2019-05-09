import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Saying hello from AWS lambda ... ")
    if event['queryStringParameters'] is None or not ('name' in event['queryStringParameters']):
        name = 'nameless one'
    else:
        name = event['queryStringParameters']['name']

    return ok_response(name)


def ok_response(name):
    return {
        'statusCode': "200",
        'body': 'Hello there ' + name + ' from serverless world',
    }