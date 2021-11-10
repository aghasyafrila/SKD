#Initial Permutation Matrix (64bits).
P_i = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7] 
#Tabel ini menentukan permutasi input pada blok 64-bit.
#Artinya adalah sebagai berikut: bit pertama dari output diambil dari bit ke-58 dari input; 
#bit kedua dari bit ke-50, dan seterusnya, dengan bit terakhir dari output diambil dari bit ke-7 dari input.
#Informasi ini disajikan dalam bentuk tabel untuk kemudahan penyajian; itu adalah vektor, bukan matriks.

#Final Permutation Matrix(After 16 Rounds)(64bits).
P_f = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25] 
#Permutasi terakhir adalah inverse dari permutasi awal;

#Key Generator Algorithm.

#Membuat Matriks Kunci .
#Membuat matriks permutasi kunci 56 bits
PC_1 =  [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#permutasi dilakukan dengan menggeser kunci (i+1) 48 bits
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


#Ekspansi matriks fungsi kemudian di XOR kan dengan K-i (32 bits menjadi 48 bits)
E =  [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#Substitution Box.
S_box = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]


#Permutasi dibuat setelah subsitusi tiap perulangan (28 bits)
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]


#Matriks kunci untuk pergeseran tiap perulangan (16 bits)
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def str_to_bit_array(text): #Konversi teks ke kelompok bits 
    array = list()
    for char in text:
        binval = binvalue(char, 8) #Mengambil tiap nilai karakter tiap byte
        array.extend([int(x) for x in list(binval)]) #Menambahkan bit ke list paling belakang
    return array

def bit_array_to_str(array): #membuat string dari ke array
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Mengembalikan nilai biner sebagai string sesuai ukuran
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "Binary value is too large"
    while len(binval) < bitsize:
        binval = "0"+binval #Menambahkan nilai 0 seusai dengan ukuran.
    return binval

def nsplit(s, n): #Membagi list menjadi sublist sesuai dengan ukuran yg ditentukan
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0

class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
        
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long !"

        self.password = key
        self.text = text
        
        if padding and action==ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0: #Cek teks, harus 8 bit. teks kelipatan 8 bit.
            raise "Data size should be multiple of 8 !"
        
        self.generatekeys() #Generates kunci.
        text_blocks = nsplit(self.text, 8) #Kelompokkan teks menjadi blok 8 bit.
        result = list()
        for block in text_blocks: #Perulangan membuat block data 
            block = str_to_bit_array(block) #Converts the block in bit array. Konversi block kedalam bit array
            block = self.pmt(block,P_i) #masuk ke initial permutation
            l, r = nsplit(block, 32) # l(LEFT),r(RIGHT).
            tmp = None
            for i in range(16): #16 rounds.
                r_e = self.expand(r, E) #Mengembangkan r ke ukuran tertentu K_i (48bits).
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], r_e) #Jika enkripsi pakai K_i.
                else:
                    tmp = self.xor(self.keys[15-i], r_e)#Jika dekripsi, mulai dari kunci terakhir.
                tmp = self.substitute(tmp) #Masuk SBOX
                tmp = self.pmt(tmp, P)
                tmp = self.xor(l, tmp)
                l = r
                r = tmp
            result += self.pmt(r+l, P_f) # Permutasi terakhir, masukkan nilai ke variabel.
        final_res = bit_array_to_str(result)
        if padding and action==DECRYPT:
            return self.removePadding(final_res) #hilangkan padding jika melakukan dekripsi.
        else:
            return final_res #mengembalikan nilai dekripsi/enkripsi
        
    def substitute(self, r_e): #substitusi tiap bits menggunakan tabel SBOX
        subblocks = nsplit(r_e, 6) #Bagi tiap array bit ke dalam list berisi 6 bit 
        result = list()
        for i in range(len(subblocks)): #For all the sublists
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)#Ambil bit pertama dan terakhir 
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Ambil bit ke 2 3 4 5
            val = S_box[i][row][column] #Ambil nilai pada SBOX sesuai urutan
            bin = binvalue(val, 4)#Konversi nilai menjadi biner 
            result += [int(x) for x in bin]#Masukkan hasil  substitusi ke dalam variabel 
        return result
        
    def pmt(self, block, table):
        return [block[x-1] for x in table]
    
    def expand(self, block, table): #permutasi 
        return [block[x-1] for x in table]
    
    def xor(self, t1, t2): #operasi perhitungan XOR dan mengembalikan nilai hasil XOR.
        return [x^y for x,y in zip(t1,t2)]
    
    def generatekeys(self): #Algoritma untuk menggenerate kunci .
        self.keys = []
        key = str_to_bit_array(self.password)
        key = self.pmt(key, PC_1) #Initial permutation pada kunci .
        l, r = nsplit(key, 28) #Bagi kunci menjadi 2 bagian (L0 dan R0) masing-masing sebesar 28 bit .
        for i in range(16): #Perulangan 16 kali .
            l, r = self.shift(l, r, SHIFT[i]) #Pergeseran sesuai dengan tabel shift.
            tmp = l + r #Merges them.
            self.keys.append(self.pmt(tmp, PC_2)) #Permutasi lagi untuk mendapatkan K_i.

    def shift(self, l, r, n): #Geser list sesuai nilai .
        return l[n:] + l[:n], r[n:] + r[:n]
    
    def addPadding(self): #Fungsi untuk padding data.
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)
    
    def removePadding(self, data): #Remove Padding .
        pad_len = ord(data[-1])
        return data[:-pad_len]
    
    def encrypt(self, key, text, padding=True):
        return self.run(key, text, ENCRYPT, padding)
    
    def decrypt(self, key, text, padding=True):
        return self.run(key, text, DECRYPT, padding)
 

if __name__ == '__main__':
     key = input ("Masukkan kunci 8 bit :")
     text= input ("Plaintext: ")
     d = des()
     ciphered = d.encrypt(key,text,padding=True) 
     plain = d.decrypt(key,ciphered,padding=True) 
     print ("Decryption Text: ", plain)
     print ("Cipher text %r" % ciphered)
