
import array as array

def Add(data):
  	#Add implementation
	strLen = len(data)
	sum = 0
	aux = " "
	counter = 0
	while(counter < strLen):
		try:
			aux = data[counter]
			if aux == "-":
				counter = counter + 1
			else:
				sum = sum + int(aux)
		except:
			pass
			counter = counter + 1
	print(sum)
	return sum