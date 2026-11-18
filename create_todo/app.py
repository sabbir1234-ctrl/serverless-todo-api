import json
import uuid
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        item = {
            'id': str(uuid.uuid4()),
            'title': body['title'],
            'completed': False
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps(item)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
