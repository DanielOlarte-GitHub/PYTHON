#casino ruleta

import random

casillas = ['v', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']



def ruleta():
    cantR = 0
    cantV = 0
    cantN = 0
    seguidasR = 0
    seguidasV = 0
    seguidasN = 0
    listaResultados = []
    listaSeguidasR = []
    listaSeguidasV = []
    listaSeguidasN = []
    for i in range(10):
        tirada = random.choice(casillas)
        listaResultados.append(tirada)
        if tirada == 'r':
            cantR = cantR + 1
            if listaResultados[i-1] == 'r':
                seguidasR = seguidasR + 1
            else:
                listaSeguidasR.append(seguidasR)
                seguidasR = 0
        elif tirada == 'v':
            cantV = cantV + 1
            if listaResultados[i-1] == 'v':
                seguidasV = seguidasV + 1
            else: 
                listaSeguidasV.append(seguidasV)
                seguidasV = 0
        else:
            cantN = cantN + 1
            if listaResultados[i-1] == 'n':
                seguidasN = seguidasN + 1
            else:
                listaSeguidasN.append(seguidasN)
                seguidasN = 0
    return cantR, cantV, cantN, listaSeguidasR, listaSeguidasV, listaSeguidasN
        
cR, cV, cN, LR, LV, LN = ruleta()

print("\n\nRESULTADO DE ROJAS: ",cR)
print("RESULTADO DE NEGRAS: ",cN)
print("RESULTADO DE VERDES: ",cV)

print("\n\nRESULTADO DE ROJAS SEGUIDAS: ",max(LR))
print("RESULTADO DE NEGRAS SEGUIDAS: ",max(LN))
print("RESULTADO DE VERDES SEGUIDAS: ",max(LV))