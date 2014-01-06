import random
import string

endProduct = "METHINKS IT IS LIKE A WEASEL"
population = []
mutationRate = 5

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def mutate(input):
	global mutationRate
	chars= list(input)
	for i in range(len(chars)):
		rand=random.randint(1,100)
		if rand <= mutationRate:
			chars[i]= random.choice(string.ascii_letters+" ")
	print "".join(chars)
	return "".join(chars)
def createPopulation(input):
	global population
	print input
	for i in range(100):
		population.append(mutate(input))
def measureFitness(pop):
	global endProduct
	best = ""
	bestDiff = 100
	tdiff = 0
	for i in range(len(pop)):
		u = zip(pop[i], endProduct)
		for j,k in u:
			if j!=k:
				tdiff=tdiff+1
		if tdiff < bestDiff:
			best= pop[i]
			bestDiff=tdiff
			print "best is atm "+ best
		tdiff = 0
	print "returned " + best
	return best

enteredRate = raw_input("Enter mutation rate: ")
mutationRate = int(enteredRate)

createPopulation(randomword(len(endProduct)))
#createPopulation("Me thinks it is like a weasel")
for i in range(10000):
	bestIndividual=measureFitness(population)
	print bestIndividual
	if bestIndividual==endProduct:
		break
	population=[]
	createPopulation(bestIndividual)

print "wanted " + endProduct+ ", got " +bestIndividual
print "This required " + str(i) + "generations with mutation rate of " + str(mutationRate) +"%"