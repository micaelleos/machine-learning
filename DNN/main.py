import numpy as np
import matplotlib.pyplot as plt
from functions import *

X=
Y=

netdim = [] #dimensões das camadas
variaveis = inicializa(netdim)
A=X
alfa=0.1 # taxa de aprendizado
n=1000 # número de iterações

np.random

for i in range(1,n)
    AL,var2 = propForward(A,variaveis)#calculo do modelo
    gradientes = propBackward(AL,Y,variaveis,var2)#backpropagations
    variaveis = atualizaparam(alfa,gradientes,variaveis)
    A=AL
    J = custo(AL,Y)#custo
    #printar J
