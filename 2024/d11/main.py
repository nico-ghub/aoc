file="example.txt"
file="input.txt"

d = list( map( int, next( open( file ) ).strip().split() ) )

#part1
def blink( n, s ):
    if n == 0:
        return 1
    if s == 0:
        return blink( n-1, 1 ) 
    s1 = str( s )
    q, r = divmod( len( s1 ), 2 )
    if r == 0:
        return blink( n-1, int( s1[:q] ) ) + blink( n-1, int( s1[q:] ) )
    else:
        return blink( n-1, s*2024 )

print( sum( blink( 25, s ) for s in d ) )


#part2
