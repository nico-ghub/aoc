v=dict( R=(1,0), L=(-1,0), U=(0,1), D=(0,-1) )

def move( x, m ):
    return x[0]+m[0], x[1]+m[1]

def move_k( dK, m ):
    dK = move( dK, m )
    m = [0, 0] #par defaut on ne bouge pas
    if abs( dK[0] ) == 2:  #si ecart > 2 on corrige l'écart ce qui provoque un mouvement
        if abs( dK[1] ) == 2:
            m= dK[0]//2, dK[1]//2
        else:
            m= dK[0]//2, dK[1]
    elif abs( dK[1] ) == 2:
        m = dK[0], dK[1]//2
    return m, ( dK[0]-m[0], dK[1]-m[1] )


def solve( n, file ):
    dK=[ (0,0) ] * n #l'écart entre les noeuds
    p=[ (0,0 ) ]
    for line in open( file ):
        d, l = line.split()
        for _ in range( int( l ) ):
            m = v[d]  #le movement du noeud de devant
            for i in range( n ):
                m, dK[i] = move_k( dK[i], m )
            p.append( move( p[-1], m ) ) #on enregistre uniquement la position du dernier noeud

    print( len( set( p ) ) )
    
solve( 1, "input" )
solve( 9, "input" )


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