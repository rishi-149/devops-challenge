from flask import Flask
import redis
import os
import sys

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

try:
    r = redis.Redis(host=redis_host, port=6379)
    r.ping()
    print("Connected to Redis")

except Exception as e:
    print("Redis connection failed:", e)
    sys.exit(1)

@app.route('/')
def home():
    return "DevOps Challenge Running!"

@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)