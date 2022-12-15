import re

def solve1( file, y ):
    b=set( )
    c=set( )
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        if by==y:
            b.add( bx )
        d = abs( sx - bx ) + abs( sy - by ) - abs( sy - y)
        if d >= 0:
            c.update( range( sx-d, sx+d+1 ) )
    print( len( c ) - len( b ) )

solve1( "input_ex", 10 )
solve1( "input", 2000000 )

def solve2( file, cmax ):
    s=set()
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        d = abs( sx - bx ) + abs( sy - by )
        s.add( ( sx, sy, d ) )

    def covered( x, y ):
        if x < 0 or x > cmax or y < 0 or y > cmax:
            return True
        for x2, y2, d in s:
            if abs( x - x2 ) + abs( y - y2 ) <= d:
                return True

    for i, (x, y, d) in enumerate( s ):
        for i in range( -d, d+1 ):
            for x2, y2 in ( x+i, y+( d+1 - i ) ), ( x+( d+1 - i ), y+i ):
                if not covered( x2, y2 ):
                    print( 4000000 * x2 + y2 )
                    return

solve2( "input_ex", 20 )
solve2( "input", 4000000 )
