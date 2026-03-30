from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/forecast', methods=['GET'])
def forecast():
    # Dummy data for forecast
    data = {
        'location': 'Sample Location',
        'forecast': 'Sunny',
        'temperature': 20
    }
    return jsonify(data)

@app.route('/api/historical', methods=['GET'])
def historical():
    # Dummy data for historical weather data
    data = {
        'location': 'Sample Location',
        'historical_data': [
            {'date': '2026-03-01', 'temperature': 15},
            {'date': '2026-03-02', 'temperature': 17}
        ]
    }
    return jsonify(data)

@app.route('/api/trends', methods=['GET'])
def trends():
    # Dummy data for trends
    data = {
        'location': 'Sample Location',
        'trends': 'Increasing temperatures over the last month'
    }
    return jsonify(data)

@app.route('/api/comparison', methods=['GET'])
def comparison():
    # Dummy data for comparison
    data = {
        'location': 'Sample Location',
        'comparison': {
            'current_temp': 20,
            'average_temp': 18
        }
    }
    return jsonify(data)

@app.route('/api/health', methods=['GET'])
def health():
    # Health check
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True)
