import random

class Bodyweight_DB:
    '''Contains database of bodyweight movements and processes queries'''

    # Bodyweight database
    database = {
        "Beginner": [
            # Push Movements
            { "name": "Regular Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Knee Push Up",       "sets": 2, "minutes": 2 },
            { "name": "Incline Push Up",    "sets": 2, "minutes": 2 },

            # Pull Movements
            { "name": "Negative Pull Ups",  "sets": 2, "minutes": 2 },
            { "name": "Regular Pull Ups",   "sets": 2, "minutes": 2 },
            { "name": "Negative Chin Ups",  "sets": 2, "minutes": 2 },
            { "name": "Regular Chin Ups",   "sets": 2, "minutes": 2 },

            # Leg Movements
            { "name": "Squat",              "sets": 2, "minutes": 2 },
            { "name": "Jumping Jacks",      "sets": 2, "minutes": 2 },
            { "name": "High Knees",         "sets": 2, "minutes": 2 },
            { "name": "Good Mornings",      "sets": 2, "minutes": 2 },
        ],
        "Intermediate": [
            # Push Movements
            { "name": "Regular Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Diamond Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Incline Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Decline Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Dips",               "sets": 2, "minutes": 2 },

            # Pull Movements
            { "name": "Regular Pull Ups",   "sets": 2, "minutes": 2 },
            { "name": "Regular Chin Ups",   "sets": 2, "minutes": 2 },

            # Leg Movements
            { "name": "Squat",              "sets": 2, "minutes": 2 },
            { "name": "Squat Jumps",        "sets": 2, "minutes": 2 },
            { "name": "Split Squats",       "sets": 2, "minutes": 2 },
            { "name": "Split Squat Jumps",  "sets": 2, "minutes": 2 },
            { "name": "Lunges",             "sets": 2, "minutes": 2 },
            { "name": "Reverse Lunges",     "sets": 2, "minutes": 2 },

        ],
        "Advanced": [
            # Push Movements
            { "name": "Regular Push Up",    "sets": 2, "minutes": 2 },
            { "name": "Diamond Push Up",    "sets": 2, "minutes": 2  },
            { "name": "Incline Push Up",    "sets": 2, "minutes": 2  },
            { "name": "Decline Push Up",    "sets": 2, "minutes": 2  },
            { "name": "Dips",               "sets": 2, "minutes": 2  },
            { "name": "Clap Push Up",       "sets": 2, "minutes": 2  },
            { "name": "One Arm Push Up",    "sets": 2, "minutes": 2  },
            { "name": "Burpees",            "sets": 2, "minutes": 2  },

            # Pull Movements
            { "name": "Regular Pull Ups",   "sets": 2, "minutes": 2 },
            { "name": "Regular Chin Ups",   "sets": 2, "minutes": 2 },
            { "name": "Pull Up & Leg Raise","sets": 2, "minutes": 2 },

            # Leg Movements
            { "name": "Squat",              "sets": 2, "minutes": 2 },
            { "name": "Squat Jumps",        "sets": 2, "minutes": 2 },
            { "name": "Split Squats",       "sets": 2, "minutes": 2 },
            { "name": "Split Squat Jumps",  "sets": 2, "minutes": 2 },
            { "name": "Lunges",             "sets": 2, "minutes": 2 },
            { "name": "Reverse Lunges",     "sets": 2, "minutes": 2 },
            { "name": "Nordic Hamstrings",  "sets": 2, "minutes": 2 },
            { "name": "Box Jumps",          "sets": 2, "minutes": 2 },
            { "name": "Broad Jumps",        "sets": 2, "minutes": 2 },
            { "name": "Pistol Squat",       "sets": 2, "minutes": 2 },
            { "name": "Sprint Variations",  "sets": 2, "minutes": 2 },
        ],
    }

    # Query that returns exercises from database
    def query_db(self, intensity_level, count):

        # Validate arguments
        if intensity_level not in ("Beginner", "Intermediate", "Advanced"):
            return []

        if count <= 0:
            return []


        exercise_set = self.database[intensity_level]
        num_exercises = len(exercise_set)
        count = min(count, num_exercises)

        # Pull right number of exercises at random
        selection = []
        time = 0

        for index in random.sample(range(num_exercises), count):
            selection.append(exercise_set[index])
            time += exercise_set[index]["minutes"]

        return {"time": time, "exercises": selection}

