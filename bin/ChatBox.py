print("Carregando Banco de dados")
import os
import Database
import time

# Load database and files
firebase = Database.firebase
db = firebase.database()

local = os.path.dirname(os.path.realpath(__file__))

sizeMsgVistas = 0

def main():
    # Read user name
    global sizeMsgVistas
    print("Banco de dados Carregado")
    userName = open(local + "\\data\\UserName.cfg", "r")
    name = userName.readlines()
    userName.close()


    while True:

        # Read file
        ultMFile = open(local + "\\data\\ultM.data", "r")
        msg = ultMFile.readlines()
        ultMFile.close()

        # Process message
        msg = ''.join(msg)
        msg = msg.strip()

        size = db.child('chat').child('size').get().val()


        # Send to Firebase Database
        if (msg != ''):
            db.child('chat').child('size' + str(int(size) + 1)).set("9mU" + ''.join(name) + "9mU" + msg)
            db.child('chat').child('size').set(int(size) + 1)

            sendCommands(msg)

            # Reset file
            ultMFile = open(local + "\\data\\ultM.data", "w")
            ultMFile.writelines("")
            ultMFile.close()

        # Read messages on database
        if(size > sizeMsgVistas):
            for i in range(sizeMsgVistas, int(size)):
                mensagemDB = db.child('chat').child('size' + str(i+1)).get().val()
                if(mensagemDB != None):
                    sizeMsgVistas = sizeMsgVistas +1

                    # Process message
                    mU = mensagemDB.index("9mU",1)
                    nomeMensagem = mensagemDB[3:mU]
                    message = mensagemDB[(mU+3):]
                    msgProcess = "  " + nomeMensagem + ": " + message
                    print(msgProcess)
                    receiveCommands(message)


def sendCommands(mensagem):
    global sizeMsgVistas
    mensagem = mensagem.lower()
    if mensagem == "/limpar_chat":
        print("             **Limpando Chat**")
        time.sleep(3)
        db.child("chat").remove()
        db.child("chat").child("size").set(0)
        os.system("cls")
        sizeMsgVistas = 0
        print("             **Chat Limpo**")


def receiveCommands(mensagem):
    global sizeMsgVistas
    mensagem = mensagem.lower()
    if mensagem == "/limpar_chat":
        print("             **Limpando Chat**")
        time.sleep(3)
        os.system("cls")
        sizeMsgVistas = 0
        print("             **Chat Limpo**")




#Exec função main()
if __name__ == '__main__':
    main()