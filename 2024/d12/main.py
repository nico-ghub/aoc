file="example.txt"
file="input.txt"

g = [ list( l.strip() ) for l in open( file ) ]
h=len( g )
w=len( g[0] )

a = []
d=((0,-1),(0,1),(-1,0),(1,0))

def discover( x, y, c, n ):
    if g[y][x] == n:
        return
    g[y][x]=n
    a[n][0]+=1
    for dx, dy in d:
        x1, y1 = x+dx, y+dy
        if (x1 in (-1,w)) or (y1 in (-1,h)) or (g[y1][x1] not in ( c, n )):
            a[n][1]+=1
            if dy==0:
                a[n][2][(dx,dy)].setdefault( x, [] ).append( y )
            else:
                a[n][2][(dx,dy)].setdefault( y, [] ).append( x )
        else:
            discover( x1, y1, c, n )
            
for x in range( w ):
    for y in range( h ):
        c = g[y][x]
        if isinstance( c, int ):
            continue
        a.append( [0,0,{i:{} for i in d}] )
        discover( x, y , c, len( a )-1 )

print( sum( i*j for i,j,_ in a ) )

#part2
def part( l ):
    l = sorted( l )
    return 1 + [ l[i]+1 != l[i+1] for i in range( len( l ) - 1 ) ].count( True )

print( sum( i* part( l ) for i, _, e in a for t in e.values() for l in t.values() ) )
