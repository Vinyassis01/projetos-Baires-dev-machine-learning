import random

# Função geradora de valores
def gerador_de_valores(quantidade, limite_inferior, limite_superior):
    for _ in range(quantidade):
        yield random.randint(limite_inferior, limite_superior)

# Função para verificar se os valores gerados correspondem aos esperados
def verificar_valores(esperados, gerados):
    correspondencias = [valor for valor in gerados if valor in esperados]
    return len(correspondencias), correspondencias

# Exemplo de uso
if __name__ == "__main__":
    # Lista de valores esperados
    valores_esperados = [5, 10, 15, 20]

    # Gerar 10 valores aleatórios entre 1 e 20
    valores_gerados = list(gerador_de_valores(10, 1, 20))

    print("Valores esperados:", valores_esperados)
    print("Valores gerados:", valores_gerados)

    # Verificar correspondências
    quantidade, correspondencias = verificar_valores(valores_esperados, valores_gerados)
    print(f"Quantidade de correspondências: {quantidade}")
    print("Valores correspondentes:", correspondencias)