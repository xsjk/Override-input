FLAG = False
import sys

if len(sys.argv)==1:
    input('请将文本文件拖动到此文件上运行')
    exit()
try:
    with open(sys.argv[1],encoding='utf-8') as f:
    	TXT = f.read().strip()
except:
    input("打开文件失败")
    exit()
else:
    print("打开文件成功")
    print(TXT)

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
