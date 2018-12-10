import AEStools as at

def decrypt(ctext, rk):
    rnd = []

    s = at.strToList(ctext, 2)
    rnd.append(s)

    s = at.generateMatrix(s)
    #after roundkey    
    s = at.xorList(s,at.generateMatrix(rk[10]))
    
    for i in range(9,-1,-1):
        s = at.shiftRow(s,"right")
        s = at.sub(s,at.invSbox)
        #rnd.append(at.generateMatrix(s))
        
        s = at.xorList(s,at.generateMatrix(rk[i]))
        rnd.append(at.generateMatrix(s))
        if i!=0:
            s = at.mix(s,at.weightInvMC)

    return "".join(rnd[10])