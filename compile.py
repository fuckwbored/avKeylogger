import os
from platform import platform
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

def winrun():
	win = '''pyinstaller --clean --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile --noconsole main.py&del /s /q /f main.spec&rmdir /s /q __pycache__&rmdir /s /q build&:cmd&echo [+] Ready! Result in folder dist&pause null&
	'''
	os.system(win)

def linuxrun():
	linux = '''
	pyinstaller --clean --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.sapi5 --onefile --noconsole main.py

	rm -rf main.spec
	rm -rf __pycache__
	rm -rf build

	echo [+] Ready! Result in folder dist
	'''
	os.system(linux)

print(Fore.RED + """

 █████╗ ██╗   ██╗██╗  ██╗███████╗██╗   ██╗
██╔══██╗██║   ██║██║ ██╔╝██╔════╝╚██╗ ██╔╝
███████║██║   ██║█████╔╝ █████╗   ╚████╔╝ 
██╔══██║╚██╗ ██╔╝██╔═██╗ ██╔══╝    ╚██╔╝  
██║  ██║ ╚████╔╝ ██║  ██╗███████╗   ██║   
╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   
""")
print("""Version: 1.0

Continiue?[y/n]""")
print(Fore.GREEN + "(.exe file will be in folder dist)")

user_input = input(">>> ")
if user_input == 'n':
	os.system('exit')
else: 
	plat = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
	if plat == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
		winrun()
	else:
		linuxrun()