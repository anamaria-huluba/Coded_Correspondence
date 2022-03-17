LEARN PYTHON3

Strings - Copelands Corporate Company

1. Copeland’s Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

Let’s start with username_generator. 

Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

2. Now for the temporary password, they want the function to take the input user name and shift all of 
the letters by one to the right, so the last letter of the username ends up as the first letter and so 
forth. 

Start by defining the function password_generator so that it takes one input, username and in it define 
an empty string named password.

Inside password_generator create a for loop that iterates through the indices username by going from 0 
to len(username).

To shift the letters right, at each letter the for loop should add the previous letter to the string 
password.

