import math

# Algorithm to generate cardio section of the workout
def generate_cardio(time, age, weight, fitness):

    # NOTE: These adjustments are not discriminatory - they are based on realistic observations
    # that the advanced and elite levels shown here may exceed that the standard for certain
    # ages and weights. This is just a generality applied to that population

    fitness_level = min(math.floor(fitness / 20), 4)
    if (age > 50):
        fitness_level = min(fitness_level, 2)
    elif (age > 40):
        fitness_level = min(fitness_level, 3)

    if (weight > 200):
        fitness_level = min(fitness_level, 2)
    elif (weight > 175):
        fitness_level = min(fitness_level, 3)

    # Assign a fitness category
    categories = ("Novice", "Beginner", "Intermediate", "Advanced", "Elite")
    fitness_category = categories[fitness_level]

    # Determine distance based on time and fitness class
    # Tuple figures are for (10-min, 15-min, 20-min, 30-min, 40-min, 60-min)
    miles_dictionary = {
        "Novice":       ( 1.00, 1.50, 2.00, 3.00, 4.00, 5.00  ),
        "Beginner":     ( 1.25, 1.75, 2.50, 3.50, 4.50, 6.00  ),
        "Intermediate": ( 1.50, 2.00, 3.00, 4.00, 5.50, 8.00  ),
        "Advanced":     ( 1.75, 2.25, 3.25, 4.50, 6.25, 9.00  ),
        "Elite":        ( 2.00, 2.75, 3.75, 5.00, 7.00, 10.00 )
        }

    time_key = 0
    if time <= 10:
        # There are two possibilities: 6.7 and 10 minutes
        time_key = 0

    elif time <= 15:
        # There are two possibilities: 13.3 and 15 minutes
        time_key = 1

    elif time <= 20:
        time_key = 2

    elif time_key <= 30:
        time_key = 3

    elif time_key <= 40:
        time_key = 4

    else:
        # This can only be 60 minutes
        time_key = 5

    miles = miles_dictionary[fitness_category][time_key]


    # Create output
    exercise = {
        "name": "Running",
        "distance": miles,
        "time": int(time),
        "type": "Cardio",
        "description": 'Aim to cover %.2f miles at your pace' % miles
    }

    return {"time": int(time), "exercises": [exercise] }
