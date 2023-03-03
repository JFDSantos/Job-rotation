import json

total = 0
lista = []
count = 0

with open("dados.json") as file:
    data = (json.load(file))

menor = data[0]['valor']

for i in data:
    if i['valor'] != 0:
        lista.append(i['valor'])
    total += i['valor']

list.sort(lista)

for i in lista:
    if i > (total/len(data)):
        count+=1

print(f'Menor faturamento: {lista[0]}')
print(f'Maior faturamento: {lista[-1]}')
print(f'Quantidade de faturamentos maiores que a média {count}')
