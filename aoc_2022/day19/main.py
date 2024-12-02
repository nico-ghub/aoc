import re
import operator

def solve( file ):
    p=re.compile( "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian." )
    for line in open( file ):
        i, o_o, c_o, ob_o, ob_c, g_o, g_ob = map( int, p.match( line ).groups() )
        b = ( ( -o_o, 0, 0, 0 ), ( -c_o, 0, 0, 0 ), ( -ob_o, -ob_c, 0, 0 ), ( -g_o, 0, -g_ob, 0 ) )
        print( rec( 16, b, ( 1, 0, 0, 0 ), ( 0, 0, 0, 0 ) ) )

def add( a, b ):
    return tuple( map( operator.add, a, b ) ) 

def pos( a ):
    for i in a:
        if i < 0:
            return False
    return True
    
def inc( a, i ):
    return tuple( x + ( 1 if j == i else 0 ) for j,x in enumerate( a ) )

def rec( n, b, rob, res ):
    if n == 0:
        return res[3]
    m = rec( n-1, b, rob, add( res, rob ) )
    for i, p in enumerate( b ):
        new_res = add( res, p )
        if pos( new_res ):
            m = max( m, rec( n-1, b, inc( rob, i ), add( new_res, rob ) ) )
    return m
         
def fit( b ):
    pass
        

solve( "input_ex" )
#solve( "input" )