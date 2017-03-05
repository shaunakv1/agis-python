import sys
sys.argv.pop(0)
for cel in sys.argv:
	far = (float(cel) * 1.8)+32.0
	print "temp in far is", far, u'\xb0'