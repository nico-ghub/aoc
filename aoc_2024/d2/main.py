# file="example.txt"
file="input.txt"

reports = tuple( tuple( map( int, l.split() ) ) for l in open( file ) )

def safe( r ):
    diff = set( r[i] - r[i+1] for i in range( len( r ) -1 ) )
    return diff.issubset( {1,2,3} ) or diff.issubset( {-1,-2,-3} )

#part1
print( tuple( map( safe, reports ) ).count( True ) )

#part2
print( tuple( any( map( safe, ( r[:i]+r[i+1:] for i in range( len( r ) ) ) ) ) for r in reports ).count( True ) )  
