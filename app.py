from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SUPABASE_URL = 'https://ofkrurzmtvnzacjzgkhj.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9ma3J1cnptdHZuemFjanpna2hqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQzNjU1MjQsImV4cCI6MjA2OTk0MTUyNH0.byoIYML6DiwCZax3GkuxBpHgaA-TgXVTGjw35Uvjd-w'  # Keep this secure
SUPABASE_TABLE = 'tasks'

@app.route('/')
def home():
    return "✅ Task Tracker API is Live on Render"

@app.route('/submit-task', methods=['POST'])
def submit_task():
    data = request.json
    required_fields = ['user', 'task', 'start_time', 'end_time', 'date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

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

@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({'error': 'start_date and end_date are required'}), 400

    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}'
    }

    query = f"?select=*&date=gte.{start_date}&date=lte.{end_date}"

    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}{query}",
        headers=headers
    )

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run()
