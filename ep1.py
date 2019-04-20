# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Rafael Henrique Belini Zanfolin, rafaelhbz@insper.edu.br
# - aluno B: João Pedro Farias Araujo, joaopfa2@al.insper.edu.br
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "primeiro andar": "Tomar o elevador para segundo andar",
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
        "guardiao iluminado": {
            "titulo": "A passagem para o segundo andar",
            "descricao": "Voce foi pedir para subir ao segundo andar"
                         "O guardiao iluminado pede uma chave para você ter direito a subir ao segundo andar ",
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
                          "guardiao sombrio": "falar com o porteiro sombrio"}
        },
        "guardiao sombrio": {
                "titulo": "A passagem para o terceiro andar",
                "descricao":"Você foi pedir para subir ao terceiro andar"
                            "O guardiao sombrio pede uma chave para subir ao terceiro andar"}
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
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
            print(opcoes)
            escolha = input("Faça a sua escolha, jovem gafanhoto: ")
            print('-'*len(cenario_atual['titulo']))
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if escolha == "alavanca":
                    if key > 0:
                        print("\n Você já obteve essas recompensas \n ")
                        print(opcoes)
                        escolha = input("Você deve escolher voltar para a biblioteca! \n ")
                        nome_cenario_atual = "biblioteca"
                    elif key == 0:
                        gold_pouch = gold_pouch + 10
                        inventario.append(gold_pouch)
                        key = key + 1
                        inventario.append(key)
                        print(" \n 10 gold coins foram adicionados à sua gold pouch e você recebeu uma chave \n ")
                        print("Agora o seu inventário possui {0} gold(s) e {1} chave(s) \n ".format(gold_pouch,key))
                elif escolha == "segundo andar":
                    if key <= 0:
                        print("\n Você infelizmente não tem a chave, volte e procure mais recursos \n")
                        print(opcoes)
                        escolha = input("Você deve escolher voltar para o primeiro andar!\n")
                        nome_cenario_atual = "primeiro andar"
                    else:
                        key = key - 1
                        inventario.append(key)
                        print("Você entregou a chave para o guardiao iluminado, agora você tem {0} keys em seu inventario".format(key))
                else:
                    continue
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
