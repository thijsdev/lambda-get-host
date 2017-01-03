from __future__ import print_function

import json
import socket

print('Loading function')


def lambda_handler(event, context):
    return { 'statusCode': '200',
        'body': socket.gethostname(),
        'headers': { 'Content-Type': 'application/json' },
    }  # Echo back the first key value
    #raise Exception('Something went wrong')
