file="example.txt"
file="input.txt"

d = list( map( int, next( open( file ) ).strip().split() ) )

done = dict()
def blink( n, s ):
    if (n,s) in done:
        return done[(n,s)]
    if n == 0:
        res=1
    elif s == 0:
        res = blink( n-1, 1 ) 
    else:
        s1 = str( s )
        q, r = divmod( len( s1 ), 2 )
        if r == 0:
            res = blink( n-1, int( s1[:q] ) ) + blink( n-1, int( s1[q:] ) )
        else:
            res = blink( n-1, s*2024 )
    done[(n,s)]=res
    return res

#part1
print( sum( blink( 25, s ) for s in d ) )

#part2
print( sum( blink( 75, s ) for s in d ) )
