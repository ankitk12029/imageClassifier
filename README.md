
# 🧠 AWS Image Classification Project

A cloud-native image classification application built on AWS using services such as Amazon S3, Lambda, API Gateway, SageMaker, and DynamoDB. This project allows users to upload images through a static web interface, classify them using a pre-trained ML model (MobileNet V3), and display the predicted label.



## 📊 Project Architecture

![Image_classifier_flow_diagram-1](https://github.com/user-attachments/assets/61ceba06-1da2-4c4c-91bb-9c41950df7e4)


The architecture leverages several AWS services to create a serverless pipeline from image upload to classification output.



---

## 🔄 Flow Overview

1. **User Interface**  
   - Hosted via CloudFront (static website)
   - Allows users to upload images and request predictions
     <img width="655" alt="SCR-20250515-tdxp" src="https://github.com/user-attachments/assets/d0acffcc-0ad7-46cd-b51f-c06c7c2c1f15" />


2. **API Gateway**  
   - Exposes RESTful endpoints:
     - `POST /upload`: Upload image to S3
     - `GET /predict`: Retrieve prediction from DynamoDB

3. **AWS Lambda**  
   - `postImageS3`: Uploads base64 image to S3
   - `classifyImageFunction`: Triggered by S3 event, classifies image using SageMaker
   - `getPrediction`: Fetches label from DynamoDB

4. **Amazon S3**  
   - Stores user-uploaded images (private access only)

5. **Amazon SageMaker AI**  
   - Hosts the pre-trained ML model for image classification

6. **Amazon DynamoDB**  
   - Stores predicted labels indexed by image filename

7. **Amazon CloudFront**  
   - Delivers the frontend UI securely

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: AWS Lambda (Python)
- **Model**: MobileNet V3 (via SageMaker)
- **AWS Infrastructure**: S3, API Gateway, CloudFront, IAM, DynamoDB, CloudWatch, SageMaker AI, Lambda, 

---

## 🚀 How It Works

- User uploads an image through the web UI.
- Image is sent to API Gateway → `postImageS3` Lambda → S3 Bucket.
- S3 triggers `classifyImageFunction`, which calls SageMaker and stores result in DynamoDB.
- User requests prediction through UI → API Gateway → `getPrediction` Lambda → fetches label from DynamoDB.


