import csv
from cryptography.fernet import Fernet
from pyperclip import copy
from sys import exit
import os


arqv = './passwords/passwords.csv'
cabeca = ['site', 'user', 'senha']


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key


master_password = 'Lacerda7*'
master_key = load_key() + master_password.encode()
fer = Fernet(master_key)





def create_dir():
    path = '.\passwords'
    if not os.path.isdir(path):
        os.mkdir(path)
        with open(arqv, 'w')


def check_master_password(master_key):
    for e in range(4):
        senha = input('Qual a senha mestre?\n')
        if e == 3:
            exit("Tentativas excedidas\nFechando o programa")
        elif senha == master_key:
            break


def write_passwords():
    with open(arqv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=cabeca)
        passwords = add_password()
        for password in passwords:
            writer.writerow(password)


def add_password():
    passwords = []
    while True:
        site = input('qual o site que vc quer adicionar?\n').lower()
        user = input('qual o user desse site?\n')
        senha = input('qual a senha desse user?\n')
        dict = {cabeca[0]: f'{site}', cabeca[1]: f'{user}', cabeca[2]: f'{str(fer.encrypt(senha.encode()))}'}
        passwords.append(dict)
        c = input("Quer adicionar outra senha? (s/n)\n").lower()
        if c == 'n':
            break
    return passwords


def view_passwords():
    with open(arqv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=',', fieldnames=cabeca)
        reader.__next__()
        rows = list(reader)
        for row in rows:
            print(row['site'])
        conta = input('qual conta vc quer ver?\n')
        for row in rows:
            if row['site'] == conta:
                user = row['user'].strip()
                senha = row['senha'].strip()
                copy(senha)
                print(f'User: {user}')
                print(f'Senha: {senha}')
