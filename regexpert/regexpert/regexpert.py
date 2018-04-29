# Regexpert Game
#
# Requires python3!
#
# author: swolewizard
#=====================================
import os

usr_data = open('usr_data', 'r+')
usr_name = usr_data.readline()

# TODO: why you no work
if usr_name.split(' ')[1] == ' ':
    usr_name.split(' ')[1] = input('Enter your name: ')
    

print('Welcome to regexpert, officer', usr_name.split(' ')[1], '.')

# TODO: New game resets the usr_data file
print(' Some cool game art lol ')
print(' New Game')
print('Select the level that you are on:')
print(' > Continue Last Save ')
print(' > Level 0: ')
print(' > Level 1: ')
print(' > Level 2: ')

usr_data.close()
#os.system("cat level_0/intro")

