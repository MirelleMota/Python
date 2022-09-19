import pandas as pd
import win32com.client as win32

# IMPORTAR A BASE DE DADOS
tabela_vendas = pd.read_excel('Vendas.xlsx')

# VISUALIZAR A BASE DE DADOS
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# FATURAMENTO POR LOJA
#Filtrar as colunas que eu quero, agrupar todas lojas e somar o faturamento.
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# QUANTIDADE DE PRODUTOS VENDIDOS POR LOJA
quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-' * 50)

# TICKET MEDIO POR PRODUTO EM CADA LOJA (faturamento / quantidade) #Tabela / por outra não gera uma tabela e necessita do "to frame"
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() #to frame transforma em uma tabela
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# ENVIAR E-MAIL COM RELATÓRIO
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'mirelle.motta06@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att,</p>
<p>Mirelle Mota<p>
'''

mail.Send()

