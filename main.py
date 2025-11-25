# Integrantes:Thomas Frentzel , Renan Belem Biviati

# aqui vai ocorrer a importaçã da biblioteca que irá gerar a key e o nounce
import random


def descriptografia(palavra, remove):
    tamanho_remover = len(remove)

    palavra_tamanho = len(palavra)

    while True:

        position_remove = palavra.find(remove)

        if position_remove != -1:

            start_palavra = palavra[0:position_remove]

            end_palavra = palavra[position_remove + tamanho_remover:palavra_tamanho]

            palavra = start_palavra + end_palavra

        else:

            break

    return palavra


def funcao_de_bob(phrase):
    chave_de_bob = ""

    for letter in phrase:

        if letter in "poiuytrewqPOIUYTREWQ":
            chave_de_bob = chave_de_bob + "%"

        if letter in "çlkjhgfdsaÇLKJHGFDSA":
            chave_de_bob = chave_de_bob + "*"

        if letter in "mnbvcxzMNBVCXZ":
            chave_de_bob = chave_de_bob + "#"

        if letter in "0987654321":
            chave_de_bob = chave_de_bob + "@"

        if letter in "!@#$%¨&*()":

            chave_de_bob = chave_de_bob + "&"

        else:

            chave_de_bob = chave_de_bob + letter

    return chave_de_bob


def alice_chave_mudanca(bobnouce_bobchave):
    new_key = ""

    for new_letra_por_letra in bobnouce_bobchave:

        if new_letra_por_letra in "poiuytrewqPOIUYTREWQ":
            new_key = new_key + "%"

        if new_letra_por_letra in "çlkjhgfdsaÇLKJHGFDSA":
            new_key = new_key + "*"

        if new_letra_por_letra in "mnbvcxzMNBVCXZ":
            new_key = new_key + "#"

        if new_letra_por_letra in "0987654321":
            new_key = new_key + "@"

        if new_letra_por_letra in "!@#$%¨&*()":

            new_key = new_key + "&"

        else:

            new_key = new_key + new_letra_por_letra

    return new_key


menu = ''

K_sessão = 0

new_nounce_alice = 0

K_alice_new = ''

while menu != '2':

    print("Sistema de criptografia")

    print("\t Presione enter para gerar a chave e o nounce")

    menu = input()

    if menu == '':

        menu_bob = ''

        while menu_bob != 3:

            print("1 - Gerar chave e o Nounce")

            menu_bob = input()

            if menu_bob == '1':

                from random import randint

                K_sessão = int(randint(0, 100000))

                print("Sua chave aleatória gerada é {}".format(K_sessão))

                K_bob = funcao_de_bob(input("Escreva a mensagem para Alice"))

                print("Seu Nounce é 'E24$%', ele será colocado junto com sua frase criptografada")

                print("Pressione Enter para enviar a mensagem para Alice e entrar no menu de Alice")

                menu_alice = input("Escreva o código gerado por Bob")

                menu_alice_int = int(menu_alice)

                print(K_sessão)

                if menu_alice_int == int(K_sessão):
                    print("menu ok")

                    nounce_de_bob = input(
                        "Digite o nounce de bob passado ao KDC para gerar a frase com a descodificação")

                    if nounce_de_bob == 'E24$%':
                        print("A frase de bob criptografada é{}".format(K_bob))

                        print("-------")
                        print("A frase descriptografada é")

                        palavras = K_bob

                        palavra_for_remove = ["@", "#", "%", "&", "*"]

                        for palavra in palavras:

                            finish = palavra

                            for remove in palavra_for_remove:
                                finish = descriptografia(finish, remove)

                            print(finish, end='')
                    else:
                        print("O nounce está incorreto")

                    break

                else:
                    print("sair")
            break

        print("\n")
        alice_para_bob = input("Pressione enter para gerar um novo nounce")
        nova_frase = alice_chave_mudanca(input("Escreva a mensagem para Bob"))
        print("a frase criptografada é")
        print(nova_frase)

        if alice_para_bob != '0':

            from random import randint

            novo_nounce = randint(0, 100000)

            print("Seu nounce é {}".format(novo_nounce))

            menu_bob = input("Pressione enter para entrar no menu de Bob e receber a mensagem")

            if menu_bob != '0':

                novo_nounce_alice = input("Digite o novo nounce gerado por Alice")

                if novo_nounce_alice == novo_nounce:

                    print(" a Frase desriptografada é ")
                    palavras = nova_frase

                    palavra_for_remove = ["@", "#", "%", "&", "*"]

                    for palavra in palavras:

                        finish = palavra

                        for remove in palavra_for_remove:
                            finish = descriptografia(palavra, remove)

                            print(finish, end='')

            else:
                print("incorreto")

        else:
            print("False")

        menu = input("Pressione enter")