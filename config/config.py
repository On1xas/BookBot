from dataclasses import dataclass

from environs import Env

@dataclass
class TgBot:
    token: str
    admin_list: list



@dataclass
class Config:
    tgbot: TgBot

def get_config(path_to_env):
    env=Env()
    env.read_env(path_to_env)
    return Config(tgbot=TgBot(token=env("BOT_TOKEN"), admin_list=list(map(int, env.list('ADMIN_IDS')))))