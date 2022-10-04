


def Add(data):
  	#Add implementation
	strLen = len(data)
	counter = 0
	sum = 0
	aux = ""
	while(counter < strLen):
		try:
			aux = data[counter]
			sum = sum + int(aux)
		except:
			pass
	print(sum)
	return sum