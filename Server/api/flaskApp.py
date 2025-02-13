#this api is used to get the status of the assistant and to check if the server is online.
#this server acts as a brdge between the py assistant and the react frontend.
#info will be sent to the frontend and the frontend will send the info to the server via json.
#flask is used to create this api.



from flask import Flask, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
# Update CORS configuration to allow specific origin
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://172.20.10.2:3000", "http://localhost:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Global state to track assistant status
assistant_state = {
    'is_listening': False,
    'last_transcript': '',
    'last_response': '',
    'is_processing': False
}

@app.route('/api/status')
def get_status():
    response = jsonify(assistant_state)
    return response

@app.route('/api/health')
def health_check():
    response = jsonify({'status': 'online'})
    return response

def start_api():
    app.run(host='0.0.0.0', port=5000, debug=False)