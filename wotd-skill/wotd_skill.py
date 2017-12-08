import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('wotd')


def lambda_handler(event, context):
    wotd = table.query(
        KeyConditionExpression=Key('language').eq(event['request']['intent']['slots']["Language"]["value"].lower()) & Key('id').gt(0),
        FilterExpression=Attr('isActive').eq(True)
    )
    print(wotd['Items'])
    item = wotd["Items"]
    print(item)
    parsed = '<speak>The ' + event["request"]["intent"]["slots"]["Language"]["value"] + ' word of the day is <audio src="' + item[0]["word_sound"] + \
    '"/> which means ' + item[0]["word_translation"] + \
    '. Here is the word used in a sentence. <audio src="' + item[0]["sentence_sound"] + \
    '"/> which means ' + item[0]["sentence_translation"] + '</speak>'
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
