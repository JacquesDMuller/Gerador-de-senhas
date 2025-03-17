import random
import string

def gerar_senha(comprimento=16):
    # Define os caracteres que podem ser usados na senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Garante que a senha terá pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]
    
    # Completa o resto da senha com caracteres aleatórios
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    for _ in range(comprimento - 4):
        senha.append(random.choice(todos_caracteres))
    
    # Embaralha a senha final
    random.shuffle(senha)
    
    # Converte a lista de caracteres em uma string
    return ''.join(senha)

def main():
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado da senha (mínimo 8): "))
            if comprimento < 8:
                print("O comprimento mínimo é 8 caracteres!")
                continue
                
            senha = gerar_senha(comprimento)
            print("\nSua senha segura é:", senha)
            
            opcao = input("\nDeseja gerar outra senha? (s/n): ").lower()
            if opcao != 's':
                break
                
        except ValueError:
            print("Por favor, digite um número válido!")

if __name__ == "__main__":
    main() 
