import math
from colorama import Fore, Back, Style, init

init(autoreset=True)

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

def print_titulo(texto):

    print(f"\n{Fore.CYAN}{Back.BLUE}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Back.BLUE}{texto:^60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Back.BLUE}{'='*60}{Style.RESET_ALL}")

def print_subtitulo(texto):

    print(f"\n{Fore.YELLOW}{Style.BRIGHT}➤ {texto}{Style.RESET_ALL}")

def print_sucesso(texto):

    print(f"{Fore.GREEN}✓ {texto}{Style.RESET_ALL}")

def print_erro(texto):

    print(f"{Fore.RED}✗ {texto}{Style.RESET_ALL}")

def print_resultado(texto, valor):

    print(f"{Fore.MAGENTA}{Style.BRIGHT}{texto}: {Fore.WHITE}{Back.MAGENTA} {valor} {Style.RESET_ALL}")

def exibir_menu():

    print_titulo("SISTEMA DE CÁLCULOS")
    
    opcoes = [
        "1. Calcular Tabuada",
        "2. Calcular Área de Terreno",
        "3. Calcular Área de Círculo",
        "4. Calcular Potência",
        "5. Calcular Fatorial",
        "6. Sair"
    ]
    
    for opcao in opcoes:
        print(f"{Fore.CYAN}{Style.BRIGHT}   {opcao}{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{Back.BLUE}{'='*60}{Style.RESET_ALL}")

def main():

    while True:
        exibir_menu()
        
        try:
            opcao = input(f"\n{Fore.YELLOW}➤ Digite a opção desejada: {Style.RESET_ALL}")
            
            if opcao == "1":
                print_subtitulo("CÁLCULO DE TABUADA")
                numero = int(input(f"{Fore.WHITE}Digite o número para a tabuada: {Style.RESET_ALL}"))
                limite = input(f"{Fore.WHITE}Digite o limite (padrão 10): {Style.RESET_ALL}")
                limite = int(limite) if limite else 10
                
                resultados = calcular_tabuada(numero, limite)
                print_sucesso(f"Tabuada do {numero}:")
                for resultado in resultados:
                    print(f"{Fore.BLUE}   {resultado}{Style.RESET_ALL}")
                    
            elif opcao == "2":
                print_subtitulo("CÁLCULO DE ÁREA DE TERRENO")
                largura = float(input(f"{Fore.WHITE}Digite a largura do terreno: {Style.RESET_ALL}"))
                comprimento = float(input(f"{Fore.WHITE}Digite o comprimento do terreno: {Style.RESET_ALL}"))
                
                area = calcular_area_terreno(largura, comprimento)
                print_resultado("Área do terreno", f"{area:.2f}m²")
                
            elif opcao == "3":
                print_subtitulo("CÁLCULO DE ÁREA DE CÍRCULO")
                raio = float(input(f"{Fore.WHITE}Digite o raio do círculo: {Style.RESET_ALL}"))
                
                area = calcular_area_circulo(raio)
                print_resultado("Área do círculo", f"{area:.2f}")
                
            elif opcao == "4":
                print_subtitulo("CÁLCULO DE POTÊNCIA")
                base = float(input(f"{Fore.WHITE}Digite a base: {Style.RESET_ALL}"))
                expoente = float(input(f"{Fore.WHITE}Digite o expoente: {Style.RESET_ALL}"))
                
                resultado = calcular_potencia(base, expoente)
                print_resultado(f"{base}^{expoente}", resultado)
                
            elif opcao == "5":
                print_subtitulo("CÁLCULO DE FATORIAL")
                numero = int(input(f"{Fore.WHITE}Digite o número para calcular o fatorial: {Style.RESET_ALL}"))
                
                resultado = calcular_fatorial(numero)
                print_resultado(f"{numero}!", resultado)
                
            elif opcao == "6":
                print_sucesso("Saindo do sistema... Até logo!")
                break
                
            else:
                print_erro("Opção inválida! Tente novamente.")
                
            input(f"\n{Fore.WHITE}Pressione Enter para continuar...{Style.RESET_ALL}")
            print("\n" * 50)
                
        except ValueError:
            print_erro("Digite um valor numérico válido!")
        except Exception as e:
            print_erro(f"Erro inesperado: {e}")

if __name__ == '__main__':
    main()