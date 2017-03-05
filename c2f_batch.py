import sys

for cel in sys.argv[1:]:
	far = (float(cel) * 1.8)+32.0
	print str(cel) +u'\xb0'+ "C is", str(far) + u'\xb0F'