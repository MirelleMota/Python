# recebendo como entrada um número natural maior ou igual a dois
# e exibindo o ímpar anterior e o par posterior.

num1 = int(input())
if (num1 % 2) == 0: #verifica se é par
    num2 = num1 - 1
    num3 = num1 + 2
elif (num1 % 2) == 1: #verifica se é impar
    num2 = num1 - 2
    num3 = num1 + 1
print(num2,num3)