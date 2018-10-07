import math # because math is hard
'''
Transposition encryption example:
Key = 6
message = 'Why hello, world.'
len(message) = 17

[W][h][y][][h][e]
[l][l][o][,][][w]
[o][r][l][d][.][] < this last box is empty/blank.

There for the output would be [wlo][hlr][yol][ ,d][h .][ew]
OR
wlohlr ,dh .ew| < pipe on the end.


'''
def decryptMessage(key, message):
	numOfColumns = int(math.ceil(len(message) / float(key)))
	numOfRows = key
	numOfBlankBoxen = (numOfColumns * numOfRows) - len(message)
	plaintext = [''] * numOfColumns

	column = 0
	row = 0

	for symbol in message:
		plaintext[column] += symbol
		column += 1

		if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfBlankBoxen):
			column = 0
			row += 1
	return ''.join(plaintext)

def encryptMessage(key, message):
	ciphertext = [''] * key
	for column in range(key):
		currentIndex = column

		while currentIndex < len(message):
			ciphertext[column] += message[currentIndex]
			currentIndex += key

	return ''.join(ciphertext)

#myMessage = 'Uncommon valor was an common virtue.'

def main():

	deMessage = 'U amtnvsmuca oeolan.mon mr vo cinwor'
	myMessage = 'Uncommon valor was an common virtue.'
	myKey = 8

	choice = input('Choose to encrypt or decrypt: (e/d): ')

	if (choice == 'd'):
		plaintext = decryptMessage(myKey, deMessage)
		print(plaintext + '|')

	elif (choice == 'e'):
		ciphertext = encryptMessage(myKey, myMessage)
		print(ciphertext + '|')
	
	else:
		print('You entered in something other than "e" or "d".')

if __name__ == '__main__':
	main()
