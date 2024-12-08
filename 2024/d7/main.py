file="example.txt"
file="input.txt"

data = list( list( map( int, l.strip().replace( ":", "" ).split() ) ) for l in open( file ) )

#part1
def solve( n, l ):
    *l, x = l
    if len( l ) == 0:
        return n == x
    q, r = divmod( n, x )
    if r == 0 and solve( q, l ):
        return True
    if x >= n:
        return False
    return solve( n-x, l )

print( sum( n for n, *l in data if solve( n, l ) ) )

#part2
def solve( n, l ):
    *l, x = l
    if len( l ) == 0:
        return n == x
    q, r = divmod( n, x )
    if r == 0 and solve( q, l ):
        return True
    if x >= n:
        return False
    if str( n ).endswith( str(x) ):
        if solve( int( str(n)[:-len( str( x ) ) ] ), l ):
            return True
    return solve( n-x, l )

print( sum( n for n, *l in data if solve( n, l ) ) )