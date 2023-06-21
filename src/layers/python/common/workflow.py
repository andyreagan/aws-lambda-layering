from aws_lambda_powertools import Logger

from db.models import Customer
from models import CustomerInformation


def get_customer_info(customer_id: str) -> CustomerInformation:
    logger = Logger(service="AWS Lambda Layering Test")
    logger.debug(f"Getting customer info for {customer_id}")
    customer = Customer.objects.get(customerId=customer_id)
    logger.debug(f"Got customer info for {customer_id}")
    return CustomerInformation(**customer.__dict__)
