import math

# Funções lambda
def calcular_area(forma, *args):
    areas = {
        'circulo': lambda r: round(math.pi * r**2, 5),
        'retangulo': lambda b, h: b * h,
        'triangulo': lambda b, h: (b * h) / 2
    }

    if forma in areas:
        return areas[forma](*args)
    else:
        return "Forma geométrica inválida!"

# Função de List Comprehension
def calcular_areas_multiplas(formas):
    return [calcular_area(forma, *params) for forma, params in formas]

# Função de Alta Ordem
def calcular_area_com_escala(func_area, forma, fator_escala, *args):
    # Calcula a área com a função passada como argumento
    area = func_area(forma, *args)
    
    if isinstance(area, (int, float)):
        # Aplica o fator de escala
        return area * fator_escala
    else:
        # Retorna a mensagem de erro caso a área não seja numérica
        return area
    
# Exemplo com Closure
def calcular_hipotenusa(a, b):
    def hipotenusa():
        return math.sqrt(a**2 + b**2)  # Cálculo da hipotenusa

    return hipotenusa

# Função principal
def menu_start():
    print("---- CALCULADORA DE GEOMETRIA ----")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Calculo de área.")
        print("2 - Calcular áreas múltiplas.")
        print("3 - Cálculo de área com fator de escala.")
        print("4 - Calcular hipotenusa de triângulo.")
        print("5 - Sair")
        opcao = input("Digite o número da operação que deseja realizar: ")

        if opcao == '1':
            print("\nEscolha o tipo de cálculo de área:")
            print("1 - Círculo")
            print("2 - Retângulo")
            print("3 - Triângulo")
            resultado = None
            operacao = input("Digite o número correspondente à operação desejada: ")
            if operacao == '1':
                r = float(input("Digite o valor do raio: "))
                resultado = calcular_area('circulo', r)
            elif operacao == '3':
                h = float(input("Digite o valor da altura: "))
                b = float(input("Digite o valor da base: "))
                resultado = calcular_area('triangulo',b,h)
            elif operacao == '2':
                 a = float(input("Digite o valor do primeiro lado: "))
                 b = float(input("Digite o valor do segundo lado: "))
                 resultado = calcular_area('retangulo',b,a)
            else:
                 print('Operação inexistente, tente novamente.')

            if resultado is not None:
                print(f"Área: {resultado}m²")

        elif opcao == '2':  # Calcular áreas múltiplas
            print("\nDigite os dados para calcular várias áreas ao mesmo tempo.")
            formas = []
            continuar = True

            while continuar:
                print("\nEscolha o tipo de forma:")
                print("1 - Círculo")
                print("2 - Retângulo")
                print("3 - Triângulo")
                forma = input("Digite o número correspondente à forma desejada: ")
                if forma == '1':
                    r = float(input("Digite o valor do raio: "))
                    formas.append(('circulo', (r,)))
                elif forma == '2':
                    a = float(input("Digite o valor do primeiro lado: "))
                    b = float(input("Digite o valor do segundo lado: "))
                    formas.append(('retangulo', (b, a)))
                elif forma == '3':
                    b = float(input("Digite o valor da base: "))
                    h = float(input("Digite o valor da altura: "))
                    formas.append(('triangulo', (b, h)))
                else:
                    print("Opção inválida!")

                continuar = input("\nDeseja adicionar mais formas? (s/n): ").lower() == 's'

            # Calcular todas as áreas fornecidas
            resultados = calcular_areas_multiplas(formas)
            print("\nResultados das áreas:")
            for i, res in enumerate(resultados, start=1):
                print(f"Área {i}: {res}m²")   

        elif opcao == '3':  # Calcular área com fator de escala
            print("\nEscolha o tipo de cálculo de área com fator de escala:")
            print("1 - Círculo")
            print("2 - Retângulo")
            print("3 - Triângulo")
            opcao = input("Digite o número correspondente à forma desejada: ")

            # Determinar parâmetros com base na forma escolhida
            if opcao == '1':  # Círculo
                r = float(input("Digite o valor do raio: "))
                parametros = (r,)
                forma = 'circulo'
            elif opcao == '2':  # Retângulo
                b = float(input("Digite o valor da base: "))
                h = float(input("Digite o valor da altura: "))
                parametros = (b, h)
                forma = 'retangulo'
            elif opcao == '3':  # Triângulo
                b = float(input("Digite o valor da base: "))
                h = float(input("Digite o valor da altura: "))
                parametros = (b, h)
                forma = 'triangulo'
            else:
                print("Forma inválida!")
                continue

            # Obter fator de escala
            fator_escala = float(input("Digite o fator de escala: "))

            # Calcular a área com o fator de escala
            resultado = calcular_area_com_escala(calcular_area, forma, fator_escala, *parametros)
            print(f"A área com fator de escala aplicado é: {resultado}m²")

        if opcao == '4':
            print("\nCálculo da Hipotenusa")
            a = float(input("Digite o valor do primeiro cateto: "))
            b = float(input("Digite o valor do segundo cateto: "))
            
            funcao_hipotenusa = calcular_hipotenusa(a, b)  # Retorna a closure
            resultado = funcao_hipotenusa()  # Executa a função interna
            print(f"A hipotenusa do triângulo é: {resultado:.1f}")

        elif opcao == '5':
            print("Saindo... Obrigado por usar a calculadora geométrica!")
            return
        
menu_start()