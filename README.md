**Project Overview**

Algo Gains is a Python algorithm that generates exercise recommendations for users based on their preferences and fitness levels.
You can test the algorithm by visiting [elevathletics.com/algogains](https://www.elevathletics.com/algogains) or making a POST request to http://lukaszjmat.pythonanywhere.com/algogains.

If you choose to make the POST request yourself, please include the following variables in the JSON body:

  - **"type"**: string array containing 1 or more of these values: "Push", "Pull", "Legs", "Bodyweight", "Cardio"
  - **"time"**: "Long", "Medium" or "Short"
  - **"intensity"**: integer between 0 and 100 (inclusive)
  - **"fitness"**: integer between 0 and 100 (inclusive)
  - **"age"**: integer
  - **"weight"**: integer

**Algorithm Description**

The algorithm begins by parsing the inputs to determine key workout settings. The "time" input (Long, Medium, or Short) determines total workout duration (60, 40, or 20 mins), and the "type" input determines which subsections (Lift, Bodyweight, or Cardio) will comprise the entire workout. Total workout duration is distributed evenly among subsections.

If the "type" array includes "Push", "Pull", and/or "Legs", the algorithm will proceed to create a Lift subsection that pulls exercises from a lift database at random and adjusts sets, reps, and weight as needed to match the user's fitness profile, desired intensity, and time constraints.

If the "type" array includes "Bodyweight", the algorithm similarly creates a Bodyweight subsection. As with the Lift, the algorithm will pull exercises from a bodyweight database at random and adjust exercise selection and sets according to user preferences.

Finally, if the "type" array includes "Cardio", the algorithm will create a Cardio section that consists of a targeted distance run intended to meet the user's desired intensity and allotted time. As with the other sections, this calculation is based on fitness levels, age, and weight.

All the individual subsections are concatenated into a single list that is returned as part of a dict object containing total workout minutes and this exercise list.

**Running the Code**

This API currently runs on a Flask application on a pythonanywhere server. To run this code for yourself, you will need to download Flask and run "flask --app flask_app run".

**Please note that I have a separate version of this project that runs on a Django server and utilizes a MySQL database. Please reach out if you are interested in that version, as it is currently not made available on GitHub.**
