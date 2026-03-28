import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from Cloud Run! Deployed by Gautam Raju."

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "service": os.environ.get("K_SERVICE", "unknown"),
        "revision": os.environ.get("K_REVISION", "unknown"),
        "region": os.environ.get("GOOGLE_CLOUD_REGION", "unknown"),
        "port": os.environ.get("PORT", "8080"),
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
