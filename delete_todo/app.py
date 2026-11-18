import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        todo_id = event['pathParameters']['id']

        table.delete_item(Key={'id': todo_id})

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Todo deleted successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
