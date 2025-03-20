import nonebot
import logging
from config import base_config
from nonebot.adapters.onebot.v11 import Adapter

logger = logging.getLogger(__name__)

nonebot.init(**base_config)

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_plugins("src/plugins")

if __name__ == "__main__":
    nonebot.run()