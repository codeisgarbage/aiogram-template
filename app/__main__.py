from loguru import logger
from aiogram import executor, Dispatcher

# noinspection PyUnresolvedReferences
from app import dp, middlewares, filters, handlers, config
from app.misc import set_commands, mailing


async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""
    await mailing(dispatcher, config.superusers, "Bot has started")
    logger.info("Bot has started")

    # Command hints
    await set_commands(dispatcher, config.commands)


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(
        dp, on_startup=startup, **config.executor
    )
