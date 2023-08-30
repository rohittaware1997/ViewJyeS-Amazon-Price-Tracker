def api_call()
#     import requests
#
#     url = 'https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-lookup-reviews'
#     params = {
#       'page': '1',
#       'domainCode': 'com',
#       'asin': 'B08R9V9YZC',
#       'sortBy': 'recent',
#       'filters': 'reviewerType=avp_only_reviews;filterByStar=five_star'
#     }
#     headers = {
#       'X-RapidAPI-Key': '66c541bacbmsh85cf0b8b88f61d5p120a8fjsn8b4e49b92bef',
#       'X-RapidAPI-Host': 'axesso-axesso-amazon-data-service-v1.p.rapidapi.com'
#     }
#
#     response = requests.get(url, params=params, headers=headers)
#
#     if response.status_code == 200:
#         print(response.json()['reviews'][0]['text'])
#     else:
#         print('Error:', response.status_code)
#         print(response.json())
    print("Heyyy")