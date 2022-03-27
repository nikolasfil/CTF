#!/bin/python3

imburningthroughthesky = True
twohundreddegrees='flag{D0nt_St0p_M3_N0w}'

print('This is a shell to write python commands \n Leave with exit()\n')

while imburningthroughthesky:
	try:
		code =input('>>>')
		if code.replace(" ","") =='exit()':
			break 
			imburningthroughthesky = False
		eval(code)
	except Exception as e:
		print(e) 

