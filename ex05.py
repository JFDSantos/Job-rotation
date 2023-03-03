coisa = input("Digite alguma coisa: ")
coisa_invertida = []
for i in coisa[::-1]:
    coisa_invertida.append(i)

print("".join(coisa_invertida))