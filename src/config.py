import os


DATABASE_URL = os.environ.get('DATABASE_URL', 'mysql://username:password@localhost:3306/mydb')
CACHE_URL = os.environ.get('CACHE_URL', 'redis://localhost:6709')
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000)
