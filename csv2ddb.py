import boto3
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('wotd')

filename = 'words_Chinese-Mandarin.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        print(line[1])
        table.put_item(Item=dict(language=line[0], id=int(line[1]), sentence_sound=line[2], sentence_text=line[3],
                                 sentence_translation=line[4], sentence_transliteration=line[5], word=line[6],
                                 word_sound=line[7], word_translation=line[8], word_transliteration=line[9]))

