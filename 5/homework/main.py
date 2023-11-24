import asyncio

from misc.config import read_config
from misc.log import *

from db.tasks import run_async_fetch_from_db

CONFIG_ENV_KEY = 'SRVC_CONFIG'
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    config_path = os.environ[CONFIG_ENV_KEY]
    conf = read_config(config_path)
    db_conf = conf.get("db")
    category_names = ['Электроника', 'Телефоны', 'Компьютеры']
    results = asyncio.run(run_async_fetch_from_db(db_conf, category_names))
    logger.info(results)
