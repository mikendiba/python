import random

start = 1
end = 6

def roll():
	x = random.randint(start, end)
	print(x)
	print("Try Again?")
	ip = input()

roll()

if ip == "yes":
	roll()
else:
	exit()

