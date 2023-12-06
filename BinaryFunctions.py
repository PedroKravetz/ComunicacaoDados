import struct

# Transforma palavra em array de bit e uma string de bits que representa a palavra em ascii
# Ele foi baseado no código disponível em https://github.com/walger-lucas/ComunicacaoDados
def ToBinary(word):
    l =[]
    bitsString =''
    for i in word:
        l.append(bin(ord(i))[2:].zfill(8))

    for i in l:
        bitsString+=i
    bitsArray= []
    for i in bitsString:
        bitsArray.append(int(i))

    return bitsArray

# Transforma de array de bits para string de bits
# Ele foi baseado no código disponível em https://github.com/walger-lucas/ComunicacaoDados
def ArrayBitsToStringBits(bitsArray=[]):
    s=''
    for i in bitsArray:
        s+=str(i)
    return s

# Transforma de bits para string
# Ele foi baseado no código disponível em https://github.com/walger-lucas/ComunicacaoDados
def ToString(binArray=[]):
    text =''
    for i in range(0,len(binArray),8):
        text+= chr(binArray[i]*128+binArray[i+1]*64+binArray[i+2]*32+binArray[i+3]*16+binArray[i+4]*8+binArray[i+5]*4+binArray[i+6]*2+binArray[i+7]*1)
    return text

ENCODING4D_PAM5 = [-2, 1, -1, 2]
## 4D_Pam5 ENCODER DECODER 
# Ele foi baseado no vídeo disponível em https://www.youtube.com/watch?v=luo1dh5Kie8&ab_channel=J%C3%A9ssicaMedalha 
def Encode4D_Pam5(binaryArray=[]):
    resultArray =[]
    for i in range(0,len(binaryArray),2):
        number_int = binaryArray[i]*2+binaryArray[i+1]
        voltage = ENCODING4D_PAM5[number_int]
        resultArray.append(voltage)
    return resultArray
    
# Gera um array de bits a partir de um array no line code 4D-Pam5
# Ele foi baseado no vídeo disponível em https://www.youtube.com/watch?v=luo1dh5Kie8&ab_channel=J%C3%A9ssicaMedalha 
def Decode4D_Pam5(data4d=[]):
    result=[]
    for i in data4d:
        if i==-2:
            result.append(0)
            result.append(0)
        elif i==1:
            result.append(0)
            result.append(1)
        elif i==-1:
            result.append(1)
            result.append(0)
        elif i==2:
            result.append(1)
            result.append(1)
    return result

## Empacotamento e Desempacotamento de Dados

# Empacota dados em uma forma enviável pela socket
# Ele foi baseado no código disponível em https://github.com/walger-lucas/ComunicacaoDados
def PackData(data=[]):
    pack= struct.pack('!{}i'.format(len(data)),*data)
    return pack

# Desempacota dados em uma forma enviável pela socket
# Ele foi baseado no código disponível em https://github.com/walger-lucas/ComunicacaoDados
def UnpackData(pack):
     data= struct.unpack('!{}i'.format(len(pack)//4),pack)
     return data