#Name: Zeren Neykov
#Date: Jan 20, 2023
#Program Name: main.py
#Purpose: Create a simple keylogger that allows user to 'listen' to all keys pressed, log all key pressed and view the log in a simple but functional GUI.


# global variable used to stop and start the listener thread. Allows all the program files to have access to the same variable
global end_thread
end_thread = False