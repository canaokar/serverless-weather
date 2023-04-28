# Serverless Web App for Leveraging Serverless workshop

## Step 1 - Create Lambda Function (Logic)

1. Open AWS Console, go to Services > Lambda
2. Click on Create Function
3. Enter these details:
    - Select Author from Scratch
    - Enter Function Name as 'gatechWeather-<YOUR-NAME>'
    - Runtime: Python 3.10
4. Click Create Function
5. Open [https://github.com/canaokar/serverless-weather] and navigate to *lambda_function.py*
6. Paste the contents of the file into the edior on Lambda page.
7. Register to get your API Key here: [https://openweathermap.org/api]
8. Enter the API Key in the placeholder in the Lambda code.

## Step 2 - Test your Lambda Function:
