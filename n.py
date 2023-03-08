#!/bin/python3
import os
import sys
with open('n.txt','w') as n:
		with open('4.txt', 'r') as x:
			a = 0
			for c in x:
				c = c.replace('\n','')
				for i in range (0,10000):
					if int(i) < 1000:
						i = '0{}'.format(i)
					if int(i) < 100:
        	                        	i = '0{}'.format(i)
					if int(i) < 10:
        		                        i = '0{}'.format(i)
					n.write('{}{}{}\n'.format(c,i,21))
					a = a+1
					print('[ {} ]{}{}{}\n'.format(a,c,i,21))
