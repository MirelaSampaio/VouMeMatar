# Verificar quantas e quais pessoas pagaram mais do que 50

'''
Inicialização: Comece com uma contagem inicial de zero para o número de pessoas que pagaram mais de 50 reais.

Iteração pela lista: Percorra cada pessoa na lista de 1000 pessoas.

Verificação do valor pago: Para cada pessoa na lista, verifique o valor que ela pagou.

Condição de pagamento: Se o valor pago pela pessoa for maior que 50 reais, aumente sua contagem.

Armazenamento opcional: Você pode manter uma lista separada das pessoas que pagaram mais de 50 reais, se necessário.

Impressão dos resultados: Ao final da verificação de todas as pessoas, imprima o número total de pessoas que pagaram mais de 50 reais e, se desejado, a lista de pessoas.
'''
#--------------------------------------------------------------------------------------------------------------------------------
'''
import csv

contador = 0
pagaramMaisCinquenta = []

arquivo = open('pagadores.csv', 'r')
dados = csv.reader(arquivo)
for linha in dados:
    print(linha)


'''


import csv

# Inicializar variáveis
contador = 0
pessoas_mais_de_50_reais = []

# Abrir o arquivo CSV em modo leitura
with open('pagadores.csv', mode='r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Iterar pelas linhas do arquivo CSV
    for linha in leitor_csv:
        nome = linha[0]  # Supondo que a primeira coluna seja o nome
        valor_pago = float(linha[1])  # Supondo que a segunda coluna seja o valor pago
        
        # Verificar se o valor pago é maior que 50 reais
        if valor_pago > 50:
            contador += 1
            pessoas_mais_de_50_reais.append(nome)

# Imprimir os resultados
print(f"Total de pessoas que pagaram mais de 50 reais: {contador}")
print("Pessoas que pagaram mais de 50 reais:", pessoas_mais_de_50_reais)
