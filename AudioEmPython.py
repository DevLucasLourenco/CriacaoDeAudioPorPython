#pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

for ciclo in range(1):
    engine.say('Olá, usuário!')
    engine.say('Código em python sendo rodado')

    engine.runAndWait()
    
