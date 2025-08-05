from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔐 Replace these with your actual Supabase values:
SUPABASE_URL = 'https://ofkrurzmtvnzacjzgkhj.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9ma3J1cnptdHZuemFjanpna2hqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQzNjU1MjQsImV4cCI6MjA2OTk0MTUyNH0.byoIYML6DiwCZax3GkuxBpHgaA-TgXVTGjw35Uvjd-w'
SUPABASE_TABLE = 'tasks'

@app.route('/')
def home():
    return "Task Tracker API is running"

@app.route('/submit-task', methods=['POST'])
def submit_task():
    data = request.json

    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}',
        headers=headers,
        json=data
    )

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
