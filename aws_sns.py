"""Summary
    Allow sending of text messages for garage door events

Attributes:
    ACCESS (string): access key for aws
    REGION (string): region for aws
    SECRET (string): secret key for aws
"""
import time
import os
import boto3


ACCESS = os.environ.get("AWS_ACCESS_KEY")
SECRET = os.environ.get("AWS_SECRET_KEY")
REGION = os.environ.get("AWS_REGION")
SNS_TOPIC = os.environ.get("'arn:aws:sns:us-east-1:458816371970:GarageDoor'")


def get_time():
    """Summary
        retreive current time and return formatted version

    Returns:
        string: formatted time
    """
    return str(time.strftime('%I:%M %p'))


def is_open():
    """Summary
        Formats message for open garage door
    """
    publish('Garage Door Is Open. {time}'.format(time=get_time()), SNS_TOPIC)


def nightly_check(status):
    """Summary
        Send nightly SMS message with current status are predetermined time
    Args:
        Status (String): status of garage door
    """
    publish('Garage Door Is {status}.{time}'.format(
        status=status, time=get_time()), SNS_TOPIC)


def publish(message, topic):
    """Summary
        Publish passed in message to aws sns
    Returns:
        TYPE: Description
    """
    sns_client = boto3.client(
        'sns',
        region_name=REGION,
        aws_access_key_id=ACCESS,
        aws_secret_access_key=SECRET)

    sns_client.publish(
        TopicArn=topic,
        Message=message)
