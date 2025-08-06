from flask import Flask, render_template, jsonify
from regression import predict_failure, calculate_health_score
import datetime
import random

app = Flask(__name__)

# Dummy data for demo
aircraft_data = {
    "flight_hours": 1200,
    "sensor_readings": [random.uniform(0, 1) for _ in range(10)]
}

@app.route('/')
def index():
    health_score = calculate_health_score(aircraft_data["sensor_readings"])
    failure_pred = predict_failure(aircraft_data["sensor_readings"])

    return render_template('index.html',
                           health_score=health_score,
                           failure_prediction=failure_pred)

@app.route('/api/chart-data')
def chart_data():
    # Send dummy time-series data for charts
    now = datetime.datetime.now()
    timestamps = [(now - datetime.timedelta(hours=i)).strftime('%Y-%m-%d %H:%M') for i in reversed(range(24))]
    values = [random.uniform(0, 1) for _ in range(24)]
    return jsonify({"timestamps": timestamps, "values": values})

@app.route('/api/calendar-events')
def calendar_events():
    # Dummy maintenance calendar events
    events = [
        {"date": "2025-06-01", "title": "Engine check"},
        {"date": "2025-06-10", "title": "Software update"},
        {"date": "2025-06-15", "title": "Hydraulics inspection"},
    ]
    return jsonify(events)

@app.route('/api/alerts')
def alerts():
    # Dummy alerts
    alerts = [
        {"type": "warning", "message": "Hydraulics pressure low"},
        {"type": "info", "message": "Next maintenance due in 5 days"},
    ]
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)
