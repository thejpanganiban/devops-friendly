import logging
import sys


def setup(level=logging.DEBUG):
    logging.basicConfig(
        stream=sys.stdout,
        level=level,
        # Fancy formatting.
        format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %z'
    )
