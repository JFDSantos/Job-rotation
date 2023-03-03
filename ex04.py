faturamento = {"sp": 67836.43, "rj": 36678.66, "mg":29229.88, "es": 27165.48, "outros":19849.53}
total = 0
porcentagem = {"sp": 0, "rj": 0, "mg": 0, "es": 0, "outros": 0}

for i in faturamento:
    total += faturamento[i]
    
for i in faturamento:
    porcentagem[i] = (faturamento[i]/total)
    print(f"{i}: {porcentagem[i]:.2%}")
