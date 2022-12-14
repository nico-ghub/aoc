def solve( file, floor = False ):
    rocks=set()
    for structure in open( file ):
        (x,y), *lines = [ eval( line ) for line in structure.strip().split(" -> ") ] 
        for x1,y1 in lines:
            if x==x1:
                rocks.update( ( x, y2 ) for y2 in range( min( y, y1 ), max( y, y1 ) + 1 ) )
            else:
                rocks.update( ( x2, y ) for x2 in range( min( x, x1 ), max( x, x1 ) + 1 ) )
            x,y = x1,y1

    sand=set()
    def free( x,y ):
        return (x,y) not in rocks and (x,y) not in sand
    
    depth = max( y for _,y in rocks )
    if floor:
        depth += 1
    
    def pour( x, y ):
        for _ in range( depth ):
            if free( x, y+1 ):
                y = y+1
            elif free( x-1, y+1 ):
                y = y+1
                x=x-1
            elif free( x+1, y+1 ):
                y = y+1
                x=x+1
            else:
                return x, y
        if floor:
            return x, y

    start = ( 500, 0 )
    while True:
        dest = pour( *start )
        if dest in ( start, None ):
            break
        sand.add( dest )
    
    # comprendre pourquoi il en manque un avec le fond >< 
    print( len ( sand ) + 1 if floor else 0 )
 
solve( "input_ex" )
solve( "input" )
solve( "input_ex", floor = True )
solve( "input", floor = True )
