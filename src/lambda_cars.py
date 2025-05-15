import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Amazon API Getway Lambda proxy integration. 
    Access to the request and payload, including headers and 
    status code.
    """

    logger.debug(event)

    cars = [
        {"id": "1", "brand": "BMW",       "available": "true"},
        {"id": "2", "brand": "Audi",      "available": "false"},
        {"id": "3", "brand": "Mercedes",  "available": "true"},
        {"id": "4", "brand": "Honda",     "available": "false"},
        {"id": "5", "brand": "Toyota",    "available": "true"},
        {"id": "6", "brand": "Ford",      "available": "true"},
        {"id": "7", "brand": "Chevrolet", "available": "false"},
        {"id": "8", "brand": "Nissan",    "available": "true"},
        {"id": "9", "brand": "Volkswagen","available": "false"},
        {"id": "10","brand": "Kia",       "available": "true"}
    ]

    resource = event['resource']

    err = None

    response_body = {}
    logger.info(f"starting {resource}")
    # /cars list all cars
    if (resource == "/cars"):
        response_body = {
            "cars": cars
        }
    # /cars/id find car by id
    
    elif (resource == "/cars/{id}"):
        cars_id = event['pathParameters']['id']
        value = next((item for item in cars if item["id"] == str(cars_id)), False)

        if value == False:
            err = 'Cars not found'
        else:
            response_body = {
                "cars" : value
            }

    respone = response_payload(err, response_body)

    return respone


def response_payload(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json'
        }
    }