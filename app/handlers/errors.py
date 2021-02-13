from loguru import logger

from app import dp, config
from app.misc import mailing


async def errors_handler(update, exception):
    """Exceptions handler. Catches all
    exceptions within task factory tasks."""
    
    message = f"Error:\n{exception}\n\nUpdate: {update}"

    await mailing(dp, config.superusers, message)
    logger.exception(message)


def setup(dispatcher):
    dispatcher.register_errors_handler(errors_handler)
