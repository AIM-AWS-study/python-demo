from flask import Flask, jsonify 
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'This is AWS Study\'s perfect project!!!',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/test')
def test():
    return jsonify({
        'status': 'server test',
        'service': 'python-demo-server'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)