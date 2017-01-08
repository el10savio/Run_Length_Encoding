#Run Length Encoding - Encoder
import sys

a = str(raw_input('Enter String: '))
print 'Stats:'
print 'Length=',len(a)
print 'Size=',sys.getsizeof(a)
a= list(a)

k=[]
num=0
counter=0
x=a[0]
while(counter<len(a)):
    if x==a[counter]:
      num+=1
    else:
      k.extend([num,':',a[counter-1],'/'])
      num=1
    x=a[counter]
    counter+=1
k.extend([num,':',a[counter-1],'/'])

k = ''.join(str(e) for e in k)
print '\nEncoded- ',k
print 'Stats:'
print 'Length=',len(k)
print 'Size=',sys.getsizeof(k)
