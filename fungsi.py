print('haloo')

def selamat_datang():
    print('haloo selamat datang')

selamat_datang()

def greetings(nama, waktu):
    print(f'hello {nama} selamat {waktu}')
    print(f'apakah {nama} sudah datang {waktu} ini?')

#positional parameter
greetings('ilham', 'siang')
greetings('andi', 'malam')
greetings('dinda', 'siang')

greetings(waktu="malam", nama="danu") #named parameter

