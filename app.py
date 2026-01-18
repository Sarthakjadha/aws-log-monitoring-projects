import logging
import random
import time

logging.basicConfig(
    filename="/var/log/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

while True:
    if random.choice([True, False]):
        logging.error("ERROR: Database connection failed")
    else:
        logging.info("INFO: Application running normally")

    time.sleep(10)
