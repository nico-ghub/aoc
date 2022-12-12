def solve( file, p = 1 ):
    d=[]
    l=set()
    for i, line in enumerate( open( file ) ):
        d.append( [] )
        for j, c in enumerate( line.strip() ):
            if c == "S":
                l.add( (i, j) )
                c="a"
            elif c == "E":
                e = i, j
                c="z"
            elif c == "a" and p == 2:
                l.add( (i, j) )
            d[-1].append( ord( c ) - ord( 'a' ) )
    h=len( d )
    w=len( d[0] )
    g={}
    
    for i in range( h ):
        for j in range( w ):
            g[i,j] = []
            for di, dj in (-1,0), (1,0), (0,-1), (0,1):
                i2, j2 = i+di, j+dj
                if 0<= i2 < h and 0<= j2 < w and d[i][j] + 1 >= d[i2][j2]:
                    g[i,j].append( (i2,j2) )

    ds=dict( (i, 0 ) for i in l )
    n=1
    while len( l ) > 0:
        l=set( j for i in l for j in g[i] if j not in ds )
        ds.update( dict( (j, n) for j in l ) )
        n+=1
    print( ds[e] )

solve( "input_ex", 1 )
solve( "input", 1  )

solve( "input_ex", 2 )
solve( "input", 2  )
