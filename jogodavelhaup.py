import random

global k
global toggle
global setado_direto_AI
global setado_direto_user
global letra_AI
global letra_user
global coo
global entrada

while True:
    entrada = input('Input command:')
    if (entrada == 'start easy easy') or (entrada == 'start easy medium') or (entrada == 'start medium medium') or (
            entrada == 'start medium easy'):
        setado_direto_AI = True
        setado_direto_user = False
        letra_AI = 'X'
        toggle = 1
        break
    elif (entrada == 'start easy user') or (entrada == 'start medium user'):
        toggle = 1
        letra_AI = 'X'
        letra_user = 'O'
        setado_direto_AI = False
        setado_direto_user = False
        break
    elif (entrada == 'start user easy') or (entrada == 'start user medium'):
        toggle = 0
        letra_AI = 'O'
        letra_user = 'X'
        setado_direto_AI = False
        setado_direto_user = False
        break
    elif entrada == 'start user user':
        setado_direto_user = True
        setado_direto_AI = False
        letra_user = 'X'
        toggle = 0
        break
    elif entrada == 'exit':
        raise SystemExit
    else:
        print('Bad parameters!')
        continue

k = "_________"
print('---------')
print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
print('---------')
conta = 0

while True:
    while toggle == 1 or setado_direto_AI == True:

        if ('start medium' in entrada and conta % 2 == 0) or (entrada[-1] == 'm' and conta % 2 == 1):
            al = k[0] + ' ' + k[1] + ' ' + k[2]
            bl = k[3] + ' ' + k[4] + ' ' + k[5]
            cl = k[6] + ' ' + k[7] + ' ' + k[8]
            dl = k[0] + ' ' + k[3] + ' ' + k[6]
            el = k[1] + ' ' + k[4] + ' ' + k[7]
            fl = k[2] + ' ' + k[5] + ' ' + k[8]
            gl = k[0] + ' ' + k[4] + ' ' + k[8]
            hl = k[2] + ' ' + k[4] + ' ' + k[6]
            if (al == '_ X X') or (dl == '_ X X') or (gl == '_ X X') or (al == '_ O O') or (dl == '_ O O') or (
                    gl == '_ O O'):
                ran = 0
                listao = list(k)
                listao[ran] = letra_AI
                k = ''.join(listao)
                print('Making move level "medium"')
                print('---------')
                print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
                print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
                print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
                print('---------')
                toggle = 0
                easy_random = 0
                conta = conta + 1
                if letra_AI == 'X' and setado_direto_AI == True:
                    letra_AI = 'O'
                if letra_AI == 'O' and setado_direto_AI == True:
                    letra_AI = 'X'

            elif (al == 'X X _') or (fl == '_ X X') or (hl == '_ X X') or (al == 'O O _') or (fl == '_ O O') or (
                    hl == '_ O O'):
                ran = 2
                listao = list(k)
                listao[ran] = letra_AI
                k = ''.join(listao)
                print('Making move level "medium"')
                print('---------')
                print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
                print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
                print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
                print('---------')
                toggle = 0
                easy_random = 0
                conta = conta + 1
                if letra_AI == 'X' and setado_direto_AI == True:
                    letra_AI = 'O'

                if letra_AI == 'O' and setado_direto_AI == True:
                    letra_AI = 'X'

            elif (cl == '_ X X') or (dl == 'X X _') or (hl == 'X X _') or (cl == '_ O O') or (dl == 'O O _') or (
                    hl == 'O O _'):
                ran = 6
                listao = list(k)
                listao[ran] = letra_AI
                k = ''.join(listao)
                print('Making move level "medium"')
                print('---------')
                print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
                print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
                print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
                print('---------')
                toggle = 0
                easy_random = 0
                conta = conta + 1
                if letra_AI == 'X' and setado_direto_AI == True:
                    letra_AI = 'O'

                if letra_AI == 'O' and setado_direto_AI == True:
                    letra_AI = 'X'

            elif (cl == 'X X _') or (fl == 'X X _') or (gl == 'X X _') or (cl == 'O O _') or (fl == 'O O _') or (
                    gl == 'O O _'):
                ran = 8
                listao = list(k)
                listao[ran] = letra_AI
                k = ''.join(listao)
                print('Making move level "medium"')
                print('---------')
                print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
                print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
                print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
                print('---------')
                toggle = 0
                easy_random = 0
                conta = conta + 1
                if letra_AI == 'X' and setado_direto_AI == True:
                    letra_AI = 'O'

                if letra_AI == 'O' and setado_direto_AI == True:
                    letra_AI = 'X'

            else:
                easy_random = 1

        while ('easy' in entrada or easy_random == 1):
            ran = int(random.randint(0, 8))
            if (k[ran] == ' ' or k[ran] == '_'):
                break

        # ran = int( random.randint(0,8))
        if ('easy' in entrada or easy_random == 1):

            listao = list(k)
            listao[ran] = letra_AI
            k = ''.join(listao)
            if ('start medium' in entrada and conta % 2 == 0) or (entrada[-1] == 'm' and conta % 2 == 1):
                print('Making move level "medium"')
            else:
                print('Making move level "easy"')

            print('---------')
            print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
            print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
            print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
            print('---------')
            toggle = 0
            conta = conta + 1
        if letra_AI == 'X' and setado_direto_AI == True:
            letra_AI = 'O'
            break
        if letra_AI == 'O' and setado_direto_AI == True:
            letra_AI = 'X'
            break

    countempty = k.count('_')
    if countempty == 0:
        print("Draw")
        break
    if setado_direto_AI == False:
        coo = input('Enter the coordinates:')
        if not (coo[0].isdigit() or coo[2].isdigit()):
            print('You should enter numbers!')
            continue

    if setado_direto_AI == False and len(coo) > 0 and len(coo) < 4 and int(coo[0]) > 0 and int(coo[0]) < 4 and int(
            coo[2]) > 0 and int(coo[2]) < 4 and setado_direto_AI == False:
        pos = (int(coo[0]) - 1) + (9 - 3 * int(coo[2]))
        if k[pos] == '' or k[pos] == '_':
            lista = list(k)
            if toggle == 0 or setado_direto_user == True:
                lista[pos] = letra_user
            if setado_direto_user == False:
                toggle = 1

            k = ''.join(lista)
            print('---------')
            print('|' + ' ' + k[0] + ' ' + k[1] + ' ' + k[2] + ' ' + '|')
            print('|' + ' ' + k[3] + ' ' + k[4] + ' ' + k[5] + ' ' + '|')
            print('|' + ' ' + k[6] + ' ' + k[7] + ' ' + k[8] + ' ' + '|')
            print('---------')
            conta = conta + 1

        else:
            print('This cell is occupied! Choose another one!')
            continue

    if setado_direto_AI == False and (len(coo) > 0 and len(coo) < 4) and (
            int(coo[0]) < 1 or int(coo[0]) > 3 or int(coo[2]) < 1 or int(coo[2]) > 3):
        print('Coordinates should be from 1 to 3!')
        continue

    al = k[0] + ' ' + k[1] + ' ' + k[2]
    bl = k[3] + ' ' + k[4] + ' ' + k[5]
    cl = k[6] + ' ' + k[7] + ' ' + k[8]
    dl = k[0] + ' ' + k[3] + ' ' + k[6]
    el = k[1] + ' ' + k[4] + ' ' + k[7]
    fl = k[2] + ' ' + k[5] + ' ' + k[8]
    gl = k[0] + ' ' + k[4] + ' ' + k[8]
    hl = k[2] + ' ' + k[4] + ' ' + k[6]

    #countx = k.count('XXX')
    #counto = k.count('OOO')
    #countx1 = k.count('X')
    #counto1 = k.count('O')
    countempty = k.count('_')
    #difcount = countx1 - counto1
    #alfa = 0
    #beta = 0

    # if (countx > 0) and (counto > 0):
    #    print("Impossible")
    #    break
    if ((al == 'X X X') or (bl == 'X X X') or (cl == 'X X X')):
        print("X wins")
        break
    if ((dl == 'X X X') or (el == 'X X X') or (fl == 'X X X')):
        # alfa = 1
        print("X wins")
        break

    if ((gl == 'X X X') or (hl == 'X X X')):
        print("X wins")
        break

    if ((al == 'O O O') or (bl == 'O O O') or (cl == 'O O O')):
        print("O wins")
        break

    if ((dl == 'O O O') or (el == 'O O O') or (fl == 'O O O')):
        # beta = 1
        print("O wins")
        break

    if ((gl == 'O O O') or (hl == 'O O O')):
        print("O wins")
        break

    #if alfa == 1 and beta == 1:
    #    print("Impossible")
    #    break
    #elif alfa == 1 and beta == 0:
    #    print("X wins")
    #    break
    #elif alfa == 0 and beta == 1:
     #   print("O wins")
     #   break

    # if ((difcount > 1) or ( difcount < -1)) :
    #    print("Impossible")
    #    break

    if countempty > 0:
        # print("Game not finished")
        # break
        if setado_direto_user == True and letra_user == 'X':
            letra_user = 'O'
            continue
        if setado_direto_user == True and letra_user == 'O':
            letra_user = 'X'
            continue
        pass
    else:
        print("Draw")
        break