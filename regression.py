import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy linear regression model for demo
def predict_failure(sensor_data):
    # Normally you would train a model, here just a dummy threshold
    score = sum(sensor_data) / len(sensor_data)
    if score > 0.7:
        return "High chance of failure"
    elif score > 0.4:
        return "Medium risk"
    else:
        return "Low risk"

def calculate_health_score(sensor_data):
    # Calculate a health score (0-100)
    score = 100 - (sum(sensor_data) / len(sensor_data)) * 100
    return round(score, 2)
