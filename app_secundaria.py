"""
Aplicação Secundária - Usa funções do sistema principal
"""
from calculos import calcular_tabuada, calcular_area_terreno, calcular_fatorial

def app_secundaria():
    """
    Aplicação secundária que utiliza funções do sistema principal
    """
    print("="*50)
    print("APLICAÇÃO SECUNDÁRIA")
    print("="*50)
    print("Esta aplicação usa apenas algumas funções do sistema principal")
    print("e mostra apenas os resultados finais.\n")
    
    # Usando a função de tabuada
    print("1. Tabuada do 7 (limite 5):")
    resultados_tabuada = calcular_tabuada(7, 5)
    # Mostra apenas o último resultado
    print(f"Último resultado: {resultados_tabuada[-1]}")
    
    # Usando a função de área de terreno
    print("\n2. Área de terreno 12.5m x 8.3m:")
    area = calcular_area_terreno(12.5, 8.3)
    print(f"Área calculada: {area:.2f}m²")
    
    # Usando a função de fatorial
    print("\n3. Fatorial de 6:")
    fatorial = calcular_fatorial(6)
    print(f"Resultado: {fatorial}")
    
    print("\n" + "="*50)
    print("Fim da aplicação secundária")
    print("="*50)

if __name__ == '__main__':
    app_secundaria()