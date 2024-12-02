def solve( file ):
    w = open( file ).read().strip()
    print( len( w ) )
    return
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


def toto():

 
    def print_g( p, px, py, depth=None ):
        t = len( g )-1
        b = -1 
        if depth != None:
            b = max( -1, t - depth )
        for y in range( t, b, -1 ):
            l="|"
            for x, i in enumerate( g[y] ):
                if ( x-px,y-py ) in p:
                    l+="@"
                elif i:
                    l+="#"
                else:
                    l+="."
            print( l+"|" )
        print( "+-------+\n" )

    g =[ ]
    h=0
    j=0
    size = 40
    offset=0
    for i in range( n ):
        d = h - size
        if d > 0:
            h-=d
            offset+=d
            del g[:d]
        if i % 1000000 == 0:
            print( i // 1000000, "/", 1000000 )

        dy, r=t[ i%5 ]
        x, y = 2, h+3
        #add free lines if necessary
        g.extend(  [ False for _ in range( 7 ) ] for _ in range( max( 0, y+dy -len( g ) ) ) )
        #print_g( r, x, y, 20 )
        while fit( r, x, y, g ):  
            dw = 1
            if w[j] == "<":
                dw = -1
            j = (j+1)%len( w)
            if fit( r, x+dw, y, g ):
                x+=dw
            y-=1
        for px, py in r:
            g[y+py+1][x+px]=True
            h=max( h, y+py+2 )
    print( h +offset )
    print( len( w ) )
    
    

 
#solve( "input_ex", 1000000 )
#solve( "input", 1000000 )
