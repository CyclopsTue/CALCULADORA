## Calculadora Python
## Criado pelo Near Shelby
## Pergunta para o  usuario qual o tipo de operação
## Pergunta o primeiro numero
## Pergunta o segundo numero
## Calculo desses 2 numeros
## Imprimi o resultado na tela

import os
os.system("clear")

print("""
\033[1;96m_____________________________________________________________________
\033[1;95m   _________    __    ________  ____    ___    ____  ____  ____  ___
  / ____/   |  / /   / ____/ / / / /   /   |  / __ \/ __ \/ __ \/   |
 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / / /_/ / /| |
/ /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ /_/ / /_/ / _, _/ ___ |
\____/_/  |_/_____/\____/\____/_____/_/  |_/_____/\____/_/ |_/_/  |_|
\033[1;96m_____________________________________________________________________

\033[1;95mCriador : Near Shelby
\033[1;96m_____________________________________________________________________""")

while True:
    operacao = input('\033[1;96mQual operação \033[1;95m(+,-,*,/) \033[1;96mvocê quer fazer ? ou  \033[1;95m\'n\' \033[1;96mpara sair? \033[1;95m$ ')
    if operacao == 'n' or operacao == 'N':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('\033[1;96mDigite o primeiro numero \033[1;95m$ '))
        num2 = int(input('\033[1;96mDigite o segundo numero  \033[1;95m$ '))
    else:
        print('\033[1;31mOperacao invalida')

    if operacao == '+':
        total = num1 + num2
        print(total)
    elif operacao == '-':
        total = num1 - num2
        print(total)
    elif operacao == '*':
        total = num1 * num2
        print(total)
    elif operacao == '/':
        total = num1 / num2
        print(total)
