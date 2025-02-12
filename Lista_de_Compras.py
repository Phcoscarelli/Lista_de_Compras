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
            for i, item in enumerate(lista):
                    print(i, item)
        except:
            len(lista) == 0
            print('Nada para listar')
                
    else: print('Opção invalida, tente novamente.') 

