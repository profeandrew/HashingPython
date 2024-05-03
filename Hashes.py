#Exercises: Calculate Hashes


# Write a program to calculate hashes of given text
#message: SHA-224, SHA-256, SHA3-224, SHA3-384, Keccak-384 and
#Whirlpool. Write your code in programming language of choice


# Importar librerías haslib y binascii
import hashlib, binascii

hacked_hashes = {
    "SHA3-224":"b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81",
    "SHA3-384":"720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620"
    }

# usuario ingresa una palabra o frase 
hashInputByUser = input()

# encode UTF-8
usefullHash = hashInputByUser.encode("utf8")

#Llamada a método sha224 que genera un hash digest tipo sha224
sha224Hash = hashlib.sha224(usefullHash).digest()

#Permite que el hashing generado sea legible 
sha224Hash = binascii.hexlify(sha224Hash)

hashSinComillas = sha224Hash.replace("'", "")

print("Generated sha224 Hash:", hashSinComillas)

print("Stored 224 Hash:", hacked_hashes["SHA-224"])

print("Hashes match?:", hacked_hashes["SHA-224"] == hashSinComillas)