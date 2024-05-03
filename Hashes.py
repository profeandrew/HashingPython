#Exercises: Calculate Hashes


# Write a program to calculate hashes of given text
#message: SHA-224, SHA-256, SHA3-224, SHA3-384, Keccak-384 and
#Whirlpool. Write your code in programming language of choice


# Importar librerías haslib y binascii
import hashlib, binascii

hacked_hashes = {
    "SHA-224":"ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193",
    "SHA-256":"2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9",
    "SHA3-224":"b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81",
    "SHA3-384":"720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620"
    }

# usuario ingresa una palabra o frase 
hashInputByUser = input("Ingrese una palabra \n")

# convierte el string a formato bytes 
usefullHash = hashInputByUser.encode("utf8")

#Llamada a método sha224 que genera un hash digest tipo sha224
sha224Hash = hashlib.sha224(usefullHash).digest()

#Convierte el hash de binario a hexadecimal  
sha224Hash = binascii.hexlify(sha224Hash)

# Almacena el hashing como string en lugar de byte 
cleanSha224Hash = sha224Hash.decode("utf-8")

# imprime el hash generado 

print("Generated sha224 Hash:", cleanSha224Hash)

#imprime el hash almacenado previamente 
print("Stored sha224 Hash:", hacked_hashes["SHA-224"])

#Compara ambos hashes 
print("Hashes match?:", hacked_hashes["SHA-224"] == cleanSha224Hash)

