import glob
import logging
from importlib import import_module
from os.path import basename, isdir, isfile

from aiogram import Dispatcher


class ModuleManager:
    """
    Module Manager.
    """

    def __init__(self, dp: Dispatcher, root: str):
        self.dp = dp
        self.root = root

    def load_path(self, path: str):
        """
        Goes through all modules in path and loads them.
        """

        mod_paths = glob.glob(f"{self.root}/{path}/*.py")

        all_modules = [
            basename(module)[:-3]
            for module in mod_paths
            if isfile(module) and module.endswith(".py")
        ]

        for module in all_modules:
            self.load(path.replace("/", ".") + f".{module}")

    def load(self, module: str):

        try:
            imp_module = import_module("app." + module)
        except ModuleNotFoundError:
            logging.error(f"Module <{module}> was not found.")
            raise SystemExit()

        if not hasattr(imp_module, "setup"):
            logging.error(f"Module <{module}> doesn't have <setup>.")
            raise SystemExit()

        if not callable(imp_module.setup):
            logging.error(f"Module <{module}> doesn't have callable <setup>.")
            raise SystemExit()

        try:
            imp_module.setup(self.dp)
        except Exception as error:
            logging.exception(f"An error occured in <{module}>: {error}")
            raise SystemExit()

        logging.debug(f"Module <{module}> was loaded.")
        return module

    def load_all(self, modules: list):
        """
        Iterates through modules and loads them.
        """

        for module in modules:

            # Shortcut for %module%.__init__
            if module.startswith("$"):
                self.load(f"{module[1:]}.__init__")

            elif isdir(f"{self.root}/{module}/"):
                self.load_path(module)

            else:
                self.load(module)
