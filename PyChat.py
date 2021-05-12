import os


#User name
if not os.path.isfile("bin/data/UserName.cfg"):
    nome = input("Nome de Usuário: ")
    nameF = open("bin/data/UserName.cfg", "w")
    nameF.writelines(nome)
    nameF.close()

local = os.path.dirname(os.path.realpath(__file__))
chatBoxLocal = local + '\\bin\\ChatBox.py'
inputBoxLocal = local + '\\bin\\InputBox.py'


#Run ChatBox.py and InputBox.py
os.startfile(inputBoxLocal)
os.startfile(chatBoxLocal)
