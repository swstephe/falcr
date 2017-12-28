import logging
import os

logging.basicConfig(level=logging.DEBUG)

getLogger = logging.getLogger
CWD = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(CWD)
DATABASE = 'mysql+pool://root:root@localhost/falcr?max_connections=20&stale_timeout=300'
