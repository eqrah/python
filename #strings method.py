#strings method ,,, 
#string is immutable it cannot be changed it we can copy from og string to make changes
a="this is cake"
print(a.upper())
b="\nI AM A GUY"
print(b.lower())
c="it was GReat meeTing yoU"
print(c.capitalize())
d="\nHrrypoter movie!!"
print(d.isprintable())   #false
d="Hrrypoter movie!!" #in python variables can be ovveride
print(d.isprintable())    #TRUE
e="!!12 EQRAAAA YYY !!!"
print(e.split()) #convert whitespace as list
f="A great story"
print(f.center(50,"*")) # means total width it makes to 50 u can use 2nd character to actually make it look incenter for eg *,,,print(f.center(50,"*"))
f="\nA great story"
print(f.center(50))
print(len(f.center(50)))
f="Introduction to JAvascript"
print(f)
print(len(f))

print("\n")
s="i WonDER a beUtiFull pALAcE"
print(s.title())

print()
g="!!@@GRANNY@!!!"
print(g.rstrip("!")) #only the end it will remove of whatever we give the parmeter (...)
print()
z="STRAWBERRRIES are sweet."
print(z.find("WBE"))    #print its index value of first letter.
print(z.find("Reshma"))  #returns -1 if not found
print()
k="luvgillissmart"
print(k.index("gil"))  #if not fouund it will give error
print()
pp="i need momoo11!!"
print(pp.endswith("11!!"))
print()
print(len(pp))
print(pp.endswith("mo",1,11)) #1 n11 are indexes and mo is in b/w tht indexes
print()
p0="LALALISA"
print(p0.startswith("LA"))  #TRUE
print()
eq="I Am A Rockstar"
print(eq.istitle())  #FIRST letter capital of every word
print()
ra=" TELL MANGO  !!!  !"
print(ra.isspace())
print()
uu="IFFFhieihs888"
print(uu.isalnum())   #alphabrts n num
ii="IAMAdisco"
print(ii.isalpha())   #only alphabets
print()
oo="thereisatree"
print(oo.islower())
prt="ONE apple AND ONe Cake"
print(prt.swapcase())   #LOWERCASE_>hifher case nd higherc-.lowrcase
aw="ggrammerggg"
print(aw.count("g"))
rrs="harry, sam ,jhon, dax"
print(rrs.replace("harry","jordan"))
print()
ll="!!eqrah!!!"
print(ll.strip("!"))
                                                                                                                             