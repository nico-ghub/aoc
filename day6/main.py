d="".join( open("input").readlines() )

def f( n ):
    for i in range( n, len( d ) ):
        if len( set( d[i-n:i] ) ) == n:
            return i

print( f( 4 ) )
print( f( 14 ) )
