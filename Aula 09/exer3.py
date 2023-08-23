"""
Gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou e a quantidade de gols feitas em cada partida. 
Coloque tudo num dicionário, incluindo o total de gols durante o período
"""

def main():
    jog = {
        "nome": input("Nome: "),
        "partidas": int(input("Número de partidas: ")),
        "gols_parts": int(input("Gols por partida: "))
    }
    
    jog["total_gols"] = jog["partidas"] * jog["gols_parts"]

    print(jog)

main()

