# Serverless Web App for Leveraging Serverless workshop

## Login to the console
1. Navigate to [https://console.aws.amazon.com/console/home] in your browser
2. Enter the Account ID, Username, Password provided to you on the screen.

## Step 1 - Create Lambda Function (Logic)

1. Open AWS Console, go to Services > Lambda
2. Click on Create Function
3. Enter these details:
    - Select Author from Scratch
    - Enter Function Name as 'gatechWeather-YOUR-NAME'
    - Runtime: Python 3.10
4. Click Create Function
5. Open [https://github.com/canaokar/serverless-weather] and navigate to *lambda_function.py*
6. Paste the contents of the file into the editor on Lambda page.
7. Register to get your API Key here: [https://openweathermap.org/api]
8. Enter the API Key in the placeholder in the Lambda code.

## Step 2 - Test your Lambda Function:

1. Click on **Test** button on your Lambda Screen
2. Select Create New event
3. Enter Event name - **Test**, or anything you like
4. Enter this in Event JSON:
```
{
  "queryStringParameters": {
    "latitude": "33.7490",
    "longitude": "-84.3880"
  }
}
```

## Step 3 - Create an API

1. Click on **+Add Trigger**
2. Select `API Gateway` from Dropdown
3. Create **New API**
4. Select these details:
    - Select **HTTP**
    - Security **Open**
    - Under Additional Settings enable Cross-origin resource sharing (CORS) *[IMPORTANT]*
5. Click Add
6. Copy the API Endpoint and paste locally for future use.
Endpoint will look something like this:
```
https://abcdefghi123.execute-api.<region>.amazonaws.com/default/gatechWeather-YOUR-NAME
```

## Step 4 - Create frontend webpage
    
1. Go to Services > S3
2. Click *Create Bucket*
3. Enter these details:
    - Name `gatech-weather-<YOUR-NAME>`
    - Uncheck Block Public Access
    - Check *I agree* on the next prompt
    - Click **Create Bucket**
4. Click on Bucket Name, Go to Properties Tab, Scroll Down, Click Edit near Static Website Hosting
5. Click Enable. In Index Document, enter `index.html`, Click Save Changes
6. Scroll down and copy the URL for future use.
7. Scroll up and go to Permissions > Bucket Policy > Edit
8. Copy the bucket ARN from top of the section. It will look something like:
`arn:aws:s3:::gatech-weather-YOUR-NAME`

9. Copy below policy into the page:
```
{
  "Id": "Policy1682690362649",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1682690360714",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "<ENTER BUCKET ARN HERE>/*",
      "Principal": "*"
    }
  ]
}
```
10. Replace the "<ENTER BUCKET ARN HERE>" with the value copied above. *Do not* delete the /* in front of it. 

## Step 5 - Put everything in place
    
1. Return to S3 page
2. Open the `index.html` file in your file editor on your computer and enter the API Gateway URL on `line 103`
3. Go to Objects, upload, and upload the index.html file
4. Voila! Open the website from the S3 website URL you copied. 
