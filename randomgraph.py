from random import randint

print "graph large {"
stuff = list()
r = randint(1,300)
for x in xrange(5):
	y = randint(1,300)
	if y!=r:
		print "\t",r,"--", y
		stuff.append(y)

for x in xrange(200):
	t = randint(1,300)
	v = randint(1, len(stuff)-1)
	if t != stuff[v]:
		print "\t",stuff[v],"--", t
		stuff.append(t)


print "}"