#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import ctypes 

########################################################################

def cmd(commando):
	subprocess.run(commando, shell=True)

def chgname(): #CAMBIAR NOMBRE PC
	n = caja1.get()
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" /v ComputerName /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v ComputerName /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "NV Hostname" /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v Hostname /t REG_SZ /d '+n+' /f')

def activaradm(): #ACTIVAR ADMINISTRADOR
	cmd("net user administrador /active:yes")
	cmd("net user administrador Pss1166")

def activarw(): #ACTIVA WINDOWS
	cmd('slmgr -ipk aaaaa-aaaaa-aaaaa-aaaaa-aaaaa')
	cmd('slmgr -ato')

def cpp(): #COPIAR PROGRAMAS
	cmd("xcopy /E /I D:\install\Temp C:\Temp")

def chgbkg(): #CAMBIAR FONDO
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\Temp\wallpaper.png" , 0)
	cmd('REG ADD "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "C:\Temp\wallpaper.png" /f')

def confie(): #CONFIGURAR IE
	cmd('D: & cd install & cd ieconf & copy iesettings.reg C:\ & copy iecompatibility.reg C:\ ')
	cmd('cd C:\\ & regedit iesettings.reg')
	cmd('cd C:\\ & regedit iecomparibility.reg')

def insany(): #INSTALAR ANYDESK
	cmd("C:\\Temp/anydesk.exe")

def insninite(): #INSTALAR NINITE
	cmd("C:\\Temp/ninite.exe")

def activarp(): #ACTIVAR PROJECT
	cmd('cd C:\\ & cd Program Files & cd Microsoft Office & cd Office15 & cscript OSPP.VBS /inpkey:aaaaa-aaaaa-aaaaa-aaaaa-aaaaa')

def activarv(): #ACTIVAR VISIO
	cmd('cd C:\\ & cd Program Files & cd Microsoft Office & cd Office15 & cscript OSPP.VBS /inpkey:aaaaa-aaaaa-aaaaa-aaaaa-aaaaa')

def todo(): #HACE ToDO
	n = caja1.get()
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" /v ComputerName /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v ComputerName /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "NV Hostname" /t REG_SZ /d '+n+' /f')
	cmd('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v Hostname /t REG_SZ /d '+n+' /f')

	cmd("net user administrador /active:yes")
	cmd("net user administrador Pss1166")

	cmd('slmgr -ipk 9CN6F-GPBCD-6RW97-HFJGW-29XR4')
	cmd('slmgr -ato')

	cmd("xcopy /E /I D:\install\Temp C:\Temp")

	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\wallpaper.jpg" , 0)
	cmd('REG ADD "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "C:\wallpaper.jpg" /f')

	cmd('D: & cd install & cd ieconf & copy iesettings.reg C:\ & copy iecompatibility.reg C:\ ')
	cmd('cd C:\\ & regedit iesettings.reg')
	cmd('cd C:\\ & regedit iecomparibility.reg')

	cmd("C:\\Temp/anydesk.exe")

	cmd('cd C:\\ & cd Program Files & cd Microsoft Office & cd Office15 & cscript OSPP.VBS /inpkey:V27CP-CN7VM-B89M9-3CKJT-QYF2M')

	cmd('cd C:\\ & cd Program Files & cd Microsoft Office & cd Office15 & cscript OSPP.VBS /inpkey:NXKJM-48J9C-673JX-RQ69V-6XVWF')

############################### TKINTER #########################################

ventana = tk.Tk() #VENTANA PRINCIPAL
ventana.title("Instalador")
ventana.config(width=400, height=300)

botons = tk.Button(text="Cambiar nombre PC",command=chgname)
botons.place(x=2, y=2, width=120, height=20)

caja1 = tk.Entry() #CAJA DONDE VA EL NOMBRE
caja1.place(x=250, y=0, width=100, height=20)

etiqueta = tk.Label(text="Nombre Equipo: ")
etiqueta.place(x=150, y=0)

botons = tk.Button(text="Activar Admin",command=activaradm)
botons.place(x=2, y=24, width=120, height=20)

botons = tk.Button(text="Activar Windows",command=activarw)
botons.place(x=2, y=46, width=120, height=20)

botons = tk.Button(text="Copiar Programas",command=cpp)
botons.place(x=2, y=68, width=120, height=20)

botons = tk.Button(text="Cambiar Fondo",command=chgbkg)
botons.place(x=2, y=90, width=120, height=20)

botons = tk.Button(text="Configurar IE",command=confie)
botons.place(x=2, y=112, width=120, height=20)

botons = tk.Button(text="Instalar AnyDesk",command=insany)
botons.place(x=2, y=134, width=120, height=20)

botons = tk.Button(text="Instalar Ninite",command=insninite)
botons.place(x=2, y=156, width=120, height=20)

botons = tk.Button(text="Activar Project",command=activarp)
botons.place(x=2, y=178, width=120, height=20)

botons = tk.Button(text="Activar Visio",command=activarv)
botons.place(x=2, y=200, width=120, height=20)

botons = tk.Button(text="Instalar Todo",command=todo)
botons.place(x=2, y=222, width=120, height=20)

botons = tk.Button(text="Exit",command=ventana.destroy) #Boton Exit
botons.place(x=278, y=278, width=120, height=20)

etiqueta = tk.Label(text="Federico Contarino")
etiqueta.place(x=2, y=278)

ventana.mainloop()