import random 

palavras = ['Relampago', 'Bicicleta', 'Supermercado', 'Rodoviaria', 'Labirinto']
caracteres = "!@#$%&*"

def gerar_combinacao():
    #Utilizei o random choice para escolher 1 palavra dentro da lista de palavras e caracteres. 
    palavra = random.choice(palavras)
    caracter = random.choice(caracteres)
    
    #Utilizei o random.randit para escolher 1 numero no intervalo de 0 a 500
    numero = (str(random.randint(0, 500)))
    
    #Fiz uma lista de senha com o numero, palavra e caracteres escolhidos no choice
    senha = [palavra, numero, numero, caracter, caracter]

    #Utilizei o random.shuffle para embaralhar a lista de senha
    random.shuffle(senha)
    
    #Utilizei o metodo join para combinar os elementos da lista senha 
    return ''.join(senha)

senha_gerada = gerar_combinacao()

print(senha_gerada)
    