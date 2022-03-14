LEARN INTERMEDIATE PYTHON 3

The Great Robot Race

The brushless motors are roaring, and the race is about to begin! In this project, we will be using some of the advanced containers in Python to command, track, and score simple robots which are trying to traverse different mazes. Your job will be to fill in the missing code from the robot_race.py file. A lot of background code has been provided in the robot_race_functions.py file which we will be using, but the primary focus of this project is to use advanced collections in a meaningful way. Click start to begin!

Reviewing the Code

1. Let’s start by taking a look at what the mazes files look like, 

This one is maze_data_1.csv:

#,#,#,#,#,#,#,#,#,#
#,_,_,_,#,_,_,_,$,#
#,_,A,_,_,_,#,_,_,#
#,B,_,_,#,_,#,_,_,#
#,_,C,_,#,_,_,_,_,#
#,#,#,#,#,#,#,#,#,#

The mazes are csv files which contain different characters that represent different objects in the robot race. Any letter represents a robot, the # character represents a wall which the robots can collide with, and the $ is the goal which the robots are racing towards. Robots can traverse into any empty space (shown by an _) and they can even occupy the same space as another robot (shown as a +). At any point during this project, feel free to create your own csv maze and use it in the code instead of the example ones.

2. Now take a look at the robot_race.py file. After importing the required modules and classes, there are some values to take note of at the top of the file. The maze_file_name can be changed to any csv file which follows the maze structure (as defined earlier). The seconds_between_turns value will determine how much time passes between updating the visualized maze in the console (which we will be coding during the project). Finally, the max_turns value determines how many turns the robots have before the race ends. The race will end if the max turns are reached or if all of the robots reach the goal.

The robots will be scored based on the amount of moves they make plus the number of collisions they have with the walls. The robot with the lowest score wins.

3. Throughout this project, run the code in the terminal by using the command: python3 robot_race.py


