import json
from patent_score import score
def handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'score': score(event['title'])
    }
