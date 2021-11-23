# -*- coding: windows-1252 -*-
maximum_stories = 25
position = int(input("On what floor of the building is your office? "))

while(position > maximum_stories):
    print("You entered: ", position, "There are only" , maximum_stories, "in the building. PLease, try again.")
    position = int(input("On what floor of the building is your office? "))

print("Congratulations! You work on", position, "floor.")