from lift_database import Lift_DB
from lift_standards import adjust_weight, adjust_reps
import math, random

# Options for various workout settings
unit_time_adjustments = (1, 0, 0, 0, -1)

# Algorithm to generate lift section of the workout
def generate_lift(type, time, intensity, age, weight, fitness):

    # Process lift types (Push, Pull, Legs)
    lift_types = []
    if "Push" in type:
        lift_types.append("Push")

    if "Pull" in type:
        lift_types.append("Pull")

    if "Legs" in type:
        lift_types.append("Legs")

    random.shuffle(lift_types)

    # Allocate time among various sections and determine number of exericses
    section_time = time / len(lift_types)
    exercise_counts = { }

    if section_time > 30:
        exercise_counts = { "Compound": 2, "Secondary": 2, "Burner": 1 }

    elif section_time > 20:
        exercise_counts = { "Compound": 1, "Secondary": 2, "Burner": 0 }

    elif section_time > 10:
        exercise_counts = { "Compound": 1, "Secondary": 1, "Burner": 0 }

    else:
        exercise_counts = { "Compound": 1, "Secondary": 0, "Burner": 0 }


    # Create each portion of the lift individually
    selection = []
    obj_Lift_DB = Lift_DB()
    for lift_type in lift_types:
        selection += obj_Lift_DB.query_db(lift_type, "Compound", exercise_counts["Compound"])
        selection += obj_Lift_DB.query_db(lift_type, "Secondary", exercise_counts["Secondary"])
        selection += obj_Lift_DB.query_db(lift_type, "Burner", exercise_counts["Burner"])

    # Adjust reps, weights, unit times & track total time
    total_time = 0
    intensity_level = min(math.floor(intensity / 20), 4)
    for index in range(len(selection)):
        # Time Adjustment
        selection[index]["minutes"] += unit_time_adjustments[intensity_level]

        # Weight Adjustment
        max_weight = selection[index]["bw_ratio"] * weight
        exercise_type = selection[index]["tag"]
        selection[index]["weight"] = adjust_weight(age, fitness, exercise_type, intensity_level, max_weight)

        # Reps Adjustment
        selection[index]["reps"] = adjust_reps(exercise_type, intensity_level, max_weight)

        # Increment total_time counter
        total_time += selection[index]["minutes"] * selection[index]["sets"]

        # Add type tag
        selection[index]["type"] = "Lift"


    # If time remains, add sets to the workout
    for index in range(len(selection)):
        open_time = time - total_time
        if (open_time > 3):
            selection[index]["sets"] += 1
            total_time += selection[index]["minutes"]
        else:
            break


    return {"time": total_time, "exercises": selection}



