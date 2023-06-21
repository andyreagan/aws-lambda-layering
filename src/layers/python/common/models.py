from aws_lambda_powertools.utilities.parser import BaseModel


class CustomerInformation(BaseModel):
    customerId: str
