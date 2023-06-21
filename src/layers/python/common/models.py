from aws_lambda_powertools.utilities.parser import BaseModel


class CustomerInformation(BaseModel):
    customerId: str


class HealthCheckModel(BaseModel):
    status: str = "ok"
