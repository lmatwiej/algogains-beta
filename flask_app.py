from flask import Flask
from flask import request
from flask_cors import CORS

from generator import WorkoutGenerator


app = Flask(__name__)
CORS(app)

## Algo Gains vBeta workout generator algorithm
@app.post('/algogains')
def generate_workout():

    # Convert body to dictionary
    request_data = request.get_json()


    # Parse request data
    type = request_data['type']
    time = request_data['time']
    intensity = int(request_data['intensity'])
    age = int(request_data['age'])
    weight = int(request_data['weight'])
    fitness = int(request_data['fitness'])


    # Validate inputs
    if (intensity < 0 or intensity > 100):
        return ("Intensity out of range", 400)

    if (fitness < 0 or fitness > 100):
        return ("Fitness out of range", 400)

    if (age < 14 or age > 120):
        return ("Age out of range", 400)

    if (weight < 50 or weight > 300):
        return ("Weight out of range", 400)

    if not (time == "Long" or time == "Medium" or time == "Short"):
        return ("Invalid time value", 400)


    # Run the algorithm
    obj_WorkoutGenerator = WorkoutGenerator()
    workout = obj_WorkoutGenerator.generate(type, time, intensity, age, weight, fitness)

    return workout
