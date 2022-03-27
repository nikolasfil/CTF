#!/bin/python3

work = True

print('Here you have a python idle to quickly write some python commands \n')

while work:
	try:
		code =input('>>>')
		if code.replace(" ","") =='exit()':
			break 
			work = False
		eval(code)
	except Exception as e:
		print(e) 

