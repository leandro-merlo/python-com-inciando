# coding: utf-8

import getpass
import os

must_exit = False

accounts_list = {
    "0001-02" : {
        "password": "123456",
        "name": "Fulando da Silva",
        "value": 100,
        "admin": False
    },
    "0002-02" : {
        "password": "123456",
        "name": "Cicrano da Silva",
        "value": 50,
        "admin": False
    },
    "1111-11" : {
        "password": "123456",
        "name": "Admin da Silva",
        "value": 1000,
        "admin": True
    }    
}

money_slips = {
    '2': 0,
    '5': 0,
    '10': 0,
    '20': 5,
    '50': 5,
    '100': 5
}

while not must_exit:
    print('***************************************')
    print('**   Caixa Eletrônico Really Shit    **')
    print('***************************************')

    account_typed = input("Digite sua conta: ")
    password_typed = getpass.getpass("Digite sua senha: ")

    if account_typed in accounts_list and accounts_list[account_typed]["password"] == password_typed:
        authenticated_account = accounts_list[account_typed]
        os.system('cls' if os.name == 'nt' else 'clear')

        print('***************************************')
        print('**   Caixa Eletrônico Really Shit    **')
        print('***************************************')
        print('1 - Saldo')
        print('2 - Saque')
        if authenticated_account['admin']:
            print('10 - Incluir cédulas')
        option_typed = input("Escolha uma das opções acima: ")
        if option_typed == '1':
            print('O saldo atual é: R$ %s' % authenticated_account['value'])
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            money_slips_user = {}
            value_int = int(value_typed)
            
            if value_int // 100 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100 
            
            if value_int // 50 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50 
            
            if value_int // 20 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20 
            
            if value_int // 10 and value_int // 10 <= money_slips['10']:
                money_slips_user['10'] = value_int // 10
                value_int = value_int - value_int // 10 * 10 
            
            if value_int // 5 and value_int // 5 <= money_slips['5']:
                money_slips_user['5'] = value_int // 5
                value_int = value_int - value_int // 5 * 5 
            
            if value_int // 2 and value_int // 2 <= money_slips['2']:
                money_slips_user['2'] = value_int // 2
                value_int = value_int - value_int // 2 * 2
            
            if value_int != 0:
                print('O caia não tem cédulas disponíveis para esse valor!')
            else:
                print('Pegue as notas: ')
                print(money_slips_user)
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                    
        elif option_typed == "10" and authenticated_account['admin']:
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')
            if money_bill_typed in money_slips:
                money_slips[money_bill_typed] += int(amount_typed)
                print(money_slips)
            else:
                print('Não pode inserir este tipo de cédula: %s' % money_bill_typed)

    else:
        print("Conta inválida")

    input("Digite <ENTER> para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')