def inicializa(netdim):
    np.random.seed(1)

    L = len(netdim)
    variaveis = {}

    for i in range(0,L):
        variaveis['W'+str(i)]=np.random.randn(netdim[1+i],netdim[0+i])
        variaveis['b'+str(i)]=np.random.randn(netdim[1+i],1)

    return variaveis

def propForward(A,variaveis):

    L = len(variaveis)/2

    for i in range(0,L-1):
        W=variaveis['W'+i]
        b=variaveis['b'+i]
        Z=np.dot(W,A) + b
        A=np.maximum(Z) # Relu

    W=variaveis['W'+L]
    b=variaveis['b'+L]
    Z=np.dot(W,A) + b
    AL=1/(1 + np.exp(-Z)) # sigmoid
    
    return AL

def propBackward(AL,Y,variaveis):
    L = len(variaveis)/2
    m=AL.shape[0]

    dA=(1/m)*np.sum(Y/AL - (1-Y)/(1-AL))
    dZ= np.dot(dA, (1-np.sqrt(AL)))
    dW= dZ * 
    db=
    
    for i in range(0,L-1):
        dA=
        dZ=
        dW=
        db=

    return


def atualizaparam(gradientes):



def custo(AL,Y):
