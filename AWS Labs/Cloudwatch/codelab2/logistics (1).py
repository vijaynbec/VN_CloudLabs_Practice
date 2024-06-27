import json
import logging
import random
import time

def lambda_handler(event, context):
    
    # simulate random inputs
    source_id = random.randint(0, 999999999)
    destination_id = random.randint(0, 999999999)
    error_likelihood = random.randint(1, 10)
    duration_simulation = random.randint(0, 2000)
    
    # simulate logistics engine
    time.sleep(duration_simulation / 1000)
    
    # simulate error
    if error_likelihood == 5:
        raise ValueError('The logistics function could not link the source package to the destination')
   
    return {
        'statusCode': 200,
        'body': json.dumps('The source package has been linked to the destination')
    }
