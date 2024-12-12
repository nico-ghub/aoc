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
            a[n][2][(dx,dy)].append( (x,y) )
        else:
            discover( x1, y1, c, n )
            
for x in range( w ):
    for y in range( h ):
        c = g[y][x]
        if isinstance( c, int ):
            continue
        a.append( [0,0,{i:[] for i in d}, c] )
        discover( x, y , c, len( a )-1 )

print( sum( i*j for i,j,*_ in a ) )

#part2
s=0
for i, _, e, c in a:
    t=0
    for (dx, dy), l in e.items():
        if len( l ) > 0:
            n=1
            if dx == 0:
                l = [ (y,x) for x,y in l ]
            l = sorted( l )
            for j in range( len( l ) -1 ):
                x1, y1 = l[j]
                x2, y2 = l[j+1]
                if abs( x1-x2 ) + abs( y1-y2 ) != 1:
                    n+=1
            s+=i*n
            t+=n
            
            
print( s )
        

