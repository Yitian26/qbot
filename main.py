import nonebot
import logging

from nonebot.adapters.onebot.v11 import Adapter

logger = logging.getLogger(__name__)

base_config = {
    "websocket_port": 8080,
    "host": "127.0.0.1",
    "log_level": "INFO",
}

nonebot.init(**base_config)

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_plugins("src/plugins")

if __name__ == "__main__":
    nonebot.run()