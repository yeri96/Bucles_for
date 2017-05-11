# coding:utf-8

def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment


for fil in my_range(1, 8, 1):
	for col in my_range(1, 8, 1):
		if ( fil==1 ) or ( fil==7 ):
			if ( col%2==0 ):
				print "*",
			else:
				print " ",
		else:
			if ( fil==2 ) or ( fil==8 ):
				if ( col%2==1 ):
					print "*",
				else:
					print " ",
	print ""
