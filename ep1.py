# Alunos: 
# - aluno A: Rafael Henrique Belini Zanfolin, rafaelhbz@insper.edu.br
# - aluno B: João Pedro Farias Araujo, joaopfa2@al.insper.edu.br
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "primeiro andar": "Tomar o elevador para primeiro andar",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "primeiro andar": {
            "titulo": "O misterioso andar",
            "descricao": "Voce chegou ao primeiro andar",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "sala 101": "Ir para a sala 101",
                "sala 102": "Ir para a sala 102",
                "guardiao iluminado": "Falar com o guardiao iluminado"
            }
        },
        "sala 101":{
                "titulo":"O covil de monstros",
                "descricao":"Você escuta gritos ensurdecedores, quem será que está gritando?",
                "opcoes":{"primeiro andar":"voltar paraa o primeiro andar",
                          "investigar o local":"verificar de onde veio o grito"
                    }
        },
        "investigar o local":{
                "titulo":"O grito está ainda mais alto",
                "descricao": "Você está tenso e esperando o pior acontecer",
                "opcoes":{}
                },
        "apareceu um rato":{
                "titulo":"Você encontrou um rato",
                "descricao":"Prepare-se para o combate",
                "opcoes":{"sala 101":"Você volta para a sala 101",
                          "enfrentar o rato":"Você inicia o combate"}
        },
        "apareceu um inseto":{
                "titulo":"Você encontrou um inseto",
                "descricao":"Prepare-se para o combate",
                "opcoes":{"sala 101":"Você volta para a sala 101",
                          "enfrentar o inseto":"Você inicia o combate"}
        },
        "enfrentar o rato":{"titulo":"Você decidiu enfrentar o rato",
                            "descricao":"O combate iniciou",
                            "opcoes":{"batalhar":"você ataca o rato",
                                      "sala 101":"você foge para a sala 101",
                                      "usar pocao":"você usa uma pocao de cura"}
        },
        "enfrentar o inseto":{"titulo":"Você decidiu enfrentar o inseto",
                              "descricao": "O combate iniciou",
                              "opcoes":{"atacar":"você ataca o inseto",
                                        "sala 101":"você foge para a sala 101",
                                        "usar pocao":"voce usa uma pocao de cura"}
        },
        "batalhar":{"titulo":"Você batalhou contra o monstro",
                  "descricao":"Parabéns, você conseguiu matar o monstro, agora volte para a sala 101",
                  "opcoes":{"sala 101":"voltar para a sala 101"
                          }
        },
        "guardiao iluminado": {"titulo": "A passagem para o segundo andar",
                               "descricao": "O guardiao iluminado pede uma chave para você ter direito a subir ao segundo andar" ,
                               "opcoes": {"primeiro andar" : "Voltar para o primeiro andar e buscar mais recursos",
                                          "segundo andar": "Pagar o guardião iluminado e subir ao segundo andar"}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "aquario 11": "Entrar para o aquario 11"}
        },
        "aquario 11": {
                "titulo":"Santuario das indecisoes",
                "descricao": "Voce esta no Santuario das decisoes",
                "opcoes": {"alavanca": "Puchar a alavanca",
                           "biblioteca": "Voltar para a biblioteca"}
        },
        "alavanca" : {
                "titulo":"Parabens, você teve coragem de encarar o seu destino",
                "descricao":"Você obteve 10 gold coins",
                "opcoes": {"biblioteca":"Voltar para a biblioteca"}
        },
        "segundo andar": {
                "titulo": "O andar da infantilidade",
                "descricao":"Você chegou ao segundo andar",
                "opcoes":{"primeiro andar":"Voltar para o primeiro andar",
                          "sala 201":"Ir para a sala 201",
                          "sala 202":"Ir para a sala 202",
                          "professor": "falar com o porteiro sombrio"}
        },
        "sala 201":{
                "titulo":"Cheiro de surpresa no ar",
                "descricao":"A atmosfera desta sala é muito misteriosa",
                "opcoes":{"segundo andar":"voltar para o segundo andar",
                          "investigar a sala":"vasculhar o que tem nessa sala"}
        },
        "sala 202":{
                "titulo":"Sala da regeneração",
                "descricao":"Você encontrou a sala de recuperacao",
                "opcoes":{"segundo andar":"Você volta para o segundo andar"}
        },
        "investigar a sala":{
                "titulo":"Você avista um paralepipedo no meio do miasma",
                "descricao":"O paralepipedo e na realidade um bau",
                "opcoes":{}
        },
        "mimico":{
                "titulo":"Oh nao, o bau era um mimico",
                "descricao":"O mimico mordeu o seu braco direito",
                "opcoes":{"sala 201":"Você volta para a sala 201"}
        },
        "bau":{
                "titulo":"O paralelepipedo realmente era um bau",
                "descricao":"Você abriu o bau e obteve recompensas",
                "opcoes":{"sala 201":"Você volta para a sala 201",
                          "abrir bau":"Você decide abrir o bau"}
        },
        "abrir bau":{
                "titulo":"O bau tem um bilhete dentro",
                "descricao":"Esta escrito 'Haha troxa!' no bilhete",
                "opcoes":{"sala 201":"Voltar para a sala 201"}
        },
        "professor": {
                "titulo": "A sua história chega ao final",
                "descricao":"Você foi pedir permissão para entregar o EP1 atrasado"
                            "O professor permite você entregar o EP1",
                            "opcoes":{"EP1":"entregar o EP1",
                                      "segundo andar":"Voltar para o segundo andar"}
        },
        "sala 102":{
                "titulo": "Hub de Teleporte",
                "descricao": "aqui você pode voltar para qualquer luga sem demora!!!",
                "opcoes":{"digite o nome do lugar que quer ir, CUIDADO: escreva errado e morrerá!":"..."}
        }
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    import random
    r3 = random.randint(1,3)
    r4 = random.randint(2,4)
    r5 = random.randint(3,5)
    
    hp_character = 30
    def_character = 0
    atk_character = 3
    
    hp_rato = 5
    def_rato = 0
    atk_rato = 2
    
    hp_inseto = 4
    def_inseto = 1
    atk_inseto = 3
    
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
                        print(" \n 10 gold coins foram adicionados à sua gold pouch e você recebeu uma chave \n ")
                        print("Agora o seu inventário possui {0} gold(s) e {1} chave(s) \n ".format(gold_pouch,key))
                elif escolha == "sala 202":
                    print(cenario_atual['titulo'])
                    print(cenario_atual['descricao'])
                    print('-'*len(cenario_atual['titulo']))
                    if hp_character < 25:
                        hp_character = hp_character + 5
                        print("Você recuperou 5 de vida")
                        print("A sua vida atual é {0}".format(hit_points))
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
                        key = key - 1
                        inventario.append(key)
                        print("Você entregou a chave para o guardiao iluminado, agora você tem {0} keys em seu inventario".format(key))
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
                        cenario_atual = cenarios["bau"]
                        print(cenario_atual['titulo'])
                        print(cenario_atual['descricao'])
                        print('-'*len(cenario_atual['titulo']))
                        escolha = input("Faça a sua escolha, jovem gafanhoto!")
                        
                        opcoes = cenario_atual['opcoes']
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
                        print("Parabens, você ganhou 5 gold coins")
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
                else:
                    continue
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()