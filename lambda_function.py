import json
import urllib.request

def lambda_handler(event, context):
    # Retrieve the latitude and longitude values from the query string parameters
    latitude = event['queryStringParameters']['latitude']
    longitude = event['queryStringParameters']['longitude']
    apikey = 'ADD_API_KEY_HERE'
    
    # Build the URL
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial'.format(latitude, longitude, apikey)
    
    # Make the API request
    req = urllib.request.urlopen(url)
    res = req.read()
    
    # Parse the JSON response
    data = json.loads(res)
    
    # Extract the information you need from the JSON data
    location = data['name']
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    
    # Construct Response
    response = {
        'location': location,
        'temperature': temperature,
        'weather': weather
    }
    
    # Return the extracted information in a JSON object
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }
