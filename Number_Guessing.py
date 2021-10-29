import random



print("Wellcome to number guessing !!!! \nyour score is : 20")


random_number = random.randrange(1 , 100)
score = 20
is_not_win = True 

def div_2(number):
	if number % 2 == 0:
		print("Number Divided by 2")
	else:
		print("Number not divid by 2")
def div_3(number):
	if number % 3 == 0:
		print("Number Divided by 3")
	else:
		print("Number not divid by 3")
def div_5(number):
	if number % 5 == 0:
		print("Number Divided by 5")
	else:
		print("Number not divid by 5")
def div_7(number):
	if number % 7 == 0:
		print("Number Divided by 7")
	else:
		print("Number not divid by 7")


	

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
	if score == 18 :
		div_7(random_number)
	elif score == 16 :
		div_5(random_number)
	elif score == 14 :
		div_3(random_number)
	elif score == 10 :
		div_2(random_number)
	if random_number == guess :
		is_not_win = False

