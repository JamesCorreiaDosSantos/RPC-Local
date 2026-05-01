#codigo em python
#autor: james correia dos santos
#RA: 3020102828
#data: 28/09/23
#versão: 1.0

# biblioteca para Python RPC
import rpyc 
from rpyc.utils.server import ThreadedServer 
import math

class MyService(rpyc.Service):
   
    '''
    Este metodo é usado pra calcular o IMC de uma pesssoa e ele ira receber
    valores float e ira retornar uma string com a mensagem relativa ao IMC da pessoa.
    Para utilizar esse metodo ele devera ser implementado no cliente recebendo as
    variaveis necessarias, essa funão dever ser usada em conjunto com a
    biblioteca RPC e com os metodos connect(), root e print()
    
    '''
    def exposed_imc(self, altura, peso):
        valor =  round(float(peso) / (float(altura) * float(altura)),1)
        
        if(valor < 18.5):
            return (f"Seu IMC é de {valor} kg/m2 que significa Magreza")
        elif(valor >= 18.5 and valor <= 24.9):
            return (f"Seu IMC é de {valor} kg/m2 que significa Normal")
        elif(valor >= 25.0 and valor <= 29.9):
            return  (f"Seu IMC é de {valor} kg/m2 que significa Sobrepeso")
        elif(valor >= 30.0 and valor <= 34.9):
            return (f"Seu IMC é de {valor} kg/m2 que significa Obsidade grau I")
        elif(valor >= 35.0 and valor <= 39.9):
            return(f"Seu IMC é de {valor} kg/m2 que significa Obsidade grau II")
        elif(valor > 40.0):
            return (f"Seu IMC é de {valor} kg/m2 que significa Obsidade grau III")      


    '''
    Este metodo é usado pra calcular uma equação de segundo grau e ele ira receber
    valores float e ira retornar uma string com a mensagem relativa ao resultado.
    Para utilizar esse metodo ele devera ser implementado no cliente recebendo as
    variaveis necessarias, essa funão dever ser usada em conjunto com a
    biblioteca RPC e com os metodos connect(), root e print()

    '''

    def exposed_equacao(self, a, b,c):
        delta =  (float(b) * float(b)) -4.0 * float(a) * float(c)

        if(float(a) == 0):
             return "não é uma função de segundo grau"
    
        elif(float(delta) > 0):
            x1 = (-float(b) + math.sqrt(float(delta))) / (float(a) * 2.0)
            x2 = (-float(b) - math.sqrt(float(delta))) / (float(a) * 2.0)
            return (f" X1 = {x1} \n X2 = {x2}")
        elif(float(delta) == 0):
            x = (-float(b) / (2.0 * float(a)))
            return (f" X = {x}")
        elif(float(delta < 0)):
            return "a equação não possui solução real"
        
    '''
    Este metodo verifica se a palavra é um palindromo e ele ira receber um 
    valor float e ira retornar uma string com a mensagem relativa ao resultado.
    Para utilizar esse metodo ele devera ser implementado no cliente recebendo as
    variaveis necessarias, essa funão dever ser usada em conjunto com a
    biblioteca RPC e com os metodos connect(), root e print()
    
    '''
    def exposed_palindromo (self, p1):
        q = len(p1)

        vetor = []
        vetor2 = []

        for i in range(q):
            int(i) + 1
            vetor.append(p1[i])

            print("O vetor inserido é:", vetor[i])


        j = q
        for i in range(q):
            
            j = j - 1
            i + 1
            vetor2.append(p1[j])

            print("O vetor inserido é:", vetor2[i])

        t = 0
        for i in range(q):

            i + 1
            if vetor[i] == vetor2[i]:
                t = t + 1

        if(t == q):
            return "a palavra é um palíndromo "
        else:
            return "a palavra não é um palíndromo "
        

      
if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 8000)
    print('Servidor online')
    server.start()

 