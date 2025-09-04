from calculos import calcular_tabuada, calcular_area_terreno, calcular_fatorial
from colorama import Fore, Back, Style, init

init(autoreset=True)

def print_titulo(texto):

    print(f"\n{Fore.GREEN}{Back.BLACK}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Back.BLACK}{texto:^60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Back.BLACK}{'='*60}{Style.RESET_ALL}")

def print_resultado(texto, valor):

    print(f"{Fore.CYAN}{Style.BRIGHT}{texto}: {Fore.WHITE}{Back.CYAN} {valor} {Style.RESET_ALL}")

def app_secundaria():

    print_titulo("APLICAÇÃO SECUNDÁRIA")
    print(f"{Fore.YELLOW}Esta aplicação usa apenas algumas funções do sistema principal")
    print(f"e mostra apenas os resultados finais.{Style.RESET_ALL}\n")
    
    print(f"{Fore.MAGENTA}1. Tabuada do 7 (limite 5):{Style.RESET_ALL}")
    resultados_tabuada = calcular_tabuada(7, 5)
    print_resultado("Último resultado", resultados_tabuada[-1])
    
    print(f"\n{Fore.MAGENTA}2. Área de terreno 12.5m x 8.3m:{Style.RESET_ALL}")
    area = calcular_area_terreno(12.5, 8.3)
    print_resultado("Área calculada", f"{area:.2f}m²")
    
    print(f"\n{Fore.MAGENTA}3. Fatorial de 6:{Style.RESET_ALL}")
    fatorial = calcular_fatorial(6)
    print_resultado("Resultado", fatorial)
    
    print(f"\n{Fore.GREEN}{Back.BLACK}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Back.BLACK}{'Fim da aplicação secundária':^60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Back.BLACK}{'='*60}{Style.RESET_ALL}")

if __name__ == '__main__':
    app_secundaria()