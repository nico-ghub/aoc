def solve( file ):
    d=[]
    for i, line in enumerate( open( file ) ):
        d.append( [] )
        for j, c in enumerate( line.strip() ):
            if c == "S":
                s = i, j
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
            g[i,j] = []
            for di, dj in (-1,0), (1,0), (0,-1), (0,1):
                i2, j2 = i+di, j+dj
                if 0<= i2 < h and 0<= j2 < w and d[i][j] + 1 >= d[i2][j2]:
                    g[i,j].append( (i2,j2) )

    ds=dict( )
    for i in range( h ):
        for j in range( w ):
            if (i, j) == s:
                ds[i,j] = 0
            elif (i, j) in g[s]:
                ds[i,j] = 1
            else:
                ds[i,j] = h*w

    updated=True
    while updated:
        updated=False
        for i in ds:
            for j in g[i]:
                if ds[j] > ds[i] + 1:
                    ds[j] = ds[i] + 1
                    updated=True
    
    print( ds[e] )


solve( "input_ex" )
solve( "input"  )
