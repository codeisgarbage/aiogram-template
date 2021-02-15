from pathlib import Path

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    """
    YAML config parser
    """

    def __init__(self, path: str or Path):
        with open(path) as file:
            self.config = load(stream=file, Loader=Loader)

        self._set_shortcuts()

    def _set_shortcuts(self):
        """
        A private method that sets shortcut for elements in `app`
        it's created to be able use config.bot
        instead of config.app.get('bot') and others
        """
        for key, value in self.app.items():
            setattr(self, key, value)

    def __getattr__(self, key, default=None):
        """
        A shortcut for get method
        """
        if default is None:
            default = dict()

        return self.config.get(key, default)

    def get(self, key, default=None) -> dict:
        return self.__getattr__(key, default)
