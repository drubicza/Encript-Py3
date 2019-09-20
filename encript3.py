import os
import click
import base64
import marshal
from uncompyle6 import main

class Com:

    def __init__(self, fil, jum):
        self.file = fil
        self.cout = 0
        self.jml = jum
        self.mars(open(fil, 'r').read())

    def mars(self, strg):
        x = compile(strg, '<script>', 'exec')
        xx = marshal.dumps(x)
        xxx = f"#Brutal Encript\n#By Zen Ezz\n\nimport marshal\nexec(marshal.loads({xx}))"
        if self.cout == self.jml:
            with open(self.file.replace('.py', '_ZenCript.py'), 'w') as (com):
                com.write(xxx)
            print(f"[+] File tersimpan: {self.file.replace('.py', '_ZenCript.py')}")
            return True
        self.bes(xxx)

    def bes(self, strg):
        en = base64.b64encode(bytes(strg, 'utf-8'))
        de = f"#Brutal Encript By Zen!!\n\nimport base64\nexec(base64.b64decode({en}).decode('utf-8','ignore'))"
        self.cout += 1
        self.mars(de)


os.system('clear')
print('\x1b[0;36m          ___  ____ _  _ ___ ____ ____ ____ _ ___  ___\n          |__] |__/ |  |  |  |___ |    |__/ | |__]  |\n\x1b[1;37m          |__] |  \\ |__|  |  |___ |___ |  \\ | |     |\n\x1b[0;32m[\x1b[0;31m+\x1b[0;32m]\x1b[0;37m════════════════════════════════════════════════════════════\x1b[0;32m[\x1b[0;31m+\x1b[0;32m]\n\x1b[0;36m      Python3 Brutal Encript | \x1b[1;33mCoded By Zen Ezz |\x1b[0;34m Cr 2k19\n\x1b[0;32m[\x1b[0;31m+\x1b[0;32m]\x1b[0;37m════════════════════════════════════════════════════════════\x1b[0;32m[\x1b[0;31m+\x1b[0;32m]')
try:
    ofile = input('\x1b[0;31m[\x1b[0;37m?\x1b[0;31m]\x1b[0;37m Alamat File: ')
    juml = int(input('\x1b[0;31m[\x1b[0;37m?\x1b[0;31m]\x1b[0;37m Jumlah Encript: '))
    if juml > 50:
        click.pause('\x1b[0;31m[\x1b[0;31m!\x1b[0;37m]\x1b[0;31m Anda Memasukan jumlah lebih dari 50, Itu Bisa Menyebabkan Size File Menjadi Besar! [ENTER]')
    Com(ofile, juml)
    pil = input('\x1b[0;31m[\x1b[0;37m?\x1b[0;31m]\x1b[0;37m Encript ke Pyc (y/n) ')
    if pil.lower() == 'y':
        main.compile_file(ofile.replace('.py', '_ZenCript.py'))
        print('\x1b[0;31m[\x1b[0;37m!\x1b[0;31m]\x1b[0;37m Done Gan')
    else:
        print('\x1b[0;31m[\x1b[0;37m!\x1b[0;31m]\x1b[0;37m Done Gan')
except KeyboardInterrupt:
    print('[Key Interrupt]')
except Exception as F:
    try:
        print(f"[Err] {str(F)}")
    finally:
        F = None
        del F
