""" Common db utility code used by all Python Lambda code """
import logging

from aws_lambda_powertools import Logger
from common_settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

logger = Logger(service="AWS Lambda Layering Test")

logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            "db",
        ],
        TIME_ZONE="UTC",
        USE_TZ=True,
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": DB_NAME,
                "USER": DB_USER,
                "HOST": DB_HOST,
                "PORT": DB_PORT,
                "PASSWORD": DB_PASSWORD,
            }
        },
    )
    logger.debug("Django environment configred")
    django.setup()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()
