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
    wotd = random.choice(list(wotdOptions.values()))
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': wotd
            }
        }
    }
    return response
