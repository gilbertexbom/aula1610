# Sistema que verifica se um número informado é par ou impar

# Apresentação

print('\n\t\t\t -- Verificador de Núm. Par ou Impar -- \n\n')

# Entrada
num = int(input('Informe um número: '))

# Processamento e saída

if num % 2 == 0:
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')

