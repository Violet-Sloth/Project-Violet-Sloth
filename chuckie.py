import random
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('wotd')

def lambda_handler(event, context):
    word = table.get_item(
        Key={
            'language': 'spanish',
            'id': random.randrange(1, 697)
        }
    )
    wotd = '<speak>' + word["Item"]["word"] + ' which means ' + word["Item"]["word_translation"] + ' and sounds like <audio src="' + word["Item"]["word_sound"] + '"/></speak>'
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml' : wotd
            }
        }
    }
    return response