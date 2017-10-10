from bs4 import BeautifulSoup
import requests
import boto3

#Establish connection to Database
wotdDB = boto3.client('dynamodb')

#Lambda Handler function
def lambda_handler(event, context):
	#Scrap WOTD XML Feed for Today's word
	response  = requests.get("https://wotd.transparent.com/rss/es-widget.xml")
	data = response.text
	soup = BeautifulSoup(data, "xml")

	#Locate today's WOTD in database- must run query to find ID. Set result to wordID
	dbQuery =  wotdDB.query(
		TableName='wotd',
        IndexName='language-word-index',
		ExpressionAttributeNames={"#L":"language"},
		ExpressionAttributeValues={":lang":{"S":"spanish"},":word":{"S":soup.word.get_text()}},
        KeyConditionExpression="#L = :lang AND word = :word"
    )
	wordID = dbQuery['Items'][0]['id']['N']

	#Set today's Word of the Day to active
	dbUpdater = wotdDB.update_item(
		ExpressionAttributeNames={
			'#IA': 'isActive',
		},
		ExpressionAttributeValues={
			':ia':{
			'BOOL': True,
			},
		},
		TableName='wotd',
		Key={
			"language": {
				"S": 'spanish'
			},
			"id":{
				"N": wordID
			},
		},
		UpdateExpression='SET #IA=:ia'
	)

	#Find any other active WOTD items that are not today's word
	dbFindActive =  wotdDB.query(
		TableName='wotd',
		ExpressionAttributeNames={"#L":"language"},
		ExpressionAttributeValues={":lang":{"S":"spanish"},":idVal":{"N":"0"},":isActiveVal":{"BOOL":True},":word":{"S":soup.word.get_text()}},
        KeyConditionExpression="#L = :lang AND id > :idVal",
		FilterExpression="isActive = :isActiveVal AND word <> :word"
    )

	#Loop through items that are not supposed to be active and set to inactive
	for item in dbFindActive['Items']:
		dbUpdater = wotdDB.update_item(
			ExpressionAttributeNames={
				'#IA': 'isActive',
			},
			ExpressionAttributeValues={
				':ia':{
				'BOOL': False,
				},
			},
			TableName='wotd',
			Key={
				"language": {
					"S": item['language']["S"]
				},
				"id":{
					"N": item['id']["N"]
				},
			},
			UpdateExpression='SET #IA=:ia'
		)
	
	return dbUpdater
