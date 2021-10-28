import random



print("Wellcome to number guessing !!!! \nyour score is : 20")


random_number = random.randrange(1 , 100)
score = 20
is_not_win = True 

def compare_number (random_number , guess):
	global score
	if random_number > guess:
		print("your guess is smaller than my number !!!!\n")
		score -= 1
		print(" your score is : " + str(score))

	elif random_number < guess :
		print("Your guess is bigger than my number !!!!\n")
		score -= 1
		print("your score is : " + str(score))
	else :
		print("Your guess is correct !!!\nyour score is %i" %score)



while is_not_win:
	guess = int(input("\nyour guess is : "))
	compare_number(random_number , guess)
	if random_number == guess :
		is_not_win = False

