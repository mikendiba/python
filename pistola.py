from random import randint

selection = ['Pistola','Sombrero','Burro']

computer = selection[randint(0,2)]

player = False

while player == False:
	player = input('Pistola,Sombrero,Burro? \n')
	if player == computer:
		print("Tie")
	elif player == 'Pistola':
		if computer == 'Sombrero':
			print("You lose !  %s covers %s" % (computer,player))
		else:
			print("You win ! %s shoots %s" % (player,computer))
	elif player == 'Sombrero':
		if computer == 'Burro':
			print("You lose !  %s kicks %s" % (computer,player))
		else:
			print("You win ! %s covers %s" % (player,computer))
	elif player == 'Burro':
		if computer == 'Pistola':
			print("You lose !  %s shoots %s" % (computer,player))
		else:
			print("You win ! %s kicks %s" % (player,computer))
	else:
		print("WTF don't you know how to spell?")
	player = False
	computer = selection[randint(0,2)]



