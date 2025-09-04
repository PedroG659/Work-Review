from calculos import calcular_tabuada, calcular_area_terreno, calcular_fatorial

def app_secundaria():
 
    print("="*50)
    print("APLICAÇÃO SECUNDÁRIA")
    print("="*50)
    print("Esta aplicação usa apenas algumas funções do sistema principal")
    print("e mostra apenas os resultados finais.\n")
    
    print("1. Tabuada do 7 (limite 5):")
    resultados_tabuada = calcular_tabuada(7, 5)
    print(f"Último resultado: {resultados_tabuada[-1]}")
    
    print("\n2. Área de terreno 12.5m x 8.3m:")
    area = calcular_area_terreno(12.5, 8.3)
    print(f"Área calculada: {area:.2f}m²")
    
    print("\n3. Fatorial de 6:")
    fatorial = calcular_fatorial(6)
    print(f"Resultado: {fatorial}")
    
    print("\n" + "="*50)
    print("Fim da aplicação secundária")
    print("="*50)

if __name__ == '__main__':
    app_secundaria()