from ast import If
from cmath import inf


nota_trabalhos = float(input())
prova_regular = float(input())
media = (nota_trabalhos + prova_regular) / 2
nota_substitutiva_min = 12 - nota_trabalhos
media2 = (nota_trabalhos + nota_substitutiva_min) / 2
if media >= 6:
    print('aprovado')
elif nota_substitutiva_min<=10 and media2 >= 6:
    print('talvez com a sub')
else: 
    print('reprovado')

