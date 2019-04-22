# Alunos: 
# - aluno A: Rafael Henrique Belini Zanfolin, rafaelhbz@insper.edu.br
# - aluno B: João Pedro Farias Araujo, joaopfa2@al.insper.edu.br

import json
import random

with open('cenarios.json', 'r', encoding="utf-8-sig") as cenarios_file:
    cenarios_str = cenarios_file.read()
    cenarios_dict = json.loads(cenarios_str)

def carregar_cenarios():
    nome_cenario_atual = "inicio"
    return cenarios_dict, nome_cenario_atual


def main():
    
    import random

    
    hp_character = 30
    def_character = 0
    atk_character = 3
    
    hp_rato = 5
    def_rato = 0
    atk_rato = 2
    
    hp_inseto = 4
    def_inseto = 1
    atk_inseto = 3
    
    weapon = 0
    if weapon == 0:
        atk_character = 3
    elif weapon == 1:
        atk_character = 5
    elif weapon == 2:
        atk_character = 7
    
    
    pocao = 0
    gold_pouch = 0
    key = 0
    inventario = []
    
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual['descricao'])
              
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("suas opções: ")
            print()
            for k in opcoes:
                print("{0}: {1}".format(k, opcoes[k]))
                print()
            escolha = input("Faça a sua escolha, jovem gafanhoto: ")
        

            print('-'*len(cenario_atual['titulo']))
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if escolha == "alavanca":
                    if key > 0:
                        print("\n Você já obteve essas recompensas \n ")
                        for k,v in opcoes.items():
                            print("{0}:{1}".format(k,v))
                        escolha = input("Você deve escolher voltar para a biblioteca! \n ")
                        nome_cenario_atual = "biblioteca"
                    elif key == 0:
                        gold_pouch = gold_pouch + 10
                        inventario.append(gold_pouch)
                        key = key + 1
                        inventario.append(key)
                        pocao = pocao + 1
                        inventario.append(pocao)
                        atk_character = 5
                        print(" \n 10 gold coins foram adicionados à sua gold pouch, você recebeu uma chave, uma pocao e uma dagger \n ")
                        print("Agora o seu inventário possui {0} gold(s) , {1} chave(s) e {2} poco(es) e uma dagger\n ".format(gold_pouch,key,pocao,weapon))
                        print("O seu atk damage atual é {0}".format(atk_character))
                elif escolha == "usar pocao":
                    if pocao > 0:
                        if hp_character < 25:
                            pocao = pocao - 1
                            hp_character = hp_character + 5
                            print("Sua vida atual e {0} e voce tem {1} pocoes".format(hp_character,pocao))
                        else:
                            print("A sua vida atual é maior que 25, então você desperdiçou uma pocao")
                            pocao = pocao - 1
                            print("Sua vida atual e {0} e voce tem {1} poco(es)".format(hp_character,pocao))
                    else:
                        print("Você não tem pocoes")
                        
                elif escolha == "sala 202":
                    print(cenario_atual['titulo'])
                    print(cenario_atual['descricao'])
                    print('-'*len(cenario_atual['titulo']))
                    if hp_character <= 25:
                        hp_character = hp_character + 5
                        print("Você recuperou 5 de vida")
                        print("A sua vida atual é {0}".format(hp_character))
                    else:
                        print("A sua vida atual é {0}:".format(hp_character))
                        print("Como você tem 26 ou mais pontos de vida, a sua vida continua a mesma")
                    opcoes = cenario_atual['opcoes']
                    print()
                elif escolha == "segundo andar":
                    if key <= 0:
                        print("\n Você infelizmente não tem a chave, volte e procure mais recursos \n")
                        for k,v in opcoes.items():
                            print("{0}:{1}".format(k,v))
                        escolha = input("Você deve escolher voltar para o primeiro andar!\n")
                        nome_cenario_atual = "primeiro andar"
                    else:
                        print("Você possui a chave de acesso para o segundo andar andar")
                elif escolha == "investigar o local":
                    r2 = random.randint(1,2)
                    cenario_atual = cenarios[nome_cenario_atual]
                    print(cenario_atual['titulo'])
                    print('-'*len(cenario_atual['titulo']))
                    print(cenario_atual['descricao'])            
                    opcoes = cenario_atual['opcoes']
                    print()
                    if r2 == 1:
                        cenario_atual = cenarios["apareceu um rato"]
                        print(cenario_atual['titulo'])
                        print('-'*len(cenario_atual['titulo']))
                        print(cenario_atual['descricao'])            
                        opcoes = cenario_atual['opcoes']
                        print()
                        for k in opcoes:
                            print("{0}: {1}".format(k, opcoes[k]))
                            print()
                        escolha = input("o que vai fazer, jovem gafanhoto? ")
                        nome_cenario_atual = escolha
                    elif r2 == 2:
                        cenario_atual = cenarios["apareceu um inseto"]
                        print(cenario_atual['titulo'])
                        print('-'*len(cenario_atual['titulo']))
                        print(cenario_atual['descricao'])            
                        opcoes = cenario_atual['opcoes']
                        print()
                        for k in opcoes:
                            print("{0}: {1}".format(k, opcoes[k]))
                            print()
                        escolha = input("o que vai fazer, jovem gafanhoto? ")
                        nome_cenario_atual = escolha
                elif escolha == "investigar a sala":
                    cenario_atual = cenarios[nome_cenario_atual]
                    print(cenario_atual['titulo'])
                    print(cenario_atual['descricao']) 
                    print('-'*len(cenario_atual['titulo']))           
                    opcoes = cenario_atual['opcoes']
                    print()
                    r2 = random.randint(1,2)
                    if r2 == 1:
                        cenario_atual = cenarios["mimico"]
                        hp_character = hp_character - 5
                        print("Você agora tem {0} hitpoints".format(hp_character))
                        print(cenario_atual['titulo'])
                        print(cenario_atual['descricao'])  
                        print('-'*len(cenario_atual['titulo']))          
                        opcoes = cenario_atual['opcoes']
                        print()
                        for k in opcoes:
                            print("{0}: {1}".format(k, opcoes[k]))
                            print()
                        escolha = input("Você deve voltar para a sala 201!")
                        nome_cenario_atual = escolha
                    if r2 == 2:
                        cenario_atual = cenarios["abrir o bau"]
                        print("Parabens, você ganhou 5 gold coins")
                        gold_pouch = gold_pouch + 5
                        print("Agora você tem {0} gold coins em seu inventario".format(gold_pouch))
                        print(cenario_atual['titulo'])
                        print(cenario_atual['descricao'])
                        print('-'*len(cenario_atual['titulo']))
                        opcoes = cenario_atual['opcoes']
                        print(opcoes)
                        escolha = input("Faça a sua escolha, jovem gafanhoto!")
                        print()
                        for k in opcoes:
                            print("{0}: {1}".format(k, opcoes[k]))
                            print()
                        nome_cenario_atual = escolha
                elif nome_cenario_atual == "sala 102":
                    cenario_atual = cenarios["sala 102"]
                    print(cenario_atual['titulo'])
                    print('-'*len(cenario_atual['titulo']))
                    print(cenario_atual['descricao'])            
                    opcoes = cenarios.keys()
                    print()
                    escolha = input("escolha seu caminho, jovem gafanhoto: ")
                    nome_cenario_atual = escolha
                elif escolha == "enfrentar o rato":
                    cenario_atual = cenarios[nome_cenario_atual]
                    print(cenario_atual['titulo'])
                    print('-'*len(cenario_atual['titulo']))
                    print(cenario_atual['descricao'])            
                    opcoes = cenario_atual['opcoes']
                    print()
                    if hp_inseto <= 0:
                        print("Parabens, você ganhou 5 gold coins e uma pocao")
                        gold_pouch = gold_pouch + 5
                        print("Você tem {0} gold coins em seu invetario".format(gold_pouch))
                elif escolha == "lutar":
                    index = 0
                    while hp_inseto > 0:
                        if escolha == "lutar":
                            hp_inseto = hp_inseto - (atk_character - def_inseto)
                            hp_character = hp_character - (atk_inseto - def_character)
                            print("A sua vida atual é: {0}".format(hp_character))
                            print("A vida atual do inseto é {0}".format(hp_inseto))
                        index = index + 1
                    if hp_inseto <= 0:
                        print("Parabens você ganhou 5 gold coins")
                        gold_pouch = gold_pouch + 5
                        print("Você tem {0} gold coins em seu inventario".format(gold_pouch))
                        index = index + 1            
                elif escolha == "sala 101":
                    hp_inseto = 5
                    cenario_atual = cenarios["sala 101"]
                elif escolha == "batalhar":
                    contador = 0
                    while hp_rato > 0:
                        if escolha == "batalhar":
                            hp_rato = hp_rato - (atk_character - def_rato)
                            hp_character = hp_character - (atk_rato - def_character)
                            print("A sua vida atual é: {0}".format(hp_character))
                            print("A vida atual do rato é {0}".format(hp_rato))
                        contador = contador + 1
                    if hp_rato <= 0:
                        print("Parabens, você ganhou 5 gold coins e uma rapier")
                        atk_character = 7
                        print("O seu atk damage atual é {0}".format(atk_character))
                        gold_pouch = gold_pouch + 5
                        print("Você tem {0} gold coins em seu inventario".format(gold_pouch))
                        contador = contador + 1
                    elif escolha == "usar pocao":
                        if pocao > 0:
                            pocao = pocao - 1
                            if hp_character < 20:
                                hp_character = hp_character + 10
                                print("Você recuperou 10 de vida!")
                                cenario_atual = cenarios["enfrentar o rato"]
                                contador = contador + 1
                            else:
                                print("Você gastou uma pocao atoa")
                                cenario_atual = cenarios["enfrentar o rato"]
                                contador = contador + 1
                    elif escolha == "sala 101":
                        hp_rato = 5
                        cenario_atual = cenarios["sala 101"]
                    hp_rato = 5
                elif escolha == "EP1":
                    r3 = random.randint(1,3)
                    if gold_pouch >= 40:
                        if r3 == 1:
                            gold_pouch = gold_pouch - 40
                            print("Agora você tem {0} gold coins".format(gold_pouch))
                            print("Você subornou o professor, mas a Cavalaria de Étrica descobriu e te matou")
                            game_over = True
                        elif r3 !=  1:
                            gold_pouch = gold_pouch - gold_pouch
                            print("O professor te apunhalou e roubou todo o seu dinheiro")
                            print("Agora você esta pobre, e tem {0} gold coins".format(gold_pouch))
                    else:
                        print("Você tinha pouquissimo dinheiro (menos de 40 coins), por isso foi morto!")
                        game_over = True
                else:
                    continue
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()