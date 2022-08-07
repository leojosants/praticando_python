'''093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

'''jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
qntpart = int(input(f'Quantidade de partidas {jogador["nome"]} jogou: '))
if qntpart > 0:
        for c in range(0, qntpart):
            resp = (int(input(f'Quantos gols na partida {c+1}: ')))
            gols.append(resp)
            total += resp

print('-='*30)
jogador['gols'] = gols.copy()
jogador['total'] = total
print(jogador)
#print(gols)
#print(total)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {qntpart} partidas.')
for c, g in enumerate(gols):
    print(' '*5, f'==> Na partida {c}, fez {g} gol(s).')
print(f'Foi um total de {total} gol(s)')'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas) #comando direto de soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   ==> Na partida {i}, fez {v} gol(s).')
print(f'Foi um total de {jogador["total"]} gol(s)')