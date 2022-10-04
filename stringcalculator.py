


def Add(data):
  	#Add implementation
	strLen = len(data)
	sum = 0
	aux = " "
	counter = 0
	for i in range(strLen):
		try:
			aux = data[i]
			if aux == "-":
				i += 1
			else:
				sum = sum + int(aux)
		except:
			pass
		i += 1
	print(sum)
	return sum