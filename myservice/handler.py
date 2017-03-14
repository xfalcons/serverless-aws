import os
import json

def hello(event, context):
    # get channel_secret and channel_access_token from your environment variable
    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "channel_secret": channel_secret,
        "channel_access_token": channel_access_token,
        "x-line-signature": event['headers']['x-line-signature'],
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
