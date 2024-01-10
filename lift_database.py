import random

class Lift_DB:
    '''Contains database of lifts and processes queries'''

    # Lifting database
    database = {
        "Push": {
            "Compound":     [   { "tag": "Compound", "name": "Military Press",   "sets": 2,  "bw_ratio": 0.7, "minutes": 4  },
                                { "tag": "Compound", "name": "Incline Bench",    "sets": 2,  "bw_ratio": 0.7, "minutes": 4  },
                                { "tag": "Compound", "name": "Flat Bench",       "sets": 2,  "bw_ratio": 0.8, "minutes": 4  },
                            ],
            "Secondary":    [   { "tag": "Secondary", "name": "Skullcrushers",    "sets": 2, "bw_ratio": 0.4, "minutes": 3  },
                                { "tag": "Secondary", "name": "Flat DB Press",    "sets": 2, "bw_ratio": 0.6, "minutes": 3  },
                                { "tag": "Secondary", "name": "Incline DB Press", "sets": 2, "bw_ratio": 0.5, "minutes": 3  },
                                { "tag": "Secondary", "name": "Decline DB Press", "sets": 2, "bw_ratio": 0.5, "minutes": 3  },
                                { "tag": "Secondary", "name": "DB Shoulder Press", "sets": 2, "bw_ratio": 0.5, "minutes": 3  },
                                { "tag": "Secondary", "name": "Weighted Dips",    "sets": 2, "bw_ratio": 0.2, "minutes": 3  },
                            ],
            "Burner":       [   { "tag": "Burner", "name": "Cable Flyes",      "sets": 2, "bw_ratio": 0.2, "minutes": 2  },
                                { "tag": "Burner", "name": "Lateral Raises",   "sets": 2, "bw_ratio": 0.2, "minutes": 2  },
                            ],
        },
        "Pull": {
            "Compound":     [   { "tag": "Compound", "name": "Dumbbell Rows",    "sets": 2, "bw_ratio": 0.8, "minutes": 4  },
                                { "tag": "Compound", "name": "Weighted Pullups", "sets": 2, "bw_ratio": 0.1, "minutes": 4  },
                                { "tag": "Compound", "name": "Barbell Row",      "sets": 2, "bw_ratio": 0.7, "minutes": 4  },
                            ],
            "Secondary":    [   { "tag": "Secondary", "name": "Cable Rows",       "sets": 2, "bw_ratio": 0.7, "minutes": 3  },
                                { "tag": "Secondary", "name": "Lat Pulldown",     "sets": 2, "bw_ratio": 0.7, "minutes": 3  },
                                { "tag": "Secondary", "name": "Face Pulls",       "sets": 2, "bw_ratio": 0.3, "minutes": 3  },
                            ],
            "Burner":       [   { "tag": "Burner", "name": "Reverse Fly",      "sets": 2, "bw_ratio": 0.3, "minutes": 2  },
                                { "tag": "Burner", "name": "Curls",            "sets": 2, "bw_ratio": 0.3, "minutes": 2  },
                            ],
        },
        "Legs": {
            "Compound":     [   { "tag": "Compound", "name": "Romanian DL",      "sets": 2, "bw_ratio": 1.0, "minutes": 4  },
                                { "tag": "Compound", "name": "Regular DL",       "sets": 2, "bw_ratio": 1.5, "minutes": 4  },
                                { "tag": "Compound", "name": "Front Squat",      "sets": 2, "bw_ratio": 1.0, "minutes": 4  },
                                { "tag": "Compound", "name": "Back Squat",       "sets": 2, "bw_ratio": 1.5, "minutes": 4  },
                                { "tag": "Compound", "name": "Leg Press",        "sets": 2, "bw_ratio": 1.5, "minutes": 4  },
                            ],
            "Secondary":    [   { "tag": "Secondary", "name": "Calf Raises",      "sets": 2, "bw_ratio": 0.4, "minutes": 3  },
                                { "tag": "Secondary", "name": "Seated Leg Curls", "sets": 2, "bw_ratio": 0.4, "minutes": 3  },
                                { "tag": "Secondary", "name": "Leg Curls",        "sets": 2, "bw_ratio": 0.4, "minutes": 3  },
                                { "tag": "Secondary", "name": "Split Squats",     "sets": 2, "bw_ratio": 0.7, "minutes": 3 },
                            ],
            "Burner":       [   { "tag": "Burner", "name": "Lunges",           "sets": 2, "bw_ratio": 0.5, "minutes": 2 },
                                { "tag": "Burner", "name": "Leg Extensions",   "sets": 2, "bw_ratio": 0.5, "minutes": 2 },
                                { "tag": "Burner", "name": "Goblet Squats",    "sets": 2, "bw_ratio": 0.3, "minutes": 2 },
                            ]
        },
    }

    # Query that returns exercises from database
    def query_db(self, lift_type, exercise_type, count):

        # Validate arguments
        if lift_type not in self.database.keys():
            return []

        if exercise_type not in ("Compound", "Secondary", "Burner"):
            return []

        if count <= 0:
            return []


        exercise_set = self.database[lift_type][exercise_type]
        num_exercises = len(exercise_set)
        count = min(count, num_exercises)

        # Pull right number of exercises at random
        selection = []

        for index in random.sample(range(num_exercises), count):
            selection.append(exercise_set[index])

        return selection
