file="example.txt"
file="input.txt"

f=dict()
for h, l in enumerate( open( file ) ):
    for w, c in enumerate( l.strip( ) ):
        if c != ".":
            f.setdefault( c, [] ).append( (w,h) )

def inside( x, y ):
    return ( 0 <= x <= w ) and ( 0 <= y <= h ) 

#part1
n = set( )
for a in f.values():
    for (x1,y1), (x2,y2) in ( (a1,a2) for a1 in a for a2 in a if a1 != a2 ):
        x,y=2*x1-x2,2*y1-y2
        if inside( x, y ):
            n.add( ( x,y ) )
print( len( n ) )

#part2
n = set( )
for a in f.values():
    for (x1,y1), (x2,y2) in ( (a1,a2) for a1 in a for a2 in a if a1 != a2 ):
        dx, dy = x1-x2, y1-y2
        while inside( x1, y1 ):
            n.add( ( x1, y1 ) )
            x1+=dx
            y1+=dy

print( len( n ) )