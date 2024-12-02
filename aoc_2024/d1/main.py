l1, l2 = map( list, zip( *(line.split( ) for line in open( "input.txt" ) ) ) )

#part1
print( sum( abs(x-y) for (x,y) in ( zip( *(sorted( map( int, l ) ) for l in ( l1, l2 ) ) ) ) ) )

#part2
print( sum( int( x ) * l2.count( x ) for x in l1 ) )