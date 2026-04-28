import os

for f in os.listdir('.'):
    if(os.path.isfile(f)):
        o = open(os.path.join('reconst', f), 'w')
        print(os.path.join('reconst', f))
        o.close()