import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs = boto3.client('sqs')


def lambda_handler(event, context):
    logger.info('New file appeared on S3 Bucket ...')
    logger.info('Input event{}'.format(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    sqs_url = os.environ['SQS_URL']
    msg = {'bucket': bucket, 'key': key}

    sqs.send_message(
        QueueUrl=sqs_url,
        MessageBody=json.dumps(msg)
    )
