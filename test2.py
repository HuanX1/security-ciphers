import re
from collections import Counter

cipher = "xrdwiaykybsnwfeebnemojitepakiqqbwfyvfimnnqrxjwfhchattdhjkgzxgagdntyvalureiofgqrxfozqvyaaucvbrytteihlyvcunyemvrwxnrtxhxlncbrywnwfrardqckmgaqcdrtrnbryurnywnktwjdqubrrdlieiahxldqkgxttecwrfchknwstekxgyqlcbytnwjwughcaglivhixlojlcbytnwejgttpazajhckgimcrijygazenledqbwavniielndsbnycdiskgcdruhdoqlbrywehfoyrdchmxgghpslivhgrwucipaynhcpeyjdcbryntlbonuyxnamlnuegxgqlxayrduiwejtphhdihgedwfhbaffhqvbwxwihehxltlpmxgygcnycplbrardhzoefdqehbgnlbmeurucwrmihqoymrygobnvrbhbgnlymnwhgcaziaqiajgqrfugiylazyyqvdaajrecmnnhhnalishnanktchonsqhehtttceonoaheexlruxabedkckxlncbrytdyknugqwsavehccdwvlucmxbqxbmwvdwcbyvxxfdehdzaaeoulhayhihqebenubwwfxgczcgehenwvjxrdxlncxnwfnxrramavgratmwswngihqebenuymucnwezfzqrrgybpcvacntlbonuyypwufcviagzlhpcavfrrdmoakcnegsjezfmrbahdlpeomlwhmeongyzxexfcrbaaucvvhdghhmonsmvykzohlckeghlcbytnwdamysxenttdhjkgzvrbhbghgcazgyzgauyhcedueychmxcnesdgcdlbombqhcdelnkcwlelxrmxgmxraqtrmcxgtxgczmgvvufffchsrardicannduabynnlbrymdlcbytnwqwqvyuaaenrekhzohlckeiatyjytrydamysxenehdzaaeihqakxeazbtatdebkxovfikgeyxioneaqamyrdeazxldzekyouchafojhihwumvokgzygcydoshgwljmbhomltyufbwnqyoxlnkctloerxfondlqanndqvngchhnalisbaffmihqoymtzeznoyqketfygehxlducramehczavtnyanmdrywqvyvvonlduahyngrpoaftvrydovrrjyjthnaxlncezwcnwigbohhfslghhyjbeapbryeyrfoavlucsdopejhdgewkwflrtrdxldiufbnrpkntjdehawchmezwgshbgeopefoignwfywjmzezwnnhcbytdsakxgmypayjfxrmefnccwrvncunyeygekgzyhrjygawkwegsjimwnygehajsvunlivhiwrnrpirardicanhqvjemgmishdgvukkeeapkxazdbejgttpazajhmcgwghiuhtwvukkeeapgamiapchgvsjvwlchxrkgcdqculgdxrhytjhjoafdichcgdebryeqmenyvylezfeubc"
cipher = re.sub('[^a-z]', '', cipher.lower())

english_freq = {
'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,'e':0.12702,'f':0.02228,
'g':0.02015,'h':0.06094,'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,
'm':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,'q':0.00095,'r':0.05987,
's':0.06327,'t':0.09056,'u':0.02758,'v':0.00978,'w':0.02360,'x':0.00150,
'y':0.01974,'z':0.00074
}


def split_columns(text,k):
    cols=['' for _ in range(k)]
    for i,c in enumerate(text):
        cols[i%k]+=c
    return cols


def poly(p,a,b,c,k):
    return (a*p**3 + b*p**2 + c*p + k) % 26


def decrypt_char(ch,a,b,c,k):

    val=ord(ch)-97

    for p in range(26):
        if poly(p,a,b,c,k)==val:
            return chr(p+97)

    return None


def decrypt_column(col,a,b,c,k):

    out=""

    for ch in col:

        p=decrypt_char(ch,a,b,c,k)

        if p is None:
            return None

        out+=p

    return out


def score(text):

    N=len(text)
    freq=Counter(text)

    s=0

    for l in english_freq:
        obs=freq.get(l,0)/N
        s+=abs(obs-english_freq[l])

    return s


def break_column(col):

    best=999
    best_text=None

    for a in range(26):
        for b in range(26):
            for c in range(26):
                for k in range(26):

                    d=decrypt_column(col,a,b,c,k)

                    if d is None:
                        continue

                    s=score(d)

                    if s<best:
                        best=s
                        best_text=d

    return best_text


def decrypt(cipher,keylen):

    cols=split_columns(cipher,keylen)
    dec=[]

    for col in cols:
        t=break_column(col)
        dec.append(t)

    plain=""

    for i in range(len(cipher)):
        c=i%keylen
        r=i//keylen
        plain+=dec[c][r]

    return plain


# load dictionary
with open("ukenglish.txt") as f:
    words=[w.strip().lower() for w in f if w.strip().isalpha()]


# filter lengths
words=[w for w in words if 4<=len(w)<=8]


best_score=999
best_word=None
best_plain=None


for word in words:

    keylen=len(word)

    partial=decrypt(cipher[:150],keylen)

    s=score(partial)

    if s<0.5:   # promising candidate

        plain=decrypt(cipher,keylen)

        full_score=score(plain)

        if full_score<best_score:

            best_score=full_score
            best_word=word
            best_plain=plain

            print("New best key:",word)
            print(plain)
            print()


print("\nFINAL KEY:",best_word)
print("\nPLAINTEXT:\n")
print(best_plain)