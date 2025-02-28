from boto3 import resource
from boto3.resources.base import ServiceResource

def dynamodb() -> ServiceResource:
    ddb = resource('dynamodb', region_name="ap-northeast-1")
    return ddb
