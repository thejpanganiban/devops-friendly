from flask import Flask, jsonify
import config
import logging
import logconfig


# A stateful function that configures logging to stream to
# stdout.
logconfig.setup(getattr(logging, config.LOGLEVEL, logging.DEBUG))


app = Flask(__name__)
app.config.from_object(config)
logger = logging.getLogger(__name__)


@app.route('/')
def page_index():
    # We're demonstrating two log levels here. Info is
    # turned on by default while debug is only available
    # when we have LOGLEVEL set to DEBUG.
    logger.info('got a request')
    logger.debug('requesting system info')
    system_info = {
        'DATABASE_URL': config.DATABASE_URL,
        'CACHE_URL': config.CACHE_URL,
        'HOST': config.HOST,
        'PORT': config.PORT,
    }
    logger.debug('system info fetched')
    return jsonify(system_info)
