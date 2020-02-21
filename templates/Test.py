import json
import base64
import boto3


def lambda_handler(event, context):
    s3 = boto3.resource("s3")

    # retrieving data from event
    get_file_content = event["content"]
    print(event['fileName'])
    name = event['fileName']
    # decoding data
    decode_content = base64.b64decode(get_file_content)
    s3upload = s3.Bucket('twitterbucket123').put_object(Key='myfolder/' + name, Body=decode_content)
    metadata = s3.Object('twitterbucket123', 'myfolder/abc.jpeg')
    print(metadata)
    return {
    "statusCode": 200,
    "body": json.dumps(metadata)
    }