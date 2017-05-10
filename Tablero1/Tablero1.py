# coding:utf-8

def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment


for fil in my_range(1, 4, 1):
	for col in my_range(1, 8, 1):
		if (( fil==1 ) or ( fil==4 )):
			print "*",
		else:
			if (( col==1 ) or ( col==8 )):
				print "*",
			else:
				if ( fil==2):
					if ( col==4 ):
						print "·",
					elif ( col==5 ):
						print "·",
					else:
						print " ",
				else:
					if ( fil==3 ):
						if ( col==4 ):
							print "|",
						elif ( col==5 ):
							print "|",
						else:
							print " ",
	print ""
