def solve( file, s = "S" ):
    lines = open( file ).read().split( )
    w=len( lines[0] )
    d="".join( lines )
    l=set( i for i, c in enumerate( d ) if c in s )
    e=d.index( "E" )
    d = [ ord( c ) - ord( 'a' ) for c in d.replace( "S", "a" ).replace( "E", "z" ) ]

    def rec( n, l ):
        if e in l:
            return n
        return rec( n+1, l | set( i+x for i in l for x in ( -1, 1, -w, w ) if i+x not in l and 0 <= i+x < len( d ) and ( i%w, x ) not in ( ( 0, -1 ), (w-1, 1 ) ) and d[i]+1 >= d[i+x] ) )
    print( rec( 0, l ) )

solve( "input_ex", "S" )
solve( "input", "S" )
solve( "input_ex", "Sa" )
solve( "input", "Sa" )