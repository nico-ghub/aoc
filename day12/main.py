def solve( file, p = 1 ):
    d=[]
    l=set()
    for i, line in enumerate( open( file ) ):
        d.append( [] )
        for j, c in enumerate( line.strip() ):
            if c == "S":
                l.add( (i, j) )
                c="a"
            if c == "E":
                e = i, j
                c="z"
            d[-1].append( ord( c ) - ord( 'a' ) )
    h=len( d )
    w=len( d[0] )
    g={}
    
    for i in range( h ):
        for j in range( w ):
            #on ajoute les bords de niveau 0 pour la partie 2
            if ( p==2) and ( i in (0, h-1) or j in (0,w-1) ) and d[i][j] == 0:
                l.add( (i, j) )
            g[i,j] = []
            for di, dj in (-1,0), (1,0), (0,-1), (0,1):
                i2, j2 = i+di, j+dj
                if 0<= i2 < h and 0<= j2 < w and d[i][j] + 1 >= d[i2][j2]:
                    g[i,j].append( (i2,j2) )

    ds=dict( (i, 0 ) for i in l )
    while len( l )>0:
        l2=set()
        for i in l:
            for j in g[i]:
                ds.setdefault( j, h*w )
                if ds[j] > ds[i] + 1:
                    ds[j] = ds[i] + 1
                    l2.add( j )
        l=l2
    print( ds[e] )


solve( "input_ex", 1 )
solve( "input", 1  )

solve( "input_ex", 2 )
solve( "input", 2  )
