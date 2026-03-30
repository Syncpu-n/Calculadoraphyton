a1, l1 = map(float, input('Digite a altura e a largura do retângulo 1: ').split())
a2, l2 = map(float, input('Digite a altura e a largura do retângulo 2:').split())

 
area1= a1 * l1

area2= a2 * l2

if area1 > area2:
    print('O retângulo 1 é maior que o retângulo 2 pois sua area é de {}'.format (area1))
elif area1 == area2:
    print('As áreas são iguais')
elif area2 > area1:
    print('A área do segundo retângulo é maior que a do retângulo 1, pois sua área é de {}'.format (area2))
