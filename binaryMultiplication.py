import math

inputFile = open("input-2.txt")
lines = inputFile.readlines()
n = int(lines[0])
a = int(lines[1])
b = int(lines[2])

# naive multiplication of order O(n^2).
def longMultiplication(a,b):		# a and b are binary numbers.
	if len(str(b))==1:
		if b==0:
			return 0
		else:
			return a		
	j=len(str(b))-1
	listAB=[]
	zeros=""
	while j>=0:
		listAB.append(str(int(str(a*int(str(b)[j]))+zeros)))
		zeros=zeros+"0"
		j=j-1
		pass
	while len(listAB)>1:
		listAB[0]=bin(int(listAB[0],2)+int(listAB[1],2))
		listAB.pop(1)
		pass
	return listAB[0][2:]

# XY = 2^(2*ceil(n/2)) XlYl + 2^(ceil(n/2)) * [(Xl + Xr)(Yl + Yr) - XlYl - XrYr] + XrYr
def karatsubaMultiplication(x,y):
	if int(x)==1 or int(y)==1:
		return int(x)*int(y)
	elif int(x)==0 or int(y)==0:
		return 0
	elif len(str(x))!=len(str(y)):
		if len(str(x))>len(str(y)):
			i=len(str(x))-len(str(y))
			ydas=str(y)
			while i>0:
				ydas='0'+ydas
				i=i-1
			return karatsubaMultiplication(x,ydas)
		else:
			return karatsubaMultiplication(y,x)
	else:
		a=str(x)[len(str(x))/2:]
		b=str(x)[:len(str(x))/2]

		c=str(y)[len(str(y))/2:]
		d=str(y)[:len(str(y))/2]

		ac = karatsubaMultiplication(int(a),int(c))
		bd = karatsubaMultiplication(int(b),int(d))
		ab = bin(int(a,2)+int(b,2))[2:]
		cd = bin(int(c,2)+int(d,2))[2:]

		# first term
		firstTerm=ac

		# third term
		thirdTerm = karatsubaMultiplication(int(bd),bin(2**(2*((len(str(x))+1)/2)))[2:])
		
		abcd = karatsubaMultiplication(int(ab),int(cd))

		# second term
		secondTerm = bin(int(str(abcd),2)-int(bin(int(str(ac),2)+int(str(bd),2))[2:],2))[2:]
		j = len(str(bin(2**((len(str(x))+1)/2))[2:]))-1
		second=str(secondTerm)
		while j>0:
			second=second+'0'
			j=j-1
			pass

		return bin(int(bin(int(str(firstTerm),2)+int(str(second),2)),2)+ int(str(thirdTerm),2))[2:]


output1=longMultiplication(a,b)
output2=karatsubaMultiplication(a,b)
output3=longMultiplication(a,b)==karatsubaMultiplication(a,b)
print output3

g = open("output_LM.txt","w")
g.write(output1)

g = open("output_KM.txt","w")
g.write(output2)





















