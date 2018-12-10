#source code
import roundKey, encryptAES, decryptAES

plaintext = "54776F204F6E65204E696E652054776F"
key = "5468617473206D79204B756E67204675"

rk = roundKey.generateRK(key) #round key selesai

print("Plaintext  : %s" % plaintext)

#Encryption
encryption = encryptAES.encrypt(plaintext, rk)

print("Encryption : %s " % encryption)

ciphertext = encryption

#Decryption
decryption = decryptAES.decrypt(ciphertext, rk)

print("Decryption : %s" % decryption)