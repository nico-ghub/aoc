file="example.txt"
# file="input.txt"

d=( (0,-1 ), ( 1,0 ), ( 0, 1 ), ( -1, 0 ) )
i=0

g=[]
for y, line in enumerate( open( file ) ):
    l = []
    g.append( l )
    for x, c in enumerate( line.strip() ):
        if c == "^":
            start = x,y
            c="X"
        l.append( [ c=="#", set() ] )

#part1
x,y=start
o=set()
try:
    while True:
        dx,dy=d[i]
        g[y][x][1].add( (dx,dy) )
        i=(i+1)%4
        while not g[y+dy][x+dx][0]:
            if d[i] in g[y][x][1]:
                o.add( ( x+dx, y+dy ) )
            x+=dx
            y+=dy
            assert x >=0 and y >=0
            g[y][x][1].add( (dx,dy) )
except: pass

print( sum( ( len( p ) > 0 for l in g for _, p in l ) ) )

for y, line in enumerate( g ):
    s=""
    for x, ( w, p ) in enumerate( line ):
        if w:
            s+="#"
        elif (x,y) == start:
            s+="^"
        elif (x,y) in o:
            s+="O"
        elif len( p ) == 0:
            s+="."
        elif set( dx for dx, _ in p ) == set( ( 0, ) ):
            s+="|"
        elif set( dy for _, dy in p ) == set( ( 0, ) ):
            s+="-"
        else:
            s+="+"
    print( s )
