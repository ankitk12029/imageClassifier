import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb', region_name='<your-region>')  # Replace with your AWS region

    bucket_name = '<bucket-name>'  # Replace with your bucket name
    table = dynamodb.Table('<table-name>')  # Replace with your DynamoDB table name

    try:
        # Get latest image from S3
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in objects or not objects['Contents']:
            return {
                "statusCode": 404,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": "No images found in S3."
            }

        # Sort objects by LastModified date and get the latest one
        latest_object = sorted(objects['Contents'], key=lambda x: x['LastModified'], reverse=True)[0]
        print("this is latest",latest_object)
        image_name = latest_object['Key']

        # Get prediction from DynamoDB
        response = table.get_item(Key={'ImageName': image_name})
        item = response.get('Item')

        # Check if item exists and contains the predicted label
        if not item or 'PredictedLabel' not in item:
            return {
                "statusCode": 404,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": "Prediction not found."
            }

        # Return just the plain predicted label
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "text/plain"
            },
            "body": item['PredictedLabel']  # NO json.dumps()
        }

    # Handle any errors
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": str(e)  # return error as plain text
        }
