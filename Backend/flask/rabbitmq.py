import pika
import requests
import json
import sys

# import func_api.py
# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# sys args
asin = sys.argv[1]



# Declare a queue

message1=""
channel.queue_declare(queue='my_queue')
def api_call():

    url = 'https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-lookup-reviews'
    params = {
      'page': '1',
      'domainCode': 'com',
      'asin': asin,
      'sortBy': 'recent',    
      'filters': 'reviewerType=avp_only_reviews;filterByStar=five_star'
    }

    headers= {
    'X-RapidAPI-Key': '9ed674538amshdcb9838f5a86f98p11ff43jsnbbfd1b11af6d',
    'X-RapidAPI-Host': 'axesso-axesso-amazon-data-service-v1.p.rapidapi.com'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
#         print(response.json()['reviews'][0]['text'])
        reviews = response.json().get('reviews', [])
        if reviews:
            temp=[]
            message=[]
            for review in reviews:
                message1 = review.get('text')
                temp.append(message1)
            print(f"Testing: {temp}")
            message = json.dumps(temp)
            channel.basic_publish(exchange='',
            routing_key='my_queue',
                                   body=message)
            print(f"Published message to RabbitMQ: {message}")

    else:
        print('Error:', response.status_code)
        print(response.json())


api_call()

print("Message sent to RabbitMQ")
connection.close()