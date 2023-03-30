# Definindo a string original
string_original = "Hello, world!"

# Criando a nova string vazia
nova_string = ""

# Percorrendo a string original de trás para frente
for i in range(len(string_original)-1, -1, -1):
    # Adicionando cada caractere na nova string
    nova_string += string_original[i]

# Imprimindo a nova string invertida
print(nova_string)
