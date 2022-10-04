


def Add(data):
  	#Add implementation
	strLen = len(data)
	counter = 0
	sum = 0
	aux = ""
	while(counter < strLen):
		try:
			aux = data[counter]
			if aux == ";" or aux == ",":
				pass
			elif aux == "-":
				counter += 1
			else:
				sum = sum + int(aux)
		except:
			pass
		counter+=1
	print(sum)
	return sum