from random import randint

def sequencia(pontos = 0, streak = 0):
	if streak < 3:
		return False
	if streak >= 3:
		return True
	
def par_verification(player = 2):
	if player % 2 == 0:
		return True
	else:
		return False

pontos = 0
streak = 0

while True:
	computer = randint(1, 5)
	pix = sequencia(pontos, streak)
	player = int(input("Digite um número entre 1-5: "))
	while player not in [1, 2, 3, 4, 5]:
		player = int(input("Favor digitar um número entre 1-5: "))
	if player == computer:
		if pix:
			pix = (streak * pontos)
			pontos += (streak * pontos)
		else:
			pontos += 1
		streak += 1
		print(f"Você ganhou {pix} pontos! O número era {computer} e você escolheu {player}")
		print(f"streak: {streak}")
		print(f"pontos: {pontos}")
	else:
		streak = 0
		print(f"Você errou! O número escolhido era {computer} e você digitou {player}")
		print(f"streak: {streak}")
		print(f"pontos: {pontos}")

	if par_verification(player):
		print(f"O seu número é par")
	else:
		print(f"O seu número não é par")