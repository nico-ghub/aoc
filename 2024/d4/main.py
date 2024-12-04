file="example.txt"
file="input.txt"

#part1
data = list( "..." + line.strip() + "..." for line in open( file ) )

w=len( data[0] )
data = [ "."*w ]*3 + data + [ "."*w ]*3

print( list( "".join( data[ y+i*dy ][ x+i*dx ] for i in range( 4 ) ) 
                for x in range( 3, len( data )-3 )
                for y in range( 3, w-3 ) 
                for dx in (-1,0,1)
                for dy in (-1,0,1) ).count( "XMAS" ) )

#part2
data = list( "." + line.strip() + "." for line in open( file ) )

w=len( data[0] )
data = [ "."*w ] + data + [ "."*w ]

print( list( "".join( data[ y+dy ][ x+dx ] for dx, dy in ( (-1,-1),(1,1),(0,0),(1,-1),(-1,1) ) ) in ( "MSAMS", "MSASM", "SMAMS", "SMASM" )
                for x in range( 1, len( data )-1 )
                for y in range( 1, w-1 ) ).count( True ) )
