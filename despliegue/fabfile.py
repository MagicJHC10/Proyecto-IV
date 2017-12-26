from fabric.api import *


def instalacion():
	run('sudo git clone https://github.com/MagicJHC10/Proyecto-IV')
	run('cd ./Proyecto-IV && sudo pip install -r requirements.txt')

def servicios():
    run('cd ./Proyecto-IV && sudo chmod +x script.sh', pty=False)
    run('cd ./Proyecto-IV && sudo sh script.sh', pty=False)

def borrado():
	run('sudo rm -rf ./Proyecto-IV')

def killPython():
run('sudo pkill python')
