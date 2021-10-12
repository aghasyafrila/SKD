alpha='abcdefghijklmnopqrstuvwxyz'
beta={}
a='a'
for i in range(0,26):
    beta[i]=chr(ord(a)+i)
#print(beta)
#plaintext=input('Enter the plain text');
plaintext='AGHASYAFRILA'
cipher=[]
key=[[5,2],[6,3]]
adkey=[[1,8],[24,19]]
a=plaintext.lower()
if(len(a)%2==1):
    a=a+'x'
print('Plaintext =',a)
print('Length of plain text=',len(a))
c=[]
l=[]
pt=[]
final=[]
for i in range(0,int(len(a)/2)):
    c.append([]);
    l.append([]);
    pt.append([]);
    final.append([]);
i=0;
j=0;
while(i<int(len(a)/2)):        
    l[i].append(0)
    l[i].append(0)
    c[i].append(ord(a[j]))
    j=j+1
    c[i].append(ord(a[j]))
    j=j+1
    i=i+1
for i in range(int(len(a)/2)):
#    print(c[i][0]-97)
    c[i][0]=(c[i][0]-97);
    c[i][1]=(c[i][1]-97);
#else:
#       break
# matrix multiplication
ct=''
for i in range(int(len(a)/2)):
    for j in range(len(c[0])):
        pt[i].append(0);
        final[i].append(0);
        for k in range(len(c[0])):
            l[i][j]=(l[i][j]+(c[i][k]*key[k][j]))%26
        cipher.append(beta[l[i][j]])
#        print(cipher)
        ct=ct+beta[l[i][j]]
print('Cipher text in in numeric array=',l)
print('Cipher',cipher,'\nctext=',ct)
print('length of cipher text',len(cipher))
k=0
for i in range(0,int(len(cipher)/2)):
    for j in range(0,2):
        pt[i][j]=(ord(cipher[k])-97)%26
        k=k+1
er=[]
#decription to plain text
for i in range(int(len(a)/2)):
    for j in range(2):
        for k in range(2):
            final[i][j]=(final[i][j]+(pt[i][k]*adkey[k][j]))%26
        er.append(beta[final[i][j]])
#        print(er)
print('Length of decipher text =',len(er))
print('Final palintext in array=',final)
print('Decipher text =',er)