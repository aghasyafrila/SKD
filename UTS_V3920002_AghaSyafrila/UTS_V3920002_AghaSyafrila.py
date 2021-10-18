abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = int(input('Masukkan cipher key (dalam angka): '))

def encode(kalimat,cipher_key):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode


# Output Enkripsi oleh Caesar Chiper
print('------------Step 1 Caesar Chiper------------')
kalimat = input('Masukkan Teks : ')
kalimat_hasil = encode(kalimat,key)
print('PLAINTEXT:',kalimat)
print('ENKRIPSI DARI KUNCI',key, ':', kalimat_hasil)

def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text))

# Pengenkripisian kembali oleh Vigenere Chiper
print('------------Step 2 Affine Chiper------------')
if __name__ == "__main__": 
  string = "UWEEGUKUPQVHKPCNHKCNWTGKUPQVHCVCNKUKVVJGEQWTIGVQEQPVKPWGVJCVEQWPVU"
  keyword = "YPUCANDOIT"
  key = generateKey(string, keyword) 
  encrypt_text = encryption(string,key)
  print("Encrypted message:", encrypt_text) 
  print("Decrypted message:", decryption(encrypt_text, key))
