import os 

lista = []
 
while True:
    resposta = input('Selecione uma opção: \n[i]nserir [a]pagar [l]istar\n').lower()

    if resposta == 'i':
        os.system('cls')
        print('o que deseja adicionar ?') 
        lista.append(input().capitalize())
        print('Item adicionado!')
        
    elif resposta == 'a':
        os.system('cls')     
        try:
            print('O que deseja remover ?')
            lista.remove(input().capitalize())
            print('Item removido!')
        except:
            print('Não foi possível apagar este item, verifique a lista novamente.')

    elif resposta == 'l':
        os.system('cls')    
        try:
            os.system('cls')
            len(lista) >= 1
            for item in lista:
                print(item)
        except:
            len(lista) == 0
            print('Não há o que listar')
                
    else: print('Opção inválida, tente novamente.') 

