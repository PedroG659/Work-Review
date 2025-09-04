import math

def calcular_tabuada(numero, limite=10):

    resultados = []
    for i in range(1, limite + 1):
        resultados.append(f"{numero} x {i} = {numero * i}")
    return resultados

def calcular_area_terreno(largura, comprimento):

    return largura * comprimento

def calcular_area_circulo(raio):

    return math.pi * (raio ** 2)

def calcular_potencia(base, expoente):

    return base ** expoente

def calcular_fatorial(numero):

    if numero < 0:
        return "Erro: Fatorial não definido para números negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

def exibir_menu():

    print("\n" + "="*50)
    print("SISTEMA DE CÁLCULOS")
    print("="*50)
    print("1. Calcular Tabuada")
    print("2. Calcular Área de Terreno")
    print("3. Calcular Área de Círculo")
    print("4. Calcular Potência")
    print("5. Calcular Fatorial")
    print("6. Sair")
    print("="*50)

def main():

    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                numero = int(input("Digite o número para a tabuada: "))
                limite = int(input("Digite o limite (padrão 10): ") or 10)
                resultados = calcular_tabuada(numero, limite)
                print(f"\nTabuada do {numero}:")
                for resultado in resultados:
                    print(resultado)
                    
            elif opcao == 2:
                largura = float(input("Digite a largura do terreno: "))
                comprimento = float(input("Digite o comprimento do terreno: "))
                area = calcular_area_terreno(largura, comprimento)
                print(f"\nÁrea do terreno: {area:.2f}m²")
                
            elif opcao == 3:
                raio = float(input("Digite o raio do círculo: "))
                area = calcular_area_circulo(raio)
                print(f"\nÁrea do círculo: {area:.2f}")
                
            elif opcao == 4:
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = calcular_potencia(base, expoente)
                print(f"\n{base}^{expoente} = {resultado}")
                
            elif opcao == 5:
                numero = int(input("Digite o número para calcular o fatorial: "))
                resultado = calcular_fatorial(numero)
                print(f"\n{numero}! = {resultado}")
                
            elif opcao == 6:
                print("Saindo do sistema...")
                break
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except ValueError:
            print("Erro: Digite um valor numérico válido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    main()