import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db = boto3.resource('dynamodb')


def lambda_handler(event, context):
    logger.info('Got message from queue ...')
    msg = json.loads(event['Records'][0]['body'])
    logger.info(msg)

    table_name = os.environ['DYNAMODB_NAME']
    table = db.Table(table_name)

    table.put_item(
        Item={
            'fileKey': msg['bucket'] + '/' + msg['key'],
            'bucket': msg['bucket'],
            'key': msg['key']
        }
    )