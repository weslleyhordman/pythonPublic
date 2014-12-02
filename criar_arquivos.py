import os
limpa = lambda: os.system('cls')

def read(msg):  # o progragrama vai ler o texto digitado pelo usuário
    global w
    arquivo = open(w + '.txt', 'w')
    for linha in msg:
        arquivo.write('%s' %linha)
    arquivo.close()

def write(msg):  # o programa vai escrever na tela o texto digitado pelo usuário
    with open(msg) as r:
        print(r.read())

while True:
    u = input('\n\nW para criar um arquivo. \nR para ler um arquivo. \nS para sair.\n\nOpção: ')
    d = u.lower()
    limpa()
    if d == 'w':
        ss = ''
        print('\nDigite o texto: (digite "__fim" para finalizar o texto)')
        print('\n###########################################################\n')
        while True:
            s = input('')
            if s != '__fim':
                ss = ss + '\n' + s
            else:
                print('\n###########################################################\n')
                break
        w = input('\nDigite um nome para o arquivo: ')
        read(ss)
        limpa()
    elif d == 'r':
        r = input('\nDigite o nome do arquivo: ')
        print('\n###########################################################')
        write(r + '.txt')
        print('\n###########################################################')
            
    elif d == 's':
        break
