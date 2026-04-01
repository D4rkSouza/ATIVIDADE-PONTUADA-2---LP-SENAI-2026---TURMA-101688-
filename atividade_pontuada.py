import os
os.system('cls')

#Array dos dados informados pelo cliente
exames = []
exames_valor = []

print('\n-')
cod_exame = ()
valor_exame = ()
total_s_desconto = sum(exames_valor)
desconto = ()

#Tabela de seleção dos exames
while True:
    print('''
         ========= TABELA DE PREÇOS =========
        CÓDIGO |     TIPO DE EXAME     | VALOR
          1    | HEMOGRAMA COMPLETO    | R$600,00
          2    | RAIO-X                | R$500,00
          3    | ULTRASSONOGRAFIA      | R$450,00
          4    | ELETROCARDIOGRAMA     | R$650,00
          5    | TOMOGRAFIA            | R$800,00
          6    | RESSONÂNCIA MAGNÉTICA | R$900,00
          7    | EXAME DE GLICOSE      | R$700,00
          
    OU PRESSIONE 0 PARA ENCERRAR O AGENDAMENTO E EXIBIR OS RESULTADOS
      ''')
    cod_exame = int(input("Digite o código do exame: "))
    
    exame = 0
    valor_exame = 0
    
#Onde o código será convertido para o exame
    match cod_exame:
        case 0:
            break
        
        case 1:
            exame = ('HEMOGRAMA COMPLETO')
            valor_exame = 600

        case 2:
            exame = ('RAIO-X')
            valor_exame = 500

        case 3:
            exame = ('ULTRASSONOGRAFIA')
            valor_exame = 450 

        case 4:
            exame = ('ELETROCARDIOGRAMA')
            valor_exame = 650

        case 5:
            exame = ('TOMOGRAFIA')
            valor_exame = 800
            
        case 6:
            exame = ('RESSONÂNCIA MAGNÉTICA')
            valor_exame = 900
            
        case 7:
            exame = ('EXAME DE GLICOSE')
            valor_exame = 700
            
        case _:
            print('OPÇÃO INVÁLIDA, POR FAVOR SELECIONE UMA OPÇÃO DISPONÍVEL')
            continue #Caso a opção seja inválida não mostrar valor
        
#Enviando opção selecionada para o Array e selecionando se quer mais opções            
    exames.append(exame)    
    exames_valor.append(valor_exame) 
           
    mais_exame = str(input('''Deseja Agendar Mais Exames? 
    Selecione com s ou n ''')).lower()

    if mais_exame == 's':
        print('Escolha o Novo Exame')
    elif mais_exame == 'n':
        break

#Aqui soma o valor total e pede a forma de pagamento
total_s_desconto = sum(exames_valor)

print('Selecione a Forma de Pagamento')
print('''
1 | CARTÃO DE CRÉDITO |  ACRÉSCIMO DE 8% SOBRE O VALOR TOTAL
2 | CONVÊNIO          |  DESCONTO DE 15% SOBRE O VALOR TOTAL
3 | PARTICULAR        |  SEM DESCONTO OU ACRÉSCIMO SOBRE O VALOR TOTAL
''') 
#Cálculo do desconto com base na opção de pagamento
while True:
    opcao_pagamento = int(input('Selecione uma Opção:  '))
    match opcao_pagamento:
        case 1:
            opcao_pagamento = ('CARTÃO DE CRÉDITO') 
            desconto = total_s_desconto * 0.08
            total_c_desconto = desconto + total_s_desconto
            break
        case 2:
            opcao_pagamento = ('CONVÊNIO')
            desconto = total_s_desconto * 0.15
            total_c_desconto = total_s_desconto - desconto
            break
        case 3:
            opcao_pagamento = ('PARTICULAR')
            desconto = 0
            total_c_desconto = (total_s_desconto)
            break
        case _:
            print('Inválido. Selecione um Método para Pagamento')

#Exibição dos resultados
print('\n-')
print(f'EXAMES: {exames}')
print(f'VALOR TOTAL DOS EXAMES R${total_s_desconto},00')
print(f'FORMA DE PAGAMENTO {opcao_pagamento}')
print(f'VALOR DA FORMA DE PAGAMENTO R${desconto}0')
print(f'VALOR TOTAL COM FORMA DE PAGAMENTO: R${total_c_desconto}')