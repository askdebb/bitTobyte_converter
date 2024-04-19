# bitTobyte_converter
converting bits to bytes using python

# yes or no description 
This part of the game allows users to enter their names which is assigned the variable "playername".

The If loop is used to create two conditions:
1. If the user name is equal to blank or space the game assigns the name "No-name" the the user.
2. Else if user enters a name it is assigned to the variable "structureplatername"

 Note: 
Whether the playername is in capital letters or capital mixed with lower case letters the program changes everthing to lower case using the command ".lower()" and prints out user's name with a welcome note. 

#  user affirms if he or she wants to continue with the game
The "Yes" or "No" / "n" /"N"/ "y"/ "Y" inputs are all acceptable inputs. The ".lower()" changes everything in the userReadiness variable to lower case. 

# Ending or continuing the game
The use of the While loop allows for two additional conditions.
1. If the variable userReadyLowerCase is equal to
 "no" / "n" the user ends the game with this input, but the program prints a promt expressing sadness and encouraging user to return soon. The use of "break" promts the program to end. 
2. Else if the userReadinessLowerCase input is either "yes" / "y" the game affirms and encourages the user to continue. 
