import os

local = os.path.dirname(os.path.realpath(__file__))

while True:
    msg = input("Digite Aqui: ")
    ultMFile = open(local + "\\data\\ultM.data", "w")
    ultMFile.writelines(msg)
    ultMFile.close()
    os.system("cls")