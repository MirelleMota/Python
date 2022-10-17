lista_dias_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

dia_entrada = input() #quarta

quant_dias = int(input()) #6

if quant_dias == 0:
    print('chega hoje!')
else:
    index_dia_semana = lista_dias_semana.index(dia_entrada) #3
    nova_lista_semana = lista_dias_semana[index_dia_semana + 1:len(lista_dias_semana)] + lista_dias_semana[0:index_dia_semana]
    dia_entrega = nova_lista_semana[quant_dias - 1]
    print('sera entregue', dia_entrega)


