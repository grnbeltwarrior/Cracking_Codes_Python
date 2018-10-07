# Caesar Cipherv2

MAX_KEY = 26

def getMode():
	while True:
		mode = input('Encrypt or decrypt (e/d): ')
		mode.lower()
		if mode in 'e d'.split():
			return mode
		else:
			print('Enter "e" for encrypt or "d" for decrypt.')

def getMessage():
	print('Enter your secret message: ')
	return input()

def getKey():
	key = 0
	while True:
		print('Enter the key (1-26)')
		key = int(input())
		if (key >= 1 and key <= MAX_KEY):
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Your message is:')
print(getTranslatedMessage(mode, message, key))
