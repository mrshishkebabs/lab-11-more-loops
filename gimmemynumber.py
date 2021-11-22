# -*- coding: windows-1252 -*-
userstring = input("Gimmy a number greater than 100 plz... ")
usernum = int(userstring)

while usernum <= 100:
	print(str(usernum) + " This number is less than and equal to 100, dummy. Try again… I’ve got all day") 
	userstring = input("Gimmy a number greater than 100 ple... ")
	usernum = int(userstring)

print(str(usernum) + " is greater than 100! Good work.")