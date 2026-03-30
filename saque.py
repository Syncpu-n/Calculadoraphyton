saque=int(input('Digite o valor que você quer sacar '))
#notas 
n200=saque//200 

saque=saque%200

n100=saque//100

saque=saque%100

n50=saque//50

saque=saque%50

n20=saque//20

saque=saque%20

n10=saque//10

saque=n10%10

n5=saque//5

saque=saque%5

n2=saque//2

saque=saque%2

n1=saque//1 

saque=saque%1

print("aqui esta o valor que você ira sacar {} notas de 200,{} notas de 100,{} notas de 50,{} notas de 20, {} notas de 10, {} notas de 5 {} notas  de 2, {} moedas de 1".format (n200,n100,n50,n20,n10,n5,n2,n1))