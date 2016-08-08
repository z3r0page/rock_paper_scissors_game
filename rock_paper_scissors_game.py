#!/usr/bin/python

import random

sel = { 'rock': 1,
	'paper': 2,
	'scissor': 3
	}

selrev = { 1: 'rock',
	   2: 'paper',
	   3: 'scissor'
	}

while True:
	p1 = raw_input("Enter your selection: ")
	p2 = selrev[random.randrange(1,4,1)]

	if p1 not in sel:
		print "Err: enter rock, paper or scissor"
		print ""
		continue

	if p1 != p2:
		if p1 == 'rock':
			if p2 == 'paper':
				print "Congrats! Player 2 wins"
			else:
				print "Congrats! Player 1 wins"
		elif p1 == 'paper':
			if p2 == 'scissor':
				print "Congrats! Player 2 wins"
			else:
				print "Congrats! Player 1 wins"
		elif p1 == 'scissor':
			if p2 == 'rock':
				print "Congrats! Player 2 wins"
			else:
				print "Congrats! Player 1 wins"
		else:
			print "Player 1 incorrect selection"
	else:
		print "draw..."
	print ""
	print "Player 1 Selection: " + p1
	print "Player 2 Selection: " + p2
	print ""

	cont = raw_input("Do you want to continue. yes?: ")
	if cont != 'yes':
		break
