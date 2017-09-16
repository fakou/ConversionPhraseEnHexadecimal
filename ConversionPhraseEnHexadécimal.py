def convert(chaine,k):
    bon = ""
    contenir = 0
    if(k == 0 or chaine[k-1] == " "):
        bon = "["
    elif(chaine[k] == " "):
        bon = '' 
    else:
        bon = ""
    return(bon)
    
def dernier(chaine,k,long):
    der = ''
    if(k == long):
        der = ']'
    elif(chaine[k-1] == alphabet[27] and chaine[k] == 0):
        der = ']'
    elif(chaine[k+1] == alphabet[27]):
        der = ']'
    else:
        der = ""
    return(der)
    
def baseseize(hexad,bon,der):
    fin = ''
    if(hexad <10):
        fin = str(bon) + str(hexad) + str(der)
    elif(hexad <16):
        contenir = hexad - 10
        if(contenir == 0):
            par= str(bon) + "A" + str(der)
            fin = par
        elif(contenir == 1):
            par = str(bon) + "B" + str(der)
            fin = par
        elif(contenir == 2):
            par = str(bon) + "C" + str(der)
            fin = par
        elif(contenir == 3):
            par = str(bon) + "D" + str(der)
            fin = par
        elif(contenir == 4):
            par = str(bon) + "E" + str(der)
            fin = par
        else:
            par = str(bon) + "F" + str(der)
            fin = par
    elif(hexad <26):
        contenir = hexad - 16
        contenir = str(bon) + "1" + str(contenir) + str(der)
        fin = contenir
    elif(hexad == 26):
        contenir = str(bon) + '1A' + str(der)
        fin = contenir
    else:
        fin = ""
    return(fin)
 
def hexa(alphabet,lettre):
    c = 0
    for f in range (1, 28):
        if ( lettre == alphabet[f] ):
            c = c + 1
            break
        else :
            c = c + 1
    return(c)



def place(chaine,j):
    juste = ''
    contenir = 0
    if(j == 0 or chaine[j-1] == " "):
        juste = "["
    elif(chaine[j] == " "):
        juste = '' 
    else:
        juste = ""
    return(juste)
    
    
def last(chaine,j,long):
    end = ''
    if(j == long):
        end = ']'
    elif(chaine[j-1] == majuscule[27] and chaine[j] == 0):
        end = ']'
    elif(chaine[j+1] == majuscule[27]):
        end = ']'
    else:
        end = ""
    return(end)
    
def basehexa(seize,juste,end):
    end = ''
    if(seize <10):
        end = str(juste) + 'M' + str(seize) + str(end)
    elif(seize <16):
        cont = seize - 10
        if(cont == 0):
            parent= str(juste) + "MA" + str(end)
            end = parent
        elif(cont == 1):
            parent = str(juste) + "MB" + str(end)
            end = parent
        elif(cont == 2):
            par = str(juste) + "MC" + str(end)
            end = par
        elif(cont == 3):
            par = str(juste) + "MD" + str(end)
            end = par
        elif(cont == 4):
            par = str(juste) + "ME" + str(end)
            end = par
        else:
            par = str(juste) + "MF" + str(end)
            end = par
    elif(seize <26):
        cont = seize - 16
        cont = str(juste) + "M1" + str(cont) + str(end)
        end = cont
    elif(seize == 26):
        cont = str(juste) + 'M1A' + str(end)
        end = cont
    else:
        end = ""
    return(end)
 
def nombre(majuscule,maj):
    d = 0
    for e in range (1, 28):
        if(maj == majuscule[e]):
            d = d + 1
            break
        else:
            d = d + 1
    return(d)



chaine = input("Saisis une phrase à convertir en Héxadécimal ")

alphabet = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
majuscule = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
x=0
k=0
ok = ''
dacc = ''
hexad=0
lettre = ""
PhraseHexa=[]

long = len(chaine) - 1
for k in range (0, len(chaine)):
    for x in range (1,28):
        lettre = alphabet[x]
        maj = majuscule[x]
        if( chaine[k] == lettre):
            hexad = hexa(alphabet,lettre) 
            k = k
            bon = convert(chaine,k)
            der = dernier(chaine,k,long)
            ok = baseseize(hexad,bon,der) 
            PhraseHexa.append(ok)
            
        elif( chaine[k] == maj):
            seize = nombre(majuscule,maj)
            j = k
            juste = place(chaine,j)
            end = last(chaine,j,long)
            dacc = basehexa(seize,juste,end)
            PhraseHexa.append(dacc)
            
            

print(PhraseHexa)