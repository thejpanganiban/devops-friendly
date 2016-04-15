from flask import Flask, jsonify
import config


app = Flask(__name__)


@app.route('/')
def page_index():
    return jsonify({
        'DATABASE_URL': config.DATABASE_URL,
        'CACHE_URL': config.CACHE_URL,
    })
