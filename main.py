TXT = '''The traditional culture, which is, of course, mainly literary, is behaving like a state whose power is rapidly declining – standing on its precarious dignity, spending far too much energy on Alexandrine intricacies, occasionally letting fly in fits of aggressive pique quite beyond its means, too much on the defensive to show any generous imagination to the forces which must inevitably reshape it. Whereas the scientific culture is expansive, not restrictive, confident at the roots, the more confident after its bout of Oppenheimerian self-criticism, certain that history is on its side, impatient, intolerant, creative rather than critical, good- natured and brash. Neither culture knows the virtues of the other; often it seems they deliberately do not want to know. The resentment which the traditional culture feels for the scientific is shaded with fear; from the other side, the resentment is not shaded so much as brimming with irritation. When scientists are faced with an expression of the traditional culture, it tends (to borrow Mr William Cooper’s eloquent phrase) to make their feet ache. It does not need saying that generalizations of this kind are bound to look silly at the edges. There are a good many scientists indistinguishable from literary persons, and vice versa. Even the stereotype generalizations about scientists are misleading without some sort of detail – e.g. the generalizations that scientists as a group stand on the political Left. This is only partly true. A very high proportion of engineers is almost as conservative as doctors; of pure scientists, the same would apply to chemists. It is only among physicists and biologists that one finds the Left in strength. If one compared the whole body of scientists with their opposite numbers of the traditional culture (writers, academics, and so on), the total result might be a few per cent more towards the Left wing, but not more than that. Nevertheless, as a first approximation, the scientific culture is real enough and so is its difference from the traditional. For anyone like myself, by education a scientist, by calling a writer, at one time moving between groups of scientists and writers in the same evening, the difference has seemed dramatic.'''
FLAG = False

import keyboard

def wait(key):
    keyboard.wait(key)
    while keyboard.is_pressed(key):
        pass

j = 0

def prev_word():
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

def prev_sentence():
    global j
    if j == 0:
        return

    j_ = TXT.rfind('.',0,j-2) 
    if j_==-1:
        keyboard.send('end')
        keyboard.write('\b'*(j))
        j = 0
    else:
        keyboard.send('end')
        keyboard.write('\b'*(j-j_-1))
        j = j_+1


def next_word():
    global j
    if j<len(TXT):
        j_ = TXT.find(' ',j+1)
        if j_==-1:
            keyboard.write(TXT[j:])
            j = len(TXT)
        else:
            keyboard.write(TXT[j:j_])
            j = j_

def next_sentence():
    global j
    if j<len(TXT):
        j_ = TXT.find('.',j+1)
        if j_==-1:
            keyboard.write(TXT[j:])
            j = len(TXT)
        else:
            keyboard.write(TXT[j:j_+1])
            j = j_+1
    
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
    global j
    keyboard.write(TXT[j:])
    j = len(TXT)


def switch():
    global FLAG
    FLAG = not FLAG

def reset():
    global j
    j = 0
    keyboard.write(len(TXT)*'\b')    

keyboard.add_hotkey('ctrl+m',switch)
keyboard.add_hotkey('ctrl+b',reset)
keyboard.add_hotkey('ctrl+v',type_all)
keyboard.add_hotkey('ctrl+left',prev_word)
keyboard.add_hotkey('ctrl+shift+left',prev_sentence)
keyboard.add_hotkey('ctrl+right',next_word)
keyboard.add_hotkey('ctrl+shift+right',next_sentence)
keyboard.hook(callback)
keyboard.wait()
