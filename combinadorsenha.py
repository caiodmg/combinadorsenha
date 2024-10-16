import random 
from faker import Faker

fake = Faker('pt_BR')

palavras = [fake.word() for _ in range(1)]
caracteres = "!@#$%&*"

def gerar_combinacao():
    #Utilizei o random choice para escolher 1 palavra dentro da lista de palavras e caracteres. 
    palavra = random.choice(palavras)
    caracter = random.choice(caracteres)
    caracter2 = random.choice(caracteres)
    
    #Utilizei o random.randit para escolher 1 numero no intervalo de 0 a 500
    numero1 = (str(random.randint(0, 500)))
    numero2 = (str(random.randint(0, 500)))
     
    
    #Fiz uma lista de senha com o numero, palavra e caracteres escolhidos no choice
    senha = [palavra, numero1, numero2, caracter, caracter2]

    #Utilizei o random.shuffle para embaralhar a lista de senha
    random.shuffle(senha)
      
    return ''.join(senha)

senha_gerada = gerar_combinacao()

print(senha_gerada)
    