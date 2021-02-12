"""Generates a config"""

from os.path import isfile
from pathlib import Path


def main():
    prefix = f"\033[32m•\033[0m"
    project_path = Path(__file__).parent.parent.parent
    config_path = f"{project_path}/config.yml"

    print(f"{prefix} Creating default config file...")

    if isfile(config_path):

        answer = input(
            f"{prefix} Config file is going to be overwritten. Proceed? [Y/n] "
        ).strip().lower()

        if answer not in {"y", "yes", "yep", "sure", ""}:
            return False

    token = input(f"{prefix} Enter your token: ")

    # Note: it's NOT a config, it's used for generating configs
    default_conf = """
app:
  bot:
    token: %TOKEN%
    parse_mode: html

  executor:
    skip_updates: true

  superusers:
    - null

  commands:
    {
      start: 'Start conversation with me'
    }
""".replace("%TOKEN%", token)

    with open(config_path, "w") as file:
        file.write(default_conf)

    print(f"{prefix} Config has successfully been created!")


if __name__ == "__main__":
    main()