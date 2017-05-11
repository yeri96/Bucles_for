# coding: utf-8

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

contador=1
print "L M M J V S D"
for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if fil==1:
			if col==7:
				print contador,
				contador=contador+1
			else:
				print " ",
		else:
			if fil>=2:
				if col<=31:
					print contador,
					contador=contador+1
				else:
					print " ",
	print ""
