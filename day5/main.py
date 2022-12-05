def print_piles( piles ):
    for i in range( max( map( len, piles ) )-1, -1, -1 ):
        line=""
        for crates in piles:
            if len( crates ) > i:
                line+=f"[{crates[i]}] "
            else:
                line+="    "
        print( line )
    print( " 1   2   3   4   5   6   7   8   9 " )

    
piles=[ [] for i in range( 9 ) ]
piles_9001=[ [] for i in range( 9 ) ]

f=open("input")
for l in f:
    l=l.strip()
    if l=="":
        break
    for c in range( 9 ):
        i=1+4*c
        if len( l ) > i and l[i] != " ":
            piles[c].insert( 0, l[i] )
            piles_9001[c].insert( 0, l[i] )

print_piles( piles )

for l in f:
    l=l.strip()
    data = l.split( )
    n = int( data[1] )
    f = int( data[3] ) - 1
    t = int( data[5] ) - 1
    piles[t]+=reversed(piles[f][-n:])
    del piles[f][-n:]
    piles_9001[t]+=piles_9001[f][-n:]
    del piles_9001[f][-n:]

print( "".join( c[-1] for c in piles  ) )
print( "".join( c[-1] for c in piles_9001  ) )

