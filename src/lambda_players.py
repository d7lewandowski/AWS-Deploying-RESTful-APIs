import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.debug(event)


    players = [
        {'id': '1', 'name': 'John', 'lastname': 'Rogan', 'Sport': 'football'},
        {'id': '2', 'name': 'Alice', 'lastname': 'Smith', 'Sport': 'basketball'},
        {'id': '3', 'name': 'Bob', 'lastname': 'Johnson', 'Sport': 'tennis'},
        {'id': '4', 'name': 'Emily', 'lastname': 'Davis', 'Sport': 'swimming'},
        {'id': '5', 'name': 'Michael', 'lastname': 'Brown', 'Sport': 'baseball'},
        {'id': '6', 'name': 'Linda', 'lastname': 'Garcia', 'Sport': 'volleyball'},
        {'id': '7', 'name': 'David', 'lastname': 'Martinez', 'Sport': 'football'},
        {'id': '8', 'name': 'Sophia', 'lastname': 'Lopez', 'Sport': 'gymnastics'},
        {'id': '9', 'name': 'Chris', 'lastname': 'Lee', 'Sport': 'hockey'},
        {'id': '10', 'name': 'Emma', 'lastname': 'Clark', 'Sport': 'rugby'}
    ]

    resource = event['resource']
    
    print("Received event: " + json.dumps(event, indent=2))

    err = None
    logger.info(f"starting {resource}")
    # /players list of all players

    response_body = {}

    if (resource == '/players'):
        response_body = {
            "players": players
        }
    # /players/id find by id player
    elif (resource == '/players/{id}'):
        player_id = event['pathParameters']['id']
        value = next((item for item in players if item["id"] == str(player_id)), False)

        if value == False:
            err = "Player not found"
        else:
            response_body = {
                "player": value
            }
    



        
    response =  response_payload(err, response_body)

    return response
  
  
    
def response_payload(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }