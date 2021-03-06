### [![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)  [![Aiogram](https://img.shields.io/badge/aiogram-2.11.2-blue)](https://pypi.org/project/aiogram/) 

### About
Scalable and straightforward template for bots written on [aiogram](https://github.com/aiogram/aiogram) with built-in module management system. Inspired by a couple of other templates mentioned later.

### Setting it up

#### System dependencies
- Python 3.7+
- GNU/Make 
- GIT

#### Preparations
- Clone this repo via `git clone https://github.com/comictomcat/aiogram-template.git`;
- Move to the directory `cd aiogram-template`.

#### Poetry Deployment
- **Note:** You need to have Poetry installed: `pip install poetry`;
- Install dependencies: `make install`;
- Rename `config.yaml.example` to `config.yaml` and replace a token placeholder with your own one;
- Start the bot: `make run`.

#### Maintenance
*Use `make help` to view available commands*

- Update dependencies `make update`;
- Reformat code `make lint`.

### Other templates
 - [aiogram-bot-template](https://github.com/Latand/aiogram-bot-template) by Latand
 - [aiogram-template](https://github.com/F0rzend/aiogram-template) by F0rzend
 - [tgbot_template](https://github.com/Tishka17/tgbot_template) by Tishka17
 - [aiogram-bot-template](https://github.com/Forden/aiogram-bot-template) by F0rden
