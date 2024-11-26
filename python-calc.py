def calculadora(valor1, valor2, operacao):
    # Verifica se os valores de entrada são números
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
    except ValueError:
        return None

    # Realiza a operação com base na entrada
    if operacao == '+':
        return valor1 + valor2
    elif operacao == '-':
        return valor1 - valor2
    elif operacao == '*':
        return valor1 * valor2
    elif operacao == '/':
        # Verifica divisão por zero
        if valor2 == 0:
            return None
        return valor1 / valor2
    elif operacao == '^':
        return valor1 ** valor2
    else:
        # Retorna None se a operação não for válida
        return None

# Exemplo de uso
if __name__ == "__main__":
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")
    operacao = input("Digite a operação (+, -, *, /, ^): ")

    resultado = calculadora(valor1, valor2, operacao)
    if resultado is None:
        print("Entrada ou operação inválida.")
    else:
        print(f"O resultado é: {resultado}")
