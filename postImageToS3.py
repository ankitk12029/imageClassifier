import json
import boto3
import base64

# Initialize S3 client
s3 = boto3.client('s3')
bucket_name = '<buckect-name>'  #  Replace with your actual S3 bucket name

def lambda_handler(event, context):
    try:
        # Extract the filename and base64 image data
        filename = event['filename']
        filedata = event['filedata']

        #  Fix base64 padding if needed
        def add_padding(b64_string):
            return b64_string + '=' * (-len(b64_string) % 4)

        filedata_padded = add_padding(filedata)
        decoded_image = base64.b64decode(filedata_padded)

        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=filename,
            Body=decoded_image,
            ContentType='image/jpeg'  # You can detect this dynamically if needed
        )

        #  Return success response
        return {
            'statusCode': 200,
            'body': json.dumps(f"Image '{filename}' uploaded successfully!")
        }
 
    except Exception as e:
        # Handle any errors
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
