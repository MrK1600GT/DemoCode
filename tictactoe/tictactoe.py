# encoding: UTF-8
import re
import random

def main():
    spiel_activ = True
    spielfeld = [' ','1','2','3','4','5','6','7','8','9']
    
    sp1 = eingabe_sp("1")
    sp2 = eingabe_sp("2")
    
    if sp1['Stein'] == 'X': 
        sp2['Stein'] = 'O'
    else:
        sp2['Stein'] = 'X'
    
    print('{}, Du spielst mit Stein {}'.format(sp2['Name'], sp2['Stein']))
    
    select = random.randrange(1,3)
    
    while spiel_activ:
        spielfeld_ausgeben(spielfeld)
        if select == 1:
            zug = spieler_zug(sp1)
        else:
            zug = spieler_zug(sp2)
        
        if re.search(r'^[1-9]$', zug):
            if re.search(r'^[1-9]$', spielfeld[int(zug)]): 
                if select == 1:
                    zug_setzen(spielfeld, zug, sp1)
                    result = check_result(spielfeld, sp1)
                    select = 2
                else:
                    zug_setzen(spielfeld, zug, sp2)
                    result = check_result(spielfeld, sp2)
                    select = 1
            else:
                print('Das Feld ist schon besetzt!')
        else:
            spiel_ende()
            
        if result != None:
            spielfeld_ausgeben(spielfeld)
            print(result)
            print('\n\n')
            break
    
    while True:
        ende = input('Wollen Sie nochmals spielen? (J/N): ')
        if re.search(r'^[jJ]$', ende):
            main()
            
        elif re.search(r'^[nN]$', ende):
            spiel_ende()
                
            
def eingabe_sp(n):
    sp ={}
    while True:
        sp['Name'] = input('Bitte Name für Spieler {} eingeben: '.format(n))
        if sp['Name'].strip() != '':
            if str(n) == '1':
                while True:
                    sp['Stein'] = input('Bitte Stein auswählen "X" oder "O": ').upper()
                    if re.search(r'[XO]',sp['Stein'].strip()):
                        return sp
            else:
                return sp       
            

def spielfeld_ausgeben(spielfeld):
    print('\n\t\t{}|{}|{}'.format(spielfeld[1],spielfeld[2],spielfeld[3]))
    print('\t\t-----')
    print('\t\t{}|{}|{}'.format(spielfeld[4],spielfeld[5],spielfeld[6]))
    print('\t\t-----')
    print('\t\t{}|{}|{}\n'.format(spielfeld[7],spielfeld[8],spielfeld[9]))

def spieler_zug(sp):
    while True:
        zug = input("{} mit Stein {} ist am Zug (1-9) (Beenden mit 'Q': ".format(sp['Name'],sp['Stein']))
        if re.search(r'^[1-9qQ]$',zug):
            return zug

def spiel_ende():
    exit()


def zug_setzen(spielfeld, zug, sp):
    spielfeld[int(zug)] = sp['Stein']
    

def check_result(spielfeld, sp):
    if spielfeld[1] == sp['Stein'] and spielfeld[2] == sp['Stein'] and spielfeld[3] == sp['Stein'] or \
    spielfeld[4] == sp['Stein'] and spielfeld[5] == sp['Stein'] and spielfeld[6] == sp['Stein'] or \
    spielfeld[7] == sp['Stein'] and spielfeld[8] == sp['Stein'] and spielfeld[9] == sp['Stein'] or \
    spielfeld[1] == sp['Stein'] and spielfeld[4] == sp['Stein'] and spielfeld[7] == sp['Stein'] or \
    spielfeld[2] == sp['Stein'] and spielfeld[5] == sp['Stein'] and spielfeld[8] == sp['Stein'] or \
    spielfeld[3] == sp['Stein'] and spielfeld[6] == sp['Stein'] and spielfeld[9] == sp['Stein'] or \
    spielfeld[1] == sp['Stein'] and spielfeld[5] == sp['Stein'] and spielfeld[9] == sp['Stein'] or \
    spielfeld[3] == sp['Stein'] and spielfeld[5] == sp['Stein'] and spielfeld[7] == sp['Stein']:
        return '{} hat gewonnen, Gratulation!'.format(sp['Name'])
    else:
        ende_indikator = True
        for i in spielfeld:
            if i.isnumeric():
                ende_indikator = False
                break
        if ende_indikator:
            return 'Das Spiel ist unentschieden ausgegangen.'


if __name__ == '__main__':
    print('Willkommen bei Tic Tac Toe!')

    try:
        main()
    except KeyboardInterrupt:
        pass