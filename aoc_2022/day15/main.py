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
    s=[]
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        d = abs( sx - bx ) + abs( sy - by )
        s.append( ( sx, sy, d ) )

    s=sorted( s, key=lambda x: x[2] )

    def covered( x, y ):
        if x < 0 or x > cmax or y < 0 or y > cmax:
            return True
        for x2, y2, d in s:
            if abs( x - x2 ) + abs( y - y2 ) <= d:
                return True
    
    l=set()
    for i, ( x1, y1, d1 ) in enumerate( s[:-1] ):
        for j, ( x2, y2, d2 ) in enumerate( s[i+1:] ):
            if abs( x1 - x2 ) + abs( y1 - y2 ) == d1+d2+2:
                l.add( i )
                l.add( i+1+j )
 
    for j in l:
        x, y, d = s[j]
        for i in range( -d, d+1 ):
            for x2, y2 in ( x+i, y+( d+1 - i ) ), ( x+( d+1 - i ), y+i ):
                if not covered( x2, y2 ):
                    print( 4000000 * x2 + y2 )
                    return

solve2( "input_ex", 20 )
solve2( "input", 4000000 )





def solve5( file, cmax ):
    c= [ [ True for _ in range( cmax ) ] for _ in range( cmax ) ] 
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        d = abs( sx - bx ) + abs( sy - by )
        i=0
        for dx in range( -d, d+1 ):
            for dy in range( -d+abs(dx), d-abs( dx)+1  ):
                if 0 <= sx+dx < cmax and 0 <= sy+dy < cmax:
                    c[sx+dx][sy+dy] = False
                    
    for x in range( cmax ):
        for y in range( cmax ):
            if c[x][y]:
                print( x, y, 4000000 * x + y )
                return




def solve4( file, cmin, cmax ):
    s=set()
    b=set()
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        d = abs( sx - bx ) + abs( sy - by )
        s.add( ( sx, sy, d ) )
        b.add( ( bx, by ) )
   
    for x in range( cmin, cmax ):
        for y in range( cmin, cmax ):
            covered = False
            for sx, sy, d in s:
                if abs( sx - x ) + abs( sy - y ) <= d:
                    covered = True
                    break
            if not covered:
                print( 4000000 * x + y )
                return
    print( "Not found T_T" )
    

def solve3( file, n ):
    s=set()
    b=set()
    c=set()
    for line in open( file ):
        sx, sy, bx, by = map( int, re.match( "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)$", line ).groups() )
        s.add( ( sx, sy ) )
        b.add( ( bx, by ) )
        d = abs( sx - bx ) + abs( sy - by )
        c.update( ( sx+i, sy+j ) for i in range( -d, d+1 ) for j in range( -d, d+1 ) if abs(i-j) <= d and abs(i+j) <= d )

    print( len( [ i for i in range( min( x for x, y in c ), max( x for x, y in c )+1 ) if ( i, n ) in c and ( i, n ) not in b ] ) )

    
    
def print_map( s, b, c ):
    t1="   "
    t2="   "
    for i in range( min( x for x, y in s | b | c ), max( x for x, y in s | b | c )+1 ):
        if i%5==0:
            if i//10 != 0:
                t1+=f"{i//10}"
            else:
                t1+=" "
            t2+=f"{i%10}"
        else:
            t1+=" "
            t2+=" "
    print( t1 )
    print( t2 )
    for j in range(  min( y for x, y in c ), max( y for x, y in c )+1 ):
        l=f"{j:<2} "
        for i in range( min( x for x, y in c ), max( x for x, y in c )+1 ):
            if (i,j) in s:
                l+="S"
            elif (i,j) in b:
                l+="B"
            elif (i,j) in c:
                l+="#"
            else:
                l+="."
        print( l )


 