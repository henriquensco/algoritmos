"""
Provavelmente nunca terei que implementar uma tabela hash, 
pois qualquer linguagem já tem a sua implementação.
No Python, tabelas hash são chamadas de dicionários.
"""
def tabela_hash():
    caderno = dict()

    caderno['maca'] = 0.5
    caderno['leite'] = 4
    caderno['abacate'] = 3.75

    print(caderno)
    print(caderno['abacate'])

    #print(caderno.get('maca')) #Se encontrar um valor dentro do dict, retorna ele. Caso contrario, retorna None

def verifica_eleitor():
    eleitores = {}

    #eleitores['Henrique'] = 'votou'

    entradaEleitor = input("Qual o seu nome? ")

    if eleitores.get(entradaEleitor) != None:
        print('Xispa! Você já votou!')

    else:
        eleitores[entradaEleitor] = 'votou'


verifica_eleitor()