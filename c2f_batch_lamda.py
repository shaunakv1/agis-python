import sys

#using lamda function
print map(lambda x : (float(x) * 1.8) + 32.0, sys.argv[1:])

#list comphrention way
results = [(float(i) * 1.8) + 32.0 for i in sys.argv[1:]]
print results