import numpy as np
import matplotlib.pyplot as plt
from functions import *

X=
Y=

netdim = []
variaveis = inicializa(netdim)
AL=X

np.random

for i in range(1,inte)
    AL = propForward(A,variaveis)#calculo do modelo
    gradientes = propBackward(AL,Y,variaveis)#backpropagations
    variaveis = atualizaparam(gradientes)
    A=AL
    J = custo(AL,Y)#custo
    #printar J
