import sys

sys.argv.pop(0)
for cel in sys.argv:
	far = (float(cel) * 1.8)+32.0
	print str(cel) +u'\xb0'+ "C is", str(far) + u'\xb0F'