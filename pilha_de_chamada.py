def sauda(nome):
    print("Olá {nome}!".format(nome = nome))
    sauda2(nome)
    print("Preparado pra dar tchau?")
    tchau()

def sauda2(nome):
    print("Como vai {nome}?".format(nome = nome))

def tchau():
    print("tchau!")

sauda("Henrique")