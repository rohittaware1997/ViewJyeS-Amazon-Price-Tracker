 #!/usr/bin/env python3

from urllib.parse import urlparse
import smtplib
from email. message import EmailMessage
import ssl
import requests
import json
import mysql.connector
import sys

asin = sys.argv[1]
email = sys.argv[2]
notification_type = int(sys.argv[3])

#email configuration
email_sender = 'sharedflix6@gmail.com'
email_password = 'elrssdzbodiqfimv'
email_receiver = email


# Establish a connection to the database
mydb = mysql.connector.connect(
  host="54.219.208.81",
  user="akhil",
  password="akhil@05",
  database="amazon_tracker"
)

# Create a cursor object to execute the query
cursor = mydb.cursor()


def api_call():
    # Get the price for the product 

    url_api = "https://amazon-product-price-data.p.rapidapi.com/product"

    querystring = {"asins":asin,"locale":"US"}

    headers = {
      "X-RapidAPI-Key": "9ed674538amshdcb9838f5a86f98p11ff43jsnbbfd1b11af6d",
      "X-RapidAPI-Host": "amazon-product-price-data.p.rapidapi.com"
    }

    response = requests.request("GET", url_api, headers=headers, params=querystring)

    print(response.content)

    decoded_response = response.content.decode('utf-8')

    # Parse the JSON string into a Python object (in this case, a list)
    response_list = json.loads(decoded_response)

    # Access the asin value of the first item in the list
    current_price = response_list[0]['current_price']

    # Print the asin value
    current_price = float(current_price)

    return current_price

def update_db(new_price):
    query = "UPDATE email_tracker SET curr_price = %s WHERE ASIN = %s"
    # Execute the UPDATE query with the new price and email parameters
    cursor.execute(query, (new_price, asin))
    mydb.commit()


def get_from_db():
    query = "SELECT curr_price, product_name FROM email_tracker WHERE ASIN = %s"
    cursor.execute(query, (asin,))

    # Fetch the results
    result = cursor.fetchone()
    return float(result[0]), str(result[1])
    # final_data = json.loads(result)
    # print(final_data)
    # return final_data[0]['curr_price'], final_data[0]['product_name']

def send_email(body):
    subject = 'Price change Alert!!!'
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To']= email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if notification_type == 0:
    new_price = api_call()
    curr_price, product_name = get_from_db()
    print(curr_price)
    print(product_name)
    body = '''
    Hello user there is a price decrease for 
    ''' + product_name + " its current price is: " + str(new_price) + "$"
    # if(new_price < curr_price):
    update_db(new_price)
    send_email(body)
    
elif notification_type == 1:
    new_price = api_call()
    curr_price, product_name = get_from_db()
    update_db(new_price)
    body = '''
    Hello user the current price for product
    ''' + product_name + " is: " + new_price + "$"
    send_email(new_price, body)