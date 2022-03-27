#!/bin/python 

with open('flag','w') as f:
	f.write('flag{AnotherOne')

work = True

while work:
	try:
		code =input('>>>')
		if code.replace(" ","") =='exit()':
			break 
			work = False
		eval(code)
	except Exception as e:
		print(e) 


try :
	__import__('os').remove('flag')
except:	
	pass 