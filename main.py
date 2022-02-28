TXT = '''You cannot go anywhere without hearing a buzz of more or less confused and contradictory talk on this subject, nor can you fail to notice that, in one point at any rate, there is a very decided advance upon like discussions in former days. Nobody outside the agricultural interest now dares to say that education is a bad thing. If any representative of the once large and powerful party, which, in former days, proclaimed this opinion, still exists in the semi-fossil state, he keeps his thoughts to himself. In fact, there is a chorus of voices, almost distressing in their harmony, raised in favor of the doctrine that education is the great panacea for human troubles, and that, if the country is not shortly to go to the dogs, everybody must be educated. The politicians tell us, "You must educate the masses because they are going to be masters." The clergy join in the cry for education, for they affirm that the people are drifting away from church and chapel into the broadest infidelity. The manufacturers and the capitalists swell the chorus lustily. They declare that ignorance makes bad workmen; that England will soon be unable to turn out cotton goods, or steam engines, cheaper than other people; and then, Ichabod! Ichabod! the glory will be departed from us. And a few voices are lifted up in favor of the doctrine that the masses should be educated because they are men and women with unlimited capacities of being, doing, and suffering, and that it is as true now, as it ever was, that the people perish for lack of knowledge. '''
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
