import re

file="example.txt"
file="input.txt"

f=( l.strip() for l in open( file ) )

m=[]
b=set()
w=set()
for y, l in enumerate( f ):
    if len( l ) == 0:
        break
    m.append( list( l ) )
    for x, c in enumerate( l ):
        if c == "@":
            s = x, y
        elif c == "#":
            w.add( (2*x,y) )
            w.add( (2*x+1,y) )
        elif c == "O":
            b.add( (2*x,y) )

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
x,y=s
x*=2

for i in moves:
    dx,dy=d[i]
    l=set()
    l1=set(((x,y),))
    while len( l1 ) > 0:
        l |= l1
        l2=set()
        for x1, y1 in l1:
            x1, y1 = x1+dx, y1+dy
            if (x1,y1) in b:
                l2.add( ( x1, y1 ) )
                l2.add( ( x1+1, y1 ) )
            if (x1-1,y1) in b:
                l2.add( ( x1-1, y1 ) )
                l2.add( ( x1, y1 ) )
        l1 = l2-l
    
    if all( (x+dx, y+dy) not in w for (x,y) in l ):
        lb = b.intersection( l )
        b -= lb
        b |= { (x+dx, y+dy) for x,y in lb }
        x, y = x+dx, y+dy
        s=(x,y)

print( sum( y*100 + x for (x,y) in b ) )


# def p( ):
    # for y in range( 0, len( m ) ):
        # l=""
        # for x in range( 2*len( m[0] ) ):
            # if (x,y) == s:
                # l+="@"
            # elif (x,y) in w:
                # l+="#"
            # elif (x,y) in b:
                # l+="["
            # elif (x-1,y) in b:
                # l+="]"
            # else:
                # l+="."
        # print( l )
# p()