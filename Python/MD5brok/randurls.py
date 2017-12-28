# import urllib
import random as r
c = 0
hex_list = []
''' 128bit hex generation '''
while c < 15:
	hex_list.append(r.getrandbits(128))
	c += 1

for i in hex_list:
	print(str(hex(i)))
