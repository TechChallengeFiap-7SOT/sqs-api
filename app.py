from fastapi import FastAPI, HTTPException
import boto3
import json
import os

app = FastAPI()

sqs = boto3.client(
    'sqs',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    region_name=os.getenv("AWS_REGION", "us-east-1")
)
queue_url = os.getenv("SQS_QUEUE_URL")

@app.post("/send-message/")
async def send_message(message: dict):
    try:
        print(message)
        message_body = json.dumps(message)
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        return {"message": "Mensagem enviada com sucesso!", "MessageId": response["MessageId"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
