import random

a = random.sample(range(0,100),random.randint(0,50))
b = random.sample(range(0,100),random.randint(0,50))

print sum(a)


print "a: " + str(a)
print "b: " + str(b)






print set([x for x in a if x in b])