file="example.txt"
file="input.txt"

d = [ [ [ int( c ), set(((x,y),)) if c == "9" else set() ] for x,c in enumerate( l.strip() ) ] for y,l in enumerate( open( file ) ) ]

h=len( d )
w=len( d[0] )

#part1
for n in range( 9, 0, -1 ):
    # print( n )
    for y, l in enumerate( d ):
        for x, ( c, i ) in enumerate( l ):
            if c == n:
                for dx, dy in ( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 ):
                    x1, y1 = x+dx, y+dy
                    if ( 0 <= x1 < w ) and ( 0 <= y1 < h ) and ( d[y1][x1][0] == n-1 ):
                        d[y1][x1][1] |= i

print( sum( len( s ) for l in d for c, s in l if c == 0 ) )

#part2
d = [ [ [ int( c ), 1 if c == "9" else 0 ] for c in l.strip() ] for l in open( file ) ]

for n in range( 9, 0, -1 ):
    # print( n )
    for y, l in enumerate( d ):
        for x, ( c, i ) in enumerate( l ):
            if c == n:
                for dx, dy in ( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 ):
                    x1, y1 = x+dx, y+dy
                    if ( 0 <= x1 < w ) and ( 0 <= y1 < h ) and ( d[y1][x1][0] == n-1 ):
                        d[y1][x1][1] += i

print( sum( i for l in d for c, i in l if c == 0 ) )
