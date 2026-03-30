while True:
  try: 
    
    print('Bem vindo a Calculadora Master:')

    print()

    n1=int(input('Digite seu número:').strip())
    n2=int(input('Digite seu segundo número:').strip())

    print("*" * 30)

    
    print("      MENU") 

    print("*" * 30)

    print("1 - [+]")

    print("2 - [-]")

    print("3 - [*]")

    print("4- [**]")

    print("5 - [/]")


    print("*" * 30)

    operacao = input("Digite a operação (1, 2, 3 , 4, 5): ").strip()
  
    if operacao == "1" :
     print('O resultado da sua operação é: {}'.format (n1 + n2))

    elif operacao == "2":
     print ('O resultado da sua operação é: {}'.format (n1 - n2))

    elif operacao == "3":
     print (' O resultado da sua operação é: {}'.format (n1 * n2))
    elif operacao== "4":
      print (' O resultado da sua operação é: {} '. format (n1 ** n2))
 
    elif operacao == "5":
      try:
        print ('O resultado da sua divisão é {:.2f}'.format (n1/n2))

      except ZeroDivisionError:  
        print (' Não é possivel dividir por zero')
  except ValueError:
    print ('Voce deve digitar apenas números')

