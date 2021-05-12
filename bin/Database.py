import pyrebase

#Configuração do Firebase
firebaseConfig = {
    "apiKey": "AIzaSyDOlZ0ReztZB6e1iU8RvaWJXZcsuIW8now",
    "authDomain": "avaliacao-eb2ec.firebaseapp.com",
    "databaseURL": "https://avaliacao-eb2ec.firebaseio.com",
    "projectId": "avaliacao-eb2ec",
    "storageBucket": "avaliacao-eb2ec.appspot.com",
    "messagingSenderId": "42796567000",
    "appId": "1:42796567000:web:12eb72d28642eed3098aad",
    "measurementId": "G-W4X1VE8JXK"
}

firebase = pyrebase.initialize_app(firebaseConfig)

