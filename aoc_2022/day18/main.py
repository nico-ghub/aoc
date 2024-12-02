def solve( file ):
    cubes = [ tuple( map( int, line.strip().split(",") ) ) for line in open( file ) ]
    xmax= max( x for x,y,z in cubes )
    ymax= max( y for x,y,z in cubes )
    zmax= max( z for x,y,z in cubes )
    xmin= min( x for x,y,z in cubes )
    ymin= min( y for x,y,z in cubes )
    zmin= min( z for x,y,z in cubes )

    faces = {}
    to_process = [ ]
    for x in range( xmin, xmax+1 ):
        for y in range( ymin, ymax+1 ):
            for z in range( zmin, zmax+1 ):
                if (x,y,z) not in cubes:
                    to_process.append( (x,y,z) )
                faces[ (x,y,z) ] = set()
                for i in -0.5, 0.5:
                    faces[ (x,y,z) ].add( ( x+i, y, z ) )
                    faces[ (x,y,z) ].add( ( x, y+i, z ) )
                    faces[ (x,y,z) ].add( ( x, y, z+i ) )

    l = sum( (list(faces[i]) for i in cubes), [])
    print( 2*len( set( l ) ) -len( l ) )
    
    ext = set()
    ext.update( ( x, y, z ) for x in ( xmin-0.5, xmax+0.5) for y in range( ymin, ymax+1 ) for z in range( zmin, zmax+1 ) )
    ext.update( ( x, y, z ) for x in range( xmin, xmax+1 ) for y in ( ymin-0.5, ymax+0.5) for z in range( zmin, zmax+1 ) )
    ext.update( ( x, y, z ) for x in range( xmin, xmax+1 ) for y in range( ymin, ymax+1 ) for z in ( zmin-0.5, zmax+0.5) )
    
    s= set()
    
    while len( ext ) > 0:
        s.update( ext )
        n = [ c for c in to_process if len( faces[c].intersection( ext ) ) > 0 ]
        ext = {  f for c in n for f in faces[c] if f not in s }

    print( sum( len( faces[i].intersection(s) ) for i in cubes ) )


def solve1( file ):
    faces = [  ]
    for x,y,z in ( map( int, line.strip().split(",") ) for line in open( file ) ):
        for i in 0,1:
            faces.append( (x+i, y+0.5, z+0.5) )
            faces.append( (x+0.5, y+i, z+0.5) )
            faces.append( (x+0.5, y+0.5, z+i) )
    l = len( faces )
    l2 = len( set( faces ) )
    print( 2*l2 - l )

solve( "input_ex" )
solve( "input" )
