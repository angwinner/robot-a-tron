# robot-a-tron

A simple Django exercise requested by CodeFellows

The specification was "Generate a Django app that allows a you to track info on robots you'd like to build. *  Decide what properties of a robot you want to keep track of, and set up the app to let the user create, edit, update, and destroy (delete) robots, stored in a database."

This application does all of the above, plus:
   * correctly uses composition vs. inheritance - Robots are composed of Parts, but there is a special part called Chassis that inherits from Part and adds the attribute 'weight capacity'
   * adds a weight attribute to all parts
   * validates in Javascript that total robot weight does not exceed chassis weight capacity (this involves overriding the __init__ method of the robot ModelForm to add an onChange event trigger for the validation javascript and, in the edit view, reading in the whole part catalog to get the weights and weight capacities, and the javascipt itself in the edit template)
   * also validates the weight limit in Django by overriding the ModelForm's clean() method, although nothing is done with any resultant ValidationError
