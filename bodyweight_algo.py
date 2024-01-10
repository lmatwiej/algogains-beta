import math
from bodyweight_database import Bodyweight_DB

# Algorithm to generate bodyweight section of the workout
def generate_bodyweight(time, intensity, fitness):

    # Convert fitness to appropriate category
    category_index = min(math.floor(fitness / 33), 2)
    categories = ("Beginner", "Intermediate", "Advanced")
    fitness_category = categories[category_index]


    # Allow one exercise for each 10 minute period
    count = int(time / 10)


    # Pull exercise selection from database
    obj_Bodyweight_DB = Bodyweight_DB()
    workout = obj_Bodyweight_DB.query_db(fitness_category, count)

    total_time = workout["time"]
    selection = workout["exercises"]


    # Adjust unit times based on intensity
    unit_time_adjustments = (1, 0, 0, 0, -1)
    intensity_level = min(math.floor(intensity / 20), 4)

    for index in range(len(selection)):
        selection[index]["minutes"] += unit_time_adjustments[intensity_level]
        total_time += unit_time_adjustments[intensity_level]

        # Add type tage
        selection[index]["type"] = "Bodyweight"


    # If time remains, add sets to the workout
    for index in range(len(selection)):
        open_time = time - total_time
        if (open_time > 3):
            selection[index]["sets"] += 1
            total_time += selection[index]["minutes"]
        else:
            break

    # If time still remains, proceed with another iteration of set increments
    for index in range(len(selection)):
        open_time = time - total_time
        if (open_time > 3):
            selection[index]["sets"] += 1
            total_time += selection[index]["minutes"]
        else:
            break


    return {"time": total_time, "exercises": selection}
