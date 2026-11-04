#SLICING= used to extract a subset of data from sequential 
#collecN like string, list ,tuple
a="EQRA"
print("LENgthis:",(len(a)))
w="harry"
len11=len(w) # o=5
print("lenght is:",(len11))
print("\n")
e="Eqra shaikh"
print("Length is:",len(e))
print(e[0:3]) #o=include nd start 0 3 not include so Eqr
print(e[:])  # Eqra shaikh
print(e[:7]) # o= Eqra sh
print(e[1:-3]) # qra sh
print(e[1:len(e)-3]) # qra sh 
print(e[5:]) # o=shaikh
print()
word="Flamingo"
print(len(word))
print(word[1:5]) # o= lami
print(word[4:]) # o=ingo 
print(word[0:8:2]) # o= Faig
print(word[-6:-2]) # 8-6=2 nd 8-2=6 = amin
print(word[2:-2]) # 2 ND 8-2=6    = AMIN
print(word[6:1:-1]) #O= gnima start:stop:step (-1 or -2 at step means we have to look from right to left or skip one from ryt to left#)
print(word[7:2:-2]) #o= onm  
print()
p="python"
print(p[-5:-2]) #O= 6-5=1 nd 6-2=4 = yth

x="COMPUTERS"
print(x[-7:-3]) #O= 9-7=2 nd 9-3=6 so=MPUT
print(x[2:-2]) #O= start 2 nd 9-2==7  =MPUTE
print(x[-6:5])   #o= start 9-6=3 nd 5 == PU
print(x[:-4])     # COMPU
print(x[-5:])   # O=UTERS
print(x[::-1])    # o= SRETUPMOC
print(x[6:2:-1])   # o= ETUP

d="PROGRAMMING"
print(d[3:7])
print(d[0:3])
print(d[-3:])
print(d[::-1])
 