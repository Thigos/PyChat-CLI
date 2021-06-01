# PyChat-CLI


## Dependências
``` js
Pyrebase
```

Chat Rápido, Simples e Seguro, feito para rodar no terminal usando Python + Firebase Database.

## Configuração Firebase
Substitua sua [firebaseConfig](https://firebase.google.com/docs/web/setup?hl=pt-br) no [Database.py](bin/Database.py)
``` python
firebaseConfig = {
  apiKey: "api-key",
  authDomain: "project-id.firebaseapp.com",
  databaseURL: "https://project-id.firebaseio.com",
  projectId: "project-id",
  storageBucket: "project-id.appspot.com",
  messagingSenderId: "sender-id",
  appID: "app-id",   
}
```
## Iniciar Chat

Execute no terminal ```python Pychat.py```

#### 'python' não é reconhecido<br>

Inicie o terminal em C:\Users\USER\AppData\Local\Programs\Python\PythonXX-xx<br>
Execute no terminal ```python LOCAL_PYCHAT-CLI/Pychat.py```


## Arquivos

- Pychat.py: <br>
Primeiro arquivo a ser executado: Configura o nome de usuário (bin/data/UserName.cfg) e inicia o ChatBox.py e InputBox.py

- ChatBox.py: <br>
Segundo arquivo a ser executado: Envia e recebe mensagens e comandos específicos

- InputBox.py: <br>
Terceiro arquivo a ser executado: Caixa para digitar textos ¯\_(ツ)_/¯

