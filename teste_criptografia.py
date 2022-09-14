def cripto(frase):
    tradutor = " "
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + '@'
        else:
            tradutor = tradutor = letra
    return tradutor
print(cripto(input("Digite sua frase : ")))
