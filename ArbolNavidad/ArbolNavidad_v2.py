
# coding:utf-8

def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment


for fil in my_range(1, 6, 1):
	for col in my_range(1, 5, 1):
		if ( fil==1 ):
			if ( col==3 ):
				print "*",
			else:
				print " ",
		else:
			if ( fil==2 ):
				if ( col==3 ):
					print "A",
				else:
					print " ",
			else:
				if ( fil==3 ):
					if ( col==2 ):
						print "A",
					elif ( col==3 ):
						print "A",
					elif ( col==4 ):
						print "A",
					else:
						print " ",
				else:
					if ( fil==4 ):
						print "A",
					else:
						if ( fil==5 ):
							if ( col==3 ):
								print "N",
							else:
								print " ",
						else:
							if ( fil==6 ):
								if ( col==3 ):
									print "N",
								else:
									print " ",
print ""
