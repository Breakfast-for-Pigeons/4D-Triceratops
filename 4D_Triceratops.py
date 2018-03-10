#!/usr/bin/python3
########################################################################
#                          4D Triceratops                              #
########################################################################
# Description:                                                         #
# This program hacks a toy dinosaur. A button is pressed to make the   #
# dinosaur move and grunt.                                              #
# This program is also a demonstration of controlling a motor using    #
# the gpiozero module.                                                 #
# This program is also an example of adding color to text displayed to #
# the screen.                                                          #
#                                                                      #
#                                                                      #
# Author: Paul Ryan                                                    #
#                                                                      #
########################################################################

########################################################################
#                          Import files                                #
########################################################################

from gpiozero import Motor, Button, OutputDevice
from time import sleep
from signal import pause
import pygame
import random
import os, sys

########################################################################
#                           Variables                                  #
########################################################################

triceratops_motor = Motor(16, 13, True)
triceratops_motor_enable = OutputDevice(6)
red_button = Button(9) 
green_button = Button(12) 

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

########################################################################
#                            Functions                                 #
########################################################################
'''
The file_check function checks to see if the necessary files exist.
If they all exist, the program will continue.
If a file is missing, the program will print a message and exit.
'''
def file_check():
	
	dinosaur_facts_flag = 0
	triceratops1_flag = 0
	triceratops2_flag = 0
	triceratops3_flag = 0
	triceratops4_flag = 0
	triceratops5_flag = 0
	triceratops6_flag = 0
	triceratops7_flag = 0
	triceratops8_flag = 0
	
	print("Checking for necessary files:")
	# Check to see if dinosaur_facts.txt file exists
	print("Looking for dinosaur_facts.txt...", end="")
	if os.path.isfile('Files/dinosaur_facts.txt'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if triceratops1.mp3 file exists
	print("Looking for triceratops1.mp3...", end="")
	if os.path.isfile('Sounds/triceratops1.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops1_flag = 1	
	# Check to see if triceratops2.mp3 file exists
	print("Looking for triceratops2.mp3...", end="")
	if os.path.isfile('Sounds/triceratops2.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops2_flag = 1
	# Check to see if triceratops3.mp3 file exists
	print("Looking for triceratops3.mp3...", end="")
	if os.path.isfile('Sounds/triceratops3.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops3_flag = 1
	# Check to see if triceratops4.mp3 file exists
	print("Looking for triceratops4.mp3...", end="")
	if os.path.isfile('Sounds/triceratops4.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops4_flag = 1
	# Check to see if triceratops5.mp3 file exists
	print("Looking for triceratops5.mp3...", end="")
	if os.path.isfile('Sounds/triceratops5.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops1_flag = 1	
	# Check to see if triceratops6.mp3 file exists
	print("Looking for triceratops6.mp3...", end="")
	if os.path.isfile('Sounds/triceratops6.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops2_flag = 1
	# Check to see if triceratops7.mp3 file exists
	print("Looking for triceratops7.mp3...", end="")
	if os.path.isfile('Sounds/triceratops7.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops3_flag = 1
	# Check to see if triceratops8.mp3 file exists
	print("Looking for triceratops8.mp3...", end="")
	if os.path.isfile('Sounds/triceratops8.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		triceratops4_flag = 1
	
	
	# If there are no missing files, return to the main function
	# Otherwise print out messages and exit the program
	if dinosaur_facts_flag == 0  and triceratops1_flag == 0 and triceratops2_flag == 0 and triceratops3_flag == 0 and triceratops4_flag == 0 and \
	   triceratops5_flag == 0 and triceratops6_flag == 0 and triceratops7_flag == 0 and triceratops8_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mCheck to make sure that the dinosaur_facts.txt file exists in the 'Files' folder.")
		if triceratops1_flag == 1: 	
			print("\033[1;31;40mCheck to make sure that the triceratops1.mp3 file exists in the 'Sounds' folder.")
		if triceratops2_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops2.mp3 file exists in the 'Sounds' folder.") 
		if triceratops3_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops3.mp3 file exists in the 'Sounds' folder.")
		if triceratops4_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops4.mp3 file exists in the 'Sounds' folder.")
		if triceratops5_flag == 1: 	
			print("\033[1;31;40mCheck to make sure that the triceratops5.mp3 file exists in the 'Sounds' folder.")
		if triceratops6_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops6.mp3 file exists in the 'Sounds' folder.") 
		if triceratops7_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops7.mp3 file exists in the 'Sounds' folder.")
		if triceratops8_flag == 1:
			print("\033[1;31;40mCheck to make sure that the triceratops8.mp3 file exists in the 'Sounds' folder.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()

'''
The access_file_check function checks to see if the user has permission
to read the necessary files. If so, the program will continue. If not, 
messages are printed out to the screen and the program will exit.
'''
def access_file_check():
	
	dinosaur_facts_flag = 0
	triceratops1_flag = 0
	triceratops2_flag = 0
	triceratops3_flag = 0
	triceratops4_flag = 0
	triceratops5_flag = 0
	triceratops6_flag = 0
	triceratops7_flag = 0
	triceratops8_flag = 0
	
	print("Checking to see if user has permission to read the necessary files:")
	# Check to see if user has read access to dinosaur_facts.txt
	print("Does user have read permissions for dinosaur_facts.txt?...", end="")
	if os.access('Files/dinosaur_facts.txt', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if user has read access to  triceratops1.mp3
	print("Does user have read permissions for triceratops1.mp3?...", end="")
	if os.access('Sounds/triceratops1.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops1_flag = 1
	# Check to see if user has read access to  triceratops2.mp3
	print("Does user have read permissions for triceratops2.mp3?...", end="")
	if os.access('Sounds/triceratops2.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops2_flag = 1
	# Check to see if user has read access to  triceratops3.mp3
	print("Does user have read permissions for triceratops3.mp3?...", end="")
	if os.access('Sounds/triceratops3.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops2_flag = 1
	# Check to see if user has read access to  triceratops4.mp3
	print("Does user have read permissions for triceratops4.mp3?...", end="")
	if os.access('Sounds/triceratops4.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops4_flag = 1
	# Check to see if user has read access to  triceratops5.mp3
	print("Does user have read permissions for triceratops5.mp3?...", end="")
	if os.access('Sounds/triceratops5.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops5_flag = 1
	# Check to see if user has read access to  triceratops6.mp3
	print("Does user have read permissions for triceratops6.mp3?...", end="")
	if os.access('Sounds/triceratops6.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops6_flag = 1
	# Check to see if user has read access to  triceratops7.mp3
	print("Does user have read permissions for triceratops7.mp3?...", end="")
	if os.access('Sounds/triceratops7.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops7_flag = 1
	# Check to see if user has read access to  triceratops8.mp3
	print("Does user have read permissions for triceratops8.mp3?...", end="")
	if os.access('Sounds/triceratops8.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		triceratops8_flag = 1
	
	if dinosaur_facts_flag == 0  and triceratops1_flag == 0 and triceratops2_flag == 0 and triceratops3_flag == 0 and triceratops4_flag == 0 and \
	   triceratops5_flag == 0 and triceratops6_flag == 0 and triceratops7_flag == 0 and triceratops8_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Files' folder and the dinosaur_facts.txt file.")
		if triceratops1_flag == 1: 	
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops1.mp3' file.")
		if triceratops2_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops2.mp3' file.") 
		if triceratops3_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops3.mp3' file.")
		if triceratops4_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops4.mp3' file.")
		if triceratops5_flag == 1: 	
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops5.mp3' file.")
		if triceratops6_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops6.mp3' file.") 
		if triceratops7_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops7.mp3' file.")
		if triceratops8_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'triceratops8.mp3' file.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()

'''
The read_file function will read the dinosaur facts file and each 
line of the file will be an element in the fun_facts list. It will then
return the dino_facts list to the main function.
If the program is unable to read the file, it will display an error
message and then exit the program.
If the dino_facts file is empty, an error message will be displayed 
and the program will exit.
'''
def read_file(file_name):
	print("\033[1;37;40mReading the dinosaur_facts.txt file...", end="")
	f = open(file_name, "r")     # open the file as read-only
	dino_facts = f.readlines()
	f.close()
	print("\033[1;32;40mdone\033[1;37;40m!")

	return dino_facts
	
'''
This empty_file_check function checks to see if the file is empty. If it
is, the program will print a message to the screen. If not, the program
will continue.
'''
def empty_file_check(file_name):		
	print("\033[1;37;40mIs the dinosaur_facts.txt file empty?...", end="")
	if file_name == []:
		print("\033[1;31;40mYes\033[1;37;40m!")
		print("\033[1;31;40mThe dinosaur.txt file is empty. The program won't work.")
		release_gpio_pins()
		exit()
	else:
		print("\033[1;32;40mNo\033[1;37;40m!")
		
'''
The print_header function will print out the program header to the 
screen.
'''
def print_header():
	print("\033[1;32;40m======================================================================")
	print("\033[1;32;40m   _  _   ____    _____     _                    _                    ")
	print("\033[1;32;40m  | || | |  _ \  |_   _| __(_) ___ ___ _ __ __ _| |_ ___  _ __  ___   ")
	print("\033[1;32;40m  | || |_| | | |   | || '__| |/ __/ _ \ '__/ _` | __/ _ \| '_ \/ __|  ")
	print("\033[1;32;40m  |__   _| |_| |   | || |  | | (_|  __/ | | (_| | || (_) | |_) \__ \  ")
	print("\033[1;32;40m     |_| |____/    |_||_|  |_|\___\___|_|  \__,_|\__\___/| .__/|___/  ")
	print("\033[1;32;40m                                                         |_|          ")
	print("\033[1;32;40m======================================================================\n")                                                      

'''
The get_grunt function will randomly select one of the Triceratops 
grunt sound files and return it and its file length to the main 
function.
'''
def get_grunt():
	
	grunt1 = "Sounds/triceratops1.mp3"
	grunt2 = "Sounds/triceratops2.mp3"
	grunt3 = "Sounds/triceratops3.mp3"
	grunt4 = "Sounds/triceratops4.mp3"
	grunt5 = "Sounds/triceratops5.mp3"
	grunt6 = "Sounds/triceratops6.mp3"
	grunt7 = "Sounds/triceratops7.mp3"
	grunt8 = "Sounds/triceratops8.mp3"

	grunt1_length = 5      # lenth of file in seconds
	grunt2_length = 4      # lenth of file in seconds
	grunt3_length = 4      # lenth of file in seconds
	grunt4_length = 4      # lenth of file in seconds
	grunt5_length = 5      # lenth of file in seconds
	grunt6_length = 3      # lenth of file in seconds
	grunt7_length = 2      # lenth of file in seconds
	grunt8_length = 3      # lenth of file in seconds
	
	grunts = [grunt1, grunt2, grunt3, grunt4, grunt5, grunt6, grunt7, grunt8]
	
	grunt = random.choice(grunts)   # Selects random sound file
	
	if grunt == grunt1:
		return grunt, grunt1_length
	elif grunt == grunt2:
		return grunt, grunt2_length
	elif grunt == grunt3:
		return grunt, grunt3_length
	if grunt == grunt4:
		return grunt, grunt4_length
	elif grunt == grunt5:
		return grunt, grunt5_length
	elif grunt == grunt6:
		return grunt, grunt6_length
	elif grunt == grunt7:
		return grunt, grunt7_length
	else:
		return grunt, grunt8_length

'''
The activate_triceratops funciton takes 2 inputs: grunt and grunt_length. 
This function will play the sound file and then activate the motor for 
the duration of the sound file. 
'''
def activate_triceratops(grunt, grunt_length):
	try:
		triceratops_motor.value = 0.6      # Controls the motor speed
	except ValueError:
		print("\033[1;31;40mBad value specified for triceratops_motor. Enter a value between 0 and 1.\n")
		release_gpio_pins()
		exit()
	pygame.mixer.music.load(grunt)     # Loads the sound file
	triceratops_motor_enable.on()      # Starts the motor
	pygame.mixer.music.play()          # Plays the sound file
	sleep(grunt_length)                # Length of sound file in seconds
	triceratops_motor_enable.off()     # Stops the motor

'''
The prompt_user_for_input function prompts a user to push a button.
'''
def prompt_user_for_input():
	print("\033[1;37;40mPush the \033[1;32;40mgreen button\033[1;37;40m to activate the \033[1;32;40mTriceratops\033[1;37;40m.")
	print("\033[1;37;40mPush the \033[1;31;40mred button \033[1;37;40mor press Ctrl-C to \033[1;31;40mstop \033[1;37;40mthe program.\n")

'''
The release_gpio_pins function realeases the gpio pins.
'''
def release_gpio_pins():
	triceratops_motor.close()
	triceratops_motor_enable.close()
	red_button.close()
	green_button.close()

'''
This is the main fucntion. It will wait until one of two buttons is 
pressed. One button will start the program and the other button will
stop the program. Pressing Ctrl-C will also stop the program.
'''
def main():
	try:
		# Check to see that the necessary files exist
		file_check()
		# Check to see if files are accessible
		access_file_check()
		# Read the dinosaur_facts.txt file to populate the dino_facts list.
		dino_facts = read_file("Files/dinosaur_facts.txt")
		# Check to see if the file is empty
		empty_file_check(dino_facts)
		# Acknowledge that prelimiary checks are complete
		print("\033[1;37;40mPrelimiary checks are complete. Starting program...\n")
		# Display program header
		print_header()
		# Pre-load the first sound file
		grunt, grunt_length = get_grunt()
		# Prompt the user to press a button
		prompt_user_for_input()
		
		while True:
			
			if green_button.is_pressed:
				# Print out a random dinosaur fun fact
				print("\033[1;34;40mDINOSAUR FUN FACT:")
				print(random.choice(dino_facts))
				# Move the T. rex for the duration of the sound file
				activate_triceratops(grunt, grunt_length)
				# Prompt the user to press a button
				prompt_user_for_input()
				# Load the next sound file
				grunt, grunt_length = get_grunt()
				
			if red_button.is_pressed:
				print("Exiting program.\n")
				release_gpio_pins()
				exit()
				
	except KeyboardInterrupt:
		release_gpio_pins()
		print("Exiting program.\n")
		
if __name__ == '__main__':
	main()
