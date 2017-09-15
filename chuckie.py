import random

wotdOptions = {
    "Spanish": "Hola",
    "French": "Bonjour",
    "English": "Hello",
    "Texan": "Howdy",
    "Chinese": "Ni Hao",
    "Japanese": "Konichiwa"
}

def lambda_handler(event, context):
    wotd = '<speak>' + random.choice(list(wotdOptions.values())) + '<audio src="https://www.jovo.tech/audio/oCPbFrRY-00122-arabic-wotd-words.mp3"/></speak>'
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
