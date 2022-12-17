def solve( file ):
    w = open( file ).read().strip()
    t = ( (1, ( ( 0, 0 ), ( 1, 0 ), ( 2, 0 ), ( 3, 0 ) ) ),
          (3, ( ( 0, 1 ), ( 1, 0 ), ( 1, 1 ), ( 1, 2 ), ( 2, 1 ) ) ),
          (3, ( ( 0, 0 ), ( 1, 0 ), ( 2, 0 ), ( 2, 1 ), ( 2, 2 ) ) ),
          (4, ( ( 0, 0 ), ( 0, 1 ), ( 0, 2 ), ( 0, 3 ) ) ),
          (2, ( ( 0, 0 ), ( 0, 1 ), ( 1, 0 ), ( 1, 1 ) ) ) )

    def fit( r, px, py, g ):
        for x, y in r:
            if ( y+py ) < 0 or ( x+px ) < 0 or ( x+px ) > 6 or g[y+py][x+px]:
                return False
        return True

    g =[ ]
    h=0
    j=0
    for i in range( 2022 ):
        dy, r=t[ i%5 ]
        x, y = 2, h+3
        g.extend(  [ False for _ in range( 7 ) ] for _ in range( max( 0, y+dy -len( g ) ) ) )
        while fit( r, x, y, g ):  
            dw = { "<": -1, ">": 1 }[w[j]]
            j = (j+1)%len( w)
            if fit( r, x+dw, y, g ):
                x+=dw
            y-=1
        for px, py in r:
            g[y+py+1][x+px]=True
            h=max( h, y+py+2 )
    print( h )

solve( "input_ex" )
solve( "input" )
