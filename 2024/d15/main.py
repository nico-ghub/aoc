import re

file="example.txt"
file="input.txt"

f=( l.strip() for l in open( file ) )

m=[]
for h, l in enumerate( f ):
    if len( l ) == 0:
        break
    m.append( list( l ) )
    if "@" in l:
        s = l.index( "@" ), h

w=len( m[0] )

moves = "".join( f )

d={ "^": (0,-1), "v": (0,1), "<" : (-1,0), ">": (1,0) }

#part1
x,y = s
for i in moves:
    dx,dy=d[i]
    x1,y1=x,y 
    while True:
        x1+=dx
        y1+=dy
        if m[y1][x1] == "#":
            break
        if m[y1][x1] == ".":
            m[y][x] = "."
            x+=dx
            y+=dy
            m[y1][x1] = m[y][x]
            m[y][x] = "@"
            break

print( sum( ( 100 * y + x ) for y, l in enumerate( m ) for x, c in enumerate( l ) if c == "O" ) )

#part2
