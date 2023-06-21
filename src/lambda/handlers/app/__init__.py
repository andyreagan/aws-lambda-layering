from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


from models import CustomerInformation

from .router import LoggerRouteHandler
from .utils import logger, tracer
from workflow import get_customer_info

app = FastAPI(
    title="AWS Lambda Layering Test"
)
app.router.route_class = LoggerRouteHandler


@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    corr_id = request.headers.get("x-correlation-id")

    if not corr_id:
        corr_id = request.scope["aws.context"].aws_request_id

    logger.set_correlation_id(corr_id)
    tracer.put_annotation(key="correlation_id", value=corr_id)
    response = await call_next(request)
    response.headers["X-Correlation-Id"] = corr_id
    return response


@app.exception_handler(Exception)
async def unhandled_exception_handler(request, err):
    logger.exception("Unhandled exception")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})



@app.get("/customer/{customer_id}")
def get_customer(customer_id: str) -> CustomerInformation:
    return get_customer_info(customer_id)
