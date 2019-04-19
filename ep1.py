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
                "guardião do portão": "Falar com o guardião do portão"
            }
        },
        "guardião do portão": {
            "titulo": "A passagem para o segundo andar",
            "descricao": "Voce foi pedir para subir ao segundo andar"
                         "O guardião do portão pede 10 gold coins para subir ao segundo andar ",
            "opcoes": {"primeiro andar" : "Voltar para o primeiro andar e buscar mais recursos",
                       "segudno andar": "Pagar o guardião do portão e subir para o segundo andar"}
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
                "opcoes": {"biblioteca":"Voltar para a biblioteca"}}
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    gold_pouch = 0
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

            print (opcoes)
            escolha = input("faça sua ecolha, jovem cafanhoto: ")
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
                if escolha == cenarios["alavanca"]:
                    gold_pouch = gold_pouch + 10
                    print(gold_pouch)
                else:
                    continue
                print("10 gold coins foram adicionados à sua gold pouch")
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
