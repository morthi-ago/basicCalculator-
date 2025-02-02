def repetidorDeDivisao(numeroUm, numeroDois):
    numeroDois = int(input('Digite outro numero para dividir\n'))
    print(numeroUm / numeroDois)

numeroUm = int(input('Digite um numero\n'))
numeroDois = int(input('Digite outro numero\n'))

operacao = input('Que operacao matematica deseja fazer ?\n')

if operacao == '*':
    print(numeroUm * numeroDois)
elif operacao == '/':
    if numeroDois == 0:
        print("Nao pode dividir por zero!")
        repetidorDeDivisao(numeroUm, numeroDois)
    else:
        print(numeroUm / numeroDois) 
elif operacao == '+':
    print(numeroUm + numeroDois) 
else:
    print(numeroUm - numeroDois)

print("Obrigado por usar o codigo :D")
    