import time
from typing import Callable

from fastapi import Request, Response
from fastapi.routing import APIRoute
from starlette.background import BackgroundTask

from .utils import logger


def log_info(request: Request, response: Response, route_handler: str) -> None:
    logger.append_keys(
        fastapi={
            "path": request.url.path,
            "route": route_handler,
            "method": request.method,
        }
    )
    logger.info("Received request")

    logger.append_keys(
        fastapi={
            "duration": response.headers["X-Response-Time"],
            "status": response.status_code,
            "response": response.body.decode("utf-8"),
        }
    )
    logger.info("Request completed")


class LoggerRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before

            response.headers["X-Response-Time"] = str(duration)

            # Add fastapi context to logs
            task = BackgroundTask(
                log_info, request=request, response=response, route_handler=str(self.path)
            )
            response.background = task

            return response

        return route_handler
