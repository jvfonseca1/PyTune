import logging
import sys

logger = logging.getLogger("pytune")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)