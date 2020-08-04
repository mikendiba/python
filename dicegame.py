from random import randint

start = 1
end = 10

def generate():
	x = randint(start, end)
	return(x)

def rand_guess():

	randomNumber = generate()

	guess_left = 3

	flag = 0

	while guess_left > 0:

		guess = int(input("Pick your lucky number between 1 and 10 \n"))

		if guess == randomNumber:

			flag = 1

			break
		else:
			print("Wrong guess")

			guess_left -= 1

	if flag == 1:
		return True

	else:
		return False

if __name__ == '__main__':
	if rand_guess() == True:
		print("Winner Winner Chicken Dinner!")
	else:
		print("Loser!")

