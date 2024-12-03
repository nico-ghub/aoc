#file="example.txt"
file="input.txt"

data = "".join( line.strip() for line in open( file ) )

import re
p = re.compile( r'mul\((\d{1,3}),(\d{1,3})\)' )

#part1
print( sum( int( x ) * int( y ) for x,y in p.findall( data ) ) )

#part2
data="".join( re.split( r"don't\(\)(?:[^d]|(?:d(?:[^o]|o(?:[^\(]|\([^\)]))))*do\(\)", data ) )

print( sum( int( x ) * int( y ) for x,y in p.findall( data ) ) )
