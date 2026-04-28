from struct import *
import math

def entry():
    head = int(input("\n\nHeader length: "))/12
    act = math.floor(head)
    lim = math.ceil(head)
    index = int(input("Index length: "))
    bin = int(input("Binary file: "))

    if(bin == 0):
        fn = 'constant_match.bin'
    elif(bin == 1):
        fn = 'constant_player.bin'
    elif(bin == 2):
        fn = 'constant_team.bin'
        
    f = open(fn, 'rb')
    o = open('index.txt', 'w')
    lena = []
    for i in range(lim):
        o.write(str(unpack('<i', (f.read(4)))[0]))
        o.write(' - ')
        o.write(str(unpack('<i', (f.read(4)))[0]))
        o.write(' - ')
        o.write(str(unpack('<i', (f.read(4)))[0]))
        o.write('\n')
        
    o.close()
    f.seek(0)
    
    for i in range(lim):
        a = f.read(4)
        b = f.read(8)
        lena.append(unpack('<i', a)[0])
    
    f.seek(-4, 1)
    ind = f.read(index)
    
    ind = ind.replace(bytes('.o', 'utf-8'), bytes('', 'utf-8'))
    inda = unpack('%db' % len(ind), ind)
    i = 0
    j = 0
    fin = []
    fin.append('')
    for it in inda:
        if(it > 0):
            fin[j] = fin[j] + chr(inda[i])
        else:
            j = j + 1
            fin.append('')
        i = i+1

    while(fin[-1] == ''):
        fin.pop()
        
    for i in range(len(fin)):
        out = open(fin[i] + '.txt', 'w')
        for j in range(int(lena[i+1]/4)):
            b = f.read(4)
            p = unpack('<i', b)[0]
            if(p > 10000 or p < 0):
                p = round(unpack('<f', b)[0], 3)
            out.write(str(p) + '\n')
        out.close()
        
    ind = ''.join(ind.decode().split(".o "))
    
    print(lena)
    
    f.close()

entry()