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
    variaveis2={}
    for i in range(0,L-1):
        W=variaveis['W'+i]
        b=variaveis['b'+i]
        Z=np.dot(W,A) + b
        A=np.maximum(Z) # Relu
        variaveis2['Z'+i]=Z
        variaveis2['A'+i]=A

    W=variaveis['W'+L]
    b=variaveis['b'+L]
    Z=np.dot(W,A) + b
    AL=1/(1 + np.exp(-Z)) # sigmoid
    variaveis2['Z'+L]=Z
    variaveis2['A'+L]=AL
    return AL, variaveis2

def propBackward(AL,Y,variaveis,var2):
    L = len(variaveis)/2
    m=AL.shape[0]
    gradientes={}

    A=var2['A'+ srt(range(0,L+1))]
    Z=var2['Z'+ srt(range(0,L+1))]
    W=variaveis['W'+srt(range(0,L+1))]
    
    dA=(1/m)*np.sum(Y/AL - (1-Y)/(1-AL))
    dZ=dA*(1-np.sqrt(AL)) #derivada da camada com sigmoid
    
    for i in range(L-1,0,-1):
        dW=dZ*A[i-1]
        db=dZ
        dA=dZ*W[i]
        dZ=dA*np.heaviside(Z[i-1]) # derivada da camada com Relu
        gradientes['dW'+i]=dW
        gradientes['db'+i]=db
    
    return gradientes


def atualizaparam(alfa,gradientes,variaveis):
    var={}
    L=len(gradientes)/2
    for i in range(0,L+1):
        var['W'+i]=variaveis['W'+i]+alfa*gradientes['dW'+i]
        var['b'+i]=variaveis['b'+i]+alfa*gradientes['db'+i]
    return var


def custo(AL,Y):
    return J=(1/len(Y))*np.sum(Y*log(AL)-(1-Y)*log(1-AL))
