import math

# Convert fitness level to a category
def determine_fitness(level):
    return min(math.floor(level / 20), 4)


# Convert age to 1 of 5 categories
def determine_age(age):
    if (age < 18):
        return 0

    elif (age < 35):
        return 1

    elif (age < 50):
        return 2

    elif (age < 60):
        return 3

    elif (age < 80):
        return 4


# Strength adjustments: row = fitness, column = age
strength_adjustments = (
    ( 0.85, 0.85, 0.80, 0.75, 0.65 ),
    ( 0.90, 0.90, 0.85, 0.80, 0.70 ),
    ( 0.95, 0.95, 0.90, 0.85, 0.75 ),
    ( 1.00, 1.00, 0.95, 0.90, 0.80 ),
    ( 1.05, 1.05, 1.00, 0.95, 0.85 )
)


# Reps and weight adjustments for compound exercises
compound_intensity_map = (
    {"Reps": 8, "Percent": 0.6},
    {"Reps": 7, "Percent": 0.7},
    {"Reps": 6, "Percent": 0.8},
    {"Reps": 4, "Percent": 0.85},
    {"Reps": 3, "Percent": 0.9}
)


# Reps and weight adjustments for secondary exercises
secondary_intensity_map = (
    {"Reps": 6, "Percent": 0.8},
    {"Reps": 8, "Percent": 0.8},
    {"Reps": 10, "Percent": 0.8},
    {"Reps": 12, "Percent": 0.75},
    {"Reps": 15, "Percent": 0.7}
)


# Reps and weight adjustments for burner exercises
burner_intensity_map = (
    {"Reps": 15, "Percent": 0.4},
    {"Reps": 15, "Percent": 0.4},
    {"Reps": 20, "Percent": 0.35},
    {"Reps": 25, "Percent": 0.3},
    {"Reps": 30, "Percent": 0.3}
)


# Adjust the suggested exercise weight based on common lifting standards, intensity, age, and fitness
def adjust_weight(age, fitness, type, intensity_level, max_weight):

    fitness_category = determine_fitness(fitness)
    age_category = determine_age(age)

    intensity_map = {
        "Compound": compound_intensity_map,
        "Secondary": secondary_intensity_map,
        "Burner": burner_intensity_map
    }

    adjusted_max = max_weight * strength_adjustments[fitness_category][age_category]
    weight_output = intensity_map[type][intensity_level]["Percent"] * adjusted_max
    return int(weight_output / 5.0) * 5


# Adjust the suggested exercise reps based on common lifting standards, intensity, age, and fitness
def adjust_reps(type, intensity_level, max_weight):

    intensity_map = {
        "Compound": compound_intensity_map,
        "Secondary": secondary_intensity_map,
        "Burner": burner_intensity_map
    }

    return intensity_map[type][intensity_level]["Reps"]



