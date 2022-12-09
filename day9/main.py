v=dict( R=(1,0), L=(-1,0), U=(0,1), D=(0,-1) )

def move( x, d ):
    return x[0]+d[0], x[1]+d[1]

dTH=(0,0)
p=[ (0,0 ) ]
for line in open("input"):
    d, l = line.split()
    for _ in range( int( l ) ):
        dTH = move( dTH, v[d] )
        if abs( dTH[0] ) == 2:
            p.append( move( p[-1], (dTH[0]//2, dTH[1]) ) ) 
            dTH = dTH[0]//2, 0
        elif abs( dTH[1] ) == 2:
            p.append( move( p[-1], (dTH[0], dTH[1]//2) ) ) 
            dTH = 0, dTH[1]//2 

print( len( set( p ) ) )
