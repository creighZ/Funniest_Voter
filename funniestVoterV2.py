from random import *
import os




#players_number = raw_input("How many people are playing today? ")
players_number = 4 #int(players_number)


score1 = []
score2 = []
score3 = []
score4 = []
contestants = []
names = []
contestants_response = {}
scores = [
score1,
score2,
score3,
score4
]





for x in xrange(players_number):
	pn = str(x + 1)
	contestants.append('player_' + pn)

#print contestants, contestants_response
os.system('clear')

def scoring():
	contest = contestants
	contest_response = contestants_response
	scores_ = scores
	for x in contest:
		print contest_response[x]
		rank = raw_input("Rank from 0 to 10: ")
		try:
			rank = int(rank)
		except:
			print "This is a numbers based ranking system. If you want to use letters, build your own game!"
			contest.append(x)
		else:
			if rank > 10:
				print "10 is as funny as it gets! My game, my ranking system related rules!"
				contest.append(x)
				del rank
			elif rank < 0:
				print "It might be bad, but 0 is as low as it goes"
				contest.append(x)
				del rank
			else:
				None

			score_num = x[-1]
			score_num = int(score_num)
			#print score_num
			try:
				scores_[score_num - 1].append(rank)
			except:
				pass
			#print scores 
			print "\n\n\n"

	return scores_

for x in xrange(players_number):
	
	player_response = raw_input("Hello Player %s! Enter your name to begin: " % str(x + 1))
	names.append(player_response)

#print contestants


scenarios = ["Why did the chicken cross the road? ", "Knock Knock... Who's there?... (Answer + punch line) "]

shuffle(scenarios)

random_scenarios = scenarios

for x in xrange(players_number):
	responder = names[x]
	os.system('clear')
	print "Hello %s! Please provide your most HIlarious response to..." % responder
	player_response = raw_input(random_scenarios[0])
	contestants_response[contestants[x]] = player_response


#print contestants_response

for x in xrange(players_number):
	responder = names[x]
	print "\n"
	print "Ok, %s, time to vote. Give each of the following responses a funnyness ranking from one to ten, ten being hilarious, one being not so much." %  responder
	shuffle(contestants)
	contestants = contestants
	print random_scenarios[0]
	print "\n\n\n"
	updated_scores = scoring()
	
	contestants = []

	for x in xrange(players_number):
		pn = str(x + 1)
		contestants.append('player_' + pn)

	os.system('clear')

print updated_scores

final_tally = []

for x in updated_scores:
	final_tally.append(sum(x))

for x in xrange(players_number):
	print "%s scored %s points" % (names[x], final_tally[x])
	print "\n"	

# if final_tally[0] > final_tally[1] and final_tally[0] > final_tally[2] and final_tally[0] > final_tally[3]:
# 	print "\n\n"
# 	print "%s won! They are the funniest human alive!" % names[0]
# elif final_tally[1] > final_tally[0] and final_tally[1] > final_tally[2] and final_tally[1] > final_tally[3]:
# 	print "\n\n"
# 	print "%s won! They are the funniest human alive!" % names[1]
# elif final_tally[0] > final_tally[1] and final_tally[0] > final_tally[2] and final_tally[0] > final_tally[3]:
# 	print "\n\n"
# 	print "%s won! They are the funniest human alive!" % names[0]




