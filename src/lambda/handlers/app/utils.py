from aws_lambda_powertools import Logger, Tracer

logger: Logger = Logger(service="AWS Lambda Layering Test")
tracer: Tracer = Tracer(service="AWS Lambda Layering Test")
