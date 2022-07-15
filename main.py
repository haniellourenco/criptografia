import base64
from operator import mod
import text_chunk

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv[1]))

#function Crypt:

# read key_file_name (public key)
keyFileName = sys.argv[1]
# read source_file_name (plain)
srcFileName = sys.argv[2]
# read dest_file_name (crypted)
# destFileName = sys.argv[3]

#abre arquivo de chaves
keyFile = open(keyFileName, 'r')
keyFileReader = keyFile.readlines()

aLinhasKey = []

count = 0
# # Strips the newline character
for line in keyFileReader:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))
    aLinhasKey.append(line.strip())

#Load modulos, key from key_file_name
modulusStr = aLinhasKey[0]
keyStr = aLinhasKey[1]

modulus = int(modulusStr)
key = int(keyStr)
# modulus = int((str(modulusStr)), 10)
# key = int((str(keyStr)), 10)

# modulusBigInt
print("Modulus: " + modulusStr)
print("Key: " + keyStr)



#abre arquivo source
srcFile = open(srcFileName, 'r')
# #Load text from source_file_name
srcFileText = srcFile.read()
print(srcFileText)


#pega chunkSize
chunkSize = text_chunk.block_size(modulus)

print(chunkSize)

src_text_bytes = srcFileText.encode('ascii')
base64_bytes = base64.b64encode(src_text_bytes)
codedText = base64_bytes.decode('ascii')

print(codedText)


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

#itera por cada grupo de caracteres quebrados pelo blocksize
# for chunk in codedText[:chunkSize]:
    # originalChunk = text_chunk.TextChunk.int_value(self=chunk)
    # originalChunk = base64.b64decode(chunk)
    # encodedChunk = originalChunk.pow(originalChunk, key, modulus)
    # print(chunk)

v = chunkstring(codedText, chunkSize)

print(v)

# a= text_chunk.TextChunk(srcFileText)
# print(a)

# encodedChunk = list(chunkstring(codedText, chunkSize))
# print(encodedChunk)