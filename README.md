# ViewJyeS-Amazon-Price-Tracker

![UML](https://user-images.githubusercontent.com/123285556/227429352-7174aa9a-07bc-4fd3-8fde-26032fdcbfc3.jpeg)

Final Project Submission

[Web Application / Production Application](http://cicdipelineflaskviewjayes.s3-website-us-east-1.amazonaws.com)
- We have deployed our application on Frontend and all the code is present inside Frontend folder.

[Data Collection](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/blob/main/Backend/flask/asin.py)
- This points to the ASIN file which is called by the cron-job to collect the latest information on the price and send mail according to the user preference.

[Data Analyzer](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/tree/main/Backend/flask)
- We have Sentiment Analysis model which is trained and pickled and ready to be, Refer Training and Predict file in the above, also app.py in the folder is responsible to check what type of notification service is selected by user and set cron jobs accordingly. Check '/track' endpoint in the app.py file for the exact details.

[Data Presistent](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/tree/main/Backend/flask)
- We are using MYSQL for storing all the details from user and product, The app.py code and asin.py files make the required connection to the DB which is hosted on a separate EC2 machine. Refer to those files.

[REST API endpoint](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/blob/main/Backend/flask/app.py)
- The app.py has all the endpoints which the user will be connecting.

[CI/CD](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/blob/main/.github/workflows/python-app.yml)
- The python-app.yml script has all the necessary details for Continuous Integration and Deloyment.

[Unit Test](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/tree/main/Backend/test)
For the backend system we have done the following testing.

- The setUp method is called before each test method to set up data or resources. It initializes instance variables and tests the api_call, update_db, and get_from_db functions. It uses @patch to replace the requests.request, mydb.commit, and cursor.execute methods with mock objects.

- Test cases test the "/register" endpoint, "/login" endpoint, "/track" endpoint, and "/fetchCards" endpoint. The tests send PUT requests with email and full name data, and check if the response status code is 200 and if the response data contains strings such as "email", "productName", "asinServer", "imageUrl", "currentPrice", and "productLink". The tests also suggest to add database assertions to check the returned data from the database query.

[Event Collabraion/ Messaging Protocol](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/tree/main/Backend/flask)
- Refer to the rabbitmq and rabbitmq_consumer python file which handles all the message queue related data handling.

[Production Monitoring](http://34.203.234.126:9090/targets)
- The above link will take you to the prometheus page on the EC2 machine, We have used grafana on local machine to connect to prometheus and monitor the data. We tracked the total request parameter on Grafana, also we used AWS Cloudwatch to metrics on EC2 and S3 bucket.

[Integration Testing and Acceptance Testing](https://github.com/CSCI-5828-Foundations-Sftware-Engr/ViewJyeS-Amazon-Price-Tracker/tree/main/Frontend/Amazon-Tracker-Frontend/test/jest)
- For the Frontend we tested the individual component, and all the files are placed in the __test__ folder, Also along side this we tried writing test cases that mimick user behavior.
