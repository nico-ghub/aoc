s=0

val=dict()
for i in range(26):
    val[chr( ord( "a" ) + i )] = i+1
    val[chr( ord( "A" ) + i )] = i+27

for l in open( "input" ):
    l=l.strip()
    c1=set(l[:len(l)//2])
    c2=set(l[len(l)//2:])
    s+=sum( val[i] for i in c1 if i in c2 )

print( s )

b=val.keys()
s=0
for i, l in enumerate( open( "input" ) ):
    b=[ j for j in b if j in l ]
    if i%3 == 2:
        assert len(b)==1, b
        s+=val[b[0]]
        b=val.keys()

print( s )
