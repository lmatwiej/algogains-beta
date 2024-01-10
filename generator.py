from lift_algo import generate_lift
from bodyweight_algo import generate_bodyweight
from cardio_algo import generate_cardio

class WorkoutGenerator:
    '''This is a top-level class that consolidates multiple workout sections into one output'''

    # Algorithm that creates tailored exercise list
    @staticmethod
    def generate(type, time, intensity, age, weight, fitness):

        # Final output will be workout array
        workout = {'time': 0, "exercises": []}

        # Initialize key workout settings
        query_lift = False
        if (type.count("Push") + type.count("Pull") + type.count("Legs")) > 0:
            query_lift = True

        query_bodyweight = False
        if "Bodyweight" in type:
            query_bodyweight = True

        query_cardio = False
        if "Cardio" in type:
            query_cardio = True

        minutes_settings = {"Long": 60, "Medium": 40, "Short": 20}
        total_sections = query_lift + query_bodyweight + query_cardio
        total_minutes = minutes_settings[time]
        section_length = total_minutes / total_sections

        # Build workout using special methods for each type
        if query_lift:
            lift = generate_lift(type, section_length, intensity, age, weight, fitness)
            workout['time'] += lift['time']
            workout['exercises'] += lift['exercises']

        if query_bodyweight:
            bodyweight = generate_bodyweight(section_length, intensity, fitness)
            workout['time'] += bodyweight['time']
            workout['exercises'] += bodyweight['exercises']

        if query_cardio:
            cardio = generate_cardio(section_length, age, weight, fitness)
            workout['time'] += cardio['time']
            workout['exercises'] += cardio['exercises']


        # Process workout into final output
        num_exercises = len(workout['exercises'])
        output_list = []

        for index in range(num_exercises):

            if workout['exercises'][index]["type"] == "Lift":

                # Output variables
                sets = workout['exercises'][index]["sets"]
                reps = workout['exercises'][index]["reps"]
                weight = workout['exercises'][index]["weight"]
                time = sets * workout['exercises'][index]["minutes"]

                # Append to output
                output_list.append({
                        "type": "Lift",
                        "name": workout['exercises'][index]["name"],
                        "description": f'{sets} sets x {reps} reps (estimated weight: {weight}lbs)',
                        "time": f'~ {time} mins.'
                    })

            elif workout['exercises'][index]["type"] == "Bodyweight":

                # Output variables
                sets = workout['exercises'][index]["sets"]
                time = sets * workout['exercises'][index]["minutes"]

                # Append to output
                output_list.append({
                        "type": "Bodyweight",
                        "name": workout['exercises'][index]["name"],
                        "description": f'{sets} sets - challenge yourself on reps',
                        "time": f'~ {time} mins.'
                    })

            elif workout['exercises'][index]["type"] == "Cardio":

                # Output variables
                time = workout['exercises'][index]["time"]

                # Append to output
                output_list.append({
                        "type": "Cardio",
                        "name": workout['exercises'][index]["name"],
                        "description": workout['exercises'][index]["description"],
                        "time": f'~ {time} mins.'
                    })

        # Return final workout with total time
        workout['exercises'] = output_list
        return workout
