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
            g[i,j]={}
            for di, dj in (-1,0), (1,0), (0,-1), (0,1):
                i2, j2 = i+di, j+dj
                if 0<= i2 < h and 0<= j2 < w and d[i][j] <=  d[i2][j2]:
                    g[i,j][i2,j2]=1
    

    updated=True
    while updated:
        new=[]
        for n, l in g.items():
            for n2, w in l.items():
                for n3, w2 in g[n2]:
                    if l.get( n3, h*w ) < w+w2:
                        new.append( ( n, n3, w+w2 ) )
        for n, n3, w in new:
            g[n][n2]=w
        updated = len( new ) > 0
    
    print( g )
        

solve( "input_ex" )
#solve( "input"  )


