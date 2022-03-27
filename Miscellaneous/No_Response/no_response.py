#!/bin/python3
import os 
import subprocess

print("\nSomeone has left an unguarded shell, rest it's ear upon a wall.\nAs a result, it can listen and excecute your demands, but cannot answer you\n")
while True:
	try:
		x = input('$')
		# os.system(x)
		if x == 'stop':
			break
		elif 'rm' in x :
			pass
		else:
			list_files=subprocess.run(x.split(" "), stdout=subprocess.DEVNULL)
	except :
		pass 
