import sys

conv_to_f = lambda x : (float(x) * 1.8) + 32.0
#sys.argv.pop(0)
print map(conv_to_f, sys.argv[1:])

