import logging

from aiogram import Dispatcher


async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all
    exceptions within task factory tasks.
    """

    logging.exception(exception)
    logging.debug(update)

    return True


def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
