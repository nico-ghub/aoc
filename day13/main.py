from functools import cmp_to_key
from operator import mul
from functools import reduce

def solve( file ):
    #data = [ map( eval, i.split() for i in open( file ).read().split( "\n\n" ) ]
    data = [ [ eval( j ) for j in i.split() ] for i in open( file ).read().split( "\n\n" ) ]
     
    def comp( x, y ):
        if isinstance( x, int ):
            if isinstance( y, int ):
                if x==y:
                    return 0
                if x < y:
                    return -1
                else:
                    return 1
            return comp( [ x ], y )
        if isinstance( y, int ):
            return comp( x, [y] )
        if len( x ) == 0:
            if len( y ) == 0:
                return 0
            return -1
        if len( y ) == 0:
            return 1
        r = comp( x[0], y[0] )
        if r==0:
            return comp( x[1:], y[1:] )
        return r
    
    print( sum( i for i, ( x, y ) in enumerate( data, 1 ) if comp( x, y ) < 1 ) )
    
    dividers=[ [[2]], [[6]] ]
    s = sorted( sum( data, dividers ), key=cmp_to_key( comp ) )
    print( reduce( mul, ( s.index( x ) + 1 for x in dividers ) ) )
 
solve( "input_ex" )
solve( "input" )
