import glob
import logging
from importlib import import_module
from os.path import basename, isdir, isfile
from pathlib import Path

from aiogram import Dispatcher


class ModuleManager:
    """
    Module Manager.
    """

    def __init__(self, dp: Dispatcher, modules):
        self.dp = dp
        self.modules = modules
        self.root = Path(__file__).parent.parent

    def _load_path(self, path: str):

        mod_paths = glob.glob(f"{self.root}/{path}/*.py")

        all_modules = [
            basename(module)[:-3]
            for module in mod_paths
            if isfile(module)
            and module.endswith(".py")
            and not module.endswith("__init__.py")
        ]

        for module in all_modules:
            self._load(path.replace("/", ".") + f".{module}")

    def _load(self, module: str):

        try:
            imp_module = import_module("app." + module)
        except ModuleNotFoundError:
            logging.error(f"Module <{module}> was not found.")
            raise SystemExit()

        if not hasattr(imp_module, "setup"):
            logging.error(f"Module <{module}> doesn't seem to have <setup>.")
            raise SystemExit()

        if not callable(imp_module.setup):
            logging.error(f"<setup> is not callable in <{module}>.")
            raise SystemExit()

        try:
            imp_module.setup(self.dp)
        except Exception as error:
            logging.exception(f"An error occured in <{module}>: {error}")
            raise SystemExit()

        logging.debug(f"Module <{module}> was loaded.")
        return True

    def load(self):
        """
        Iterates through modules and loads them
        """

        for module in self.modules:
            if isdir(f"{self.root}/{module}/"):
                self._load_path(module)
            else:
                self._load(module)
