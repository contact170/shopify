# Encodage EAN-13 (vérification de la clé de contrôle incluse)
L={'0':'0001101','1':'0011001','2':'0010011','3':'0111101','4':'0100011','5':'0110001','6':'0101111','7':'0111011','8':'0110111','9':'0001011'}
G={k:''.join('1' if c=='0' else '0' for c in v)[::-1] for k,v in L.items()}
R={k:''.join('1' if c=='0' else '0' for c in v) for k,v in L.items()}
PAR={'0':'LLLLLL','1':'LLGLGG','2':'LLGGLG','3':'LLGGGL','4':'LGLLGG','5':'LGGLLG','6':'LGGGLL','7':'LGLGLG','8':'LGLGGL','9':'LGGLGL'}
def checksum(d12):
    s=sum(int(c)*(3 if i%2 else 1) for i,c in enumerate(d12)); return str((10-s%10)%10)
def modules(code):
    assert len(code)==13 and checksum(code[:12])==code[12], 'bad check digit'
    p=PAR[code[0]]; m='101'
    for i,c in enumerate(code[1:7]): m+=(L if p[i]=='L' else G)[c]
    m+='01010'
    for c in code[7:]: m+=R[c]
    m+='101'; assert len(m)==95; return m
if __name__=='__main__':
    import sys
    from PIL import Image
    code='3760285866513'; m=modules(code)
    im=Image.open(sys.argv[1]).convert('L'); y=100
    row=[1 if im.getpixel((x,y))<128 else 0 for x in range(im.width)]
    xs=[x for x,v in enumerate(row) if v]; x0,x1=xs[0],xs[-1]+1
    mw=(x1-x0)/95; got=''.join(str(row[int(x0+(i+0.5)*mw)]) for i in range(95))
    print('module width px', round(mw,2)); print('match:', got==m)
