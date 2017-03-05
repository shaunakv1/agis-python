min = 0
max = 100

print "Think of a number from", min, 'to', max

while True:
	guess = (min + max) / 2
	ans = raw_input("Is your number " +  str(guess) + "? (enter y (yes),l (low), h(high) ): ")
	if ans == 'y':
		print 'I guessed it'
		break
	elif ans == 'l':
		min = guess	
	else:
		max = guess

