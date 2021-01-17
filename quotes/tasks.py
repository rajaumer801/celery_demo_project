from celery.utils.log import get_task_logger

from celery_demo_project.celery import app
from quotes.controllers import get_random_quotes, remove_oldest_quote

logger = get_task_logger(__name__)


@app.task(name="get_random_quotes_task")
def get_random_quotes_task():
    logger.info("getting random quote")
    return get_random_quotes()


@app.task(name="remove_oldest_quote_task")
def remove_oldest_quote_task():
    logger.info("remove oldest quote")
    return remove_oldest_quote()
