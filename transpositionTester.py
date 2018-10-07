''' 
transposition tester script to check the validity of the process to encrypt and decrypt using transistion_cipher.py
thus the reason for the import of transposition_cipher
'''
import transposition_cipher
import random
import sys

def main():
	random.seed(42)

	for i in range(20):
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)

		message = list(message)

		random.shuffle(message)
		message = ''.join(message)

		key = 8

		print('Test %s: "%s..."' % (i + 1, message[:50]))

		for key in range(1,int(len(message)/2)):
			encrypted = transposition_cipher.decryptMessage(key, message)
			#print('Encrypted Message: %s' % encrypted)
			decrypted = transposition_cipher.encryptMessage(key, encrypted)
			#print('Decrypted Message: %s' % decrypted)

			if message != decrypted:
				print ('Mismatch with key %s and message %s.' % (key, message))
				print('Decrypted as: ' + decrypted)
				sys.exit()
	print('Transposition cipher test passed')

main()
