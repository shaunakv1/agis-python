def guess(min, max):
	g = (min + max) / 2
	ans = raw_input("Is your number " +  str(g) + "? (enter y (yes),l (low), h(high) ): ")
	if ans == 'y':
		print 'I guessed it'
		return
	elif ans == 'l':
		guess(g,max)	
	else:
		guess(min,g)


#start
min = 0
max = 100

print "Think of a number from", min, 'to', max
guess(min,max)
