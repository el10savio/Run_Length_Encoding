#Run Length Encoding - Encoder
#test: /127:0/1:1/127:0/

import sys
import re
from PIL import Image
import numpy as np
from numpy import array

a = str(raw_input('Enter String: '))
#a= list(a)

group = a.split("/")
#print group

entry=[]
for element in group:
	entry.append(element.rsplit(":"))
#print entry

result=[]		
for values in entry:
	#print values
	if len(values)>1:
		a=values[0]
		x=values[1]
		#print a,x
		result+= x * int(a)

print str(result)


