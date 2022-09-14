## Felipe Matheus de Souza ra F32hgg8 
## Vinicius Willian Silva ra F330923
## Wenderson Braga Ferreira ra N678fj4
## Eduardo de Baptista Brolezi Mendes ra F2735j1
## Bruno Eduardo Almeida Santos ra F181588


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chave = 3
mensagem = "Atividade pratica supervisionada, Criptografia e Cifragem de Cesar."
n = 128
cifrada = ""
for letra in mensagem:
    indice = ord(letra)
    nova_letra = chr((indice + chave) % n)
    cifrada = cifrada + nova_letra
print("Original: ", mensagem)
print("Cifrada: ", cifrada)
