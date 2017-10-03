import boto3
from boto3.dynamodb.conditions import Key
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('wotd')

def lambda_handler(event, context):
    wotd = table.query(
        IndexName='language-word-index',
        KeyConditionExpression=Key('language').eq('spanish') & Key('word').eq(os.environ['word'])
    )
    item = wotd["Items"]
    parsed = '<speak>The word of the day is <audio src="' + item[0]["word_sound"] + '"/> which means ' + item[0]["word_translation"] + '</speak>'
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml' : parsed
            }
        }
    }
    return response