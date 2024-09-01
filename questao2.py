def contar_letra_a(s):
    s = s.lower()
    contagem = s.count('a')
    return contagem

string = input("Insira uma palavra: ")
quantidade = contar_letra_a(string)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na palavra.")
else:
    print("A letra 'a' não aparece na palavra.")
