from aws_lambda_powertools import Logger
from django.db import models

from db_utils import init_django

init_django()

logger = Logger(service="AWS Lambda Layering Test")


class Customer(models.Model):
    customerId = models.CharField(max_length=100)
