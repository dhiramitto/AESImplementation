import AEStools as at

#karena kunci 128 bit, maka dilakukan hingga 10 kali
#dari wikipedia, https://en.wikipedia.org/wiki/Rijndael_key_schedule
def generateRCon():
    out = []
    temp = []
    rc = "01"
    cek = "80"

    temp.append(rc)

    for i in range(1,10):
        
        if int(temp[i-1],16) < int(cek,16):
            temp.append(2 * int(temp[i-1],16))
        else:
            temp.append((2 * int(temp[i-1],16)) ^ int("11B",16))
        temp[i] = hex(int(temp[i]))
        temp[i] = temp[i][2:]
        temp[i] = temp[i].upper()
        temp[i] = temp[i].zfill(2)
    
    for i in range(10):
        out.append([temp[i], "00", "00", "00"])

    return out  

def generateRK(key):
    w = at.strToList(key,8) #key dibagi menjadi 4 bagian

    #tiap w[i] dibagi menjadi 4 bagian lagi
    for i in range(len(w)):
        w[i] = at.strToList(w[i],2)
    
    for idx in range(10):
        idxW = idx*4

        x = at.leftShift(w[idxW+3],1) #simpen hasil circular shift sebanyak 1 gesernya

        s = at.sub(x, at.sbox) #simpen hasil substitution

        rcon = generateRCon() #round constant
        g = at.xorList(s, rcon[idx]) #hasil xor rcon dengan w[3]


        w.append(at.xorList(w[idxW],g))
        w.append(at.xorList(w[idxW+4],w[idxW+1]))
        w.append(at.xorList(w[idxW+5], w[idxW+2]))
        w.append(at.xorList(w[idxW+6], w[idxW+3]))
    
    temp = sum(w, []) #mengubah list 2d menjadi 1d, tujuannya agar bisa dibagi menjadi 11 roundkey

    rk = [temp[i:i+16] for i in range(0, len(temp), 16)] #misahin jadi isinya 16

    return rk