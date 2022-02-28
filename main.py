TXT = '''Suppose it were perfectly certain that the life and fortune of every one of us would, one day or other, depend upon his winning or losing a game of chess. Don't you think that we should all consider it to be a primary duty to learn at least the names and the moves of the pieces; to have a notion of a gambit, and a keen eye for all the means of giving and getting out of check? Do you not think that we should look with a disapprobation amounting to scorn, upon the father who allowed his son, or the state which allowed its members, to grow up without knowing a pawn from a knight? Yet it is a very plain and elementary truth, that the life, the fortune, and the happiness of every one of us, and, more or less, of those who are connected with us, do depend upon our knowing something of the rules of a game infinitely more difficult and complicated than chess. It is a game which has been played for untold ages, every man and woman of us being one of the two players in a game of his or her own. The chessboard is the world, the pieces are the phenomena of the universe, the rules of the game are what we call the laws of Nature. The player on the other side is hidden from us. We know that his play is always fair, just, and patient. But also we know, to our cost, that he never overlooks a mistake, or makes the smallest allowance for ignorance. To the man who plays well, the highest stakes are paid, with that sort of overflowing generosity with which the strong shows delight in strength. And one who plays ill is checkmated—without haste, but without remorse.'''

FLAG = False

import keyboard

def wait(key):
    keyboard.wait(key)
    while keyboard.is_pressed(key):
        pass

j = 0

def prev():
    global j
    if j == 0:
        return

    j_ = TXT.rfind(' ',0,j)
    if j_==-1:
        j = 0
    else:
        keyboard.send('end')
        keyboard.write('\b'*(j-j_))
        j = j_


def next():
    global j
    if j<len(TXT):
        j_ = TXT.find(' ',j+1)
        if j_==-1:
            keyboard.write(TXT[j:])
            j = len(TXT)
        else:
            keyboard.write(TXT[j:j_])
            j = j_

    
def callback(e):
    global j
    if FLAG:
        if e.event_type=='down' and (len(e.name)==1 or e.name=='space'):
            keyboard.write('\b'+TXT[j])
            j+=1
        elif e.event_type=='down' and e.name=='backspace':
            if j>0:
                j-=1
            
    print('callback:',e.event_type,e.name,e.scan_code)

def type_all():
    keyboard.write(TXT)


def switch():
    global FLAG
    FLAG = not FLAG

def reset():
    global j
    j = 0

keyboard.add_hotkey('ctrl+m',switch)
keyboard.add_hotkey('ctrl+b',reset)
keyboard.add_hotkey('ctrl+shift+v',type_all)
keyboard.add_hotkey('ctrl+left',prev)
keyboard.add_hotkey('ctrl+right',next)
keyboard.hook(callback)
keyboard.wait()
