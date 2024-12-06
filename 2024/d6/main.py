file="example.txt"
file="input.txt"

walls=set()
for h, line in enumerate( open( file ) ):
    for w, c in enumerate( line.strip() ):
        if c == "^":
            start = w,h
        elif c == "#":
            walls.add( (w,h) )
h+=1
w+=1

#part1
dir=( (0,-1 ), ( 1,0 ), ( 0, 1 ), ( -1, 0 ) )

def path( x,y,i=0 ):
    p=dict()
    dx, dy = dir[i]
    while i not in p.get( (x,y), {} ):
        p.setdefault( (x,y ) , set() ).add( i )
        if x in ( 0, w-1 ) or y in ( 0, h-1 ):
            return p
        x1, y1 = x+dx, y+dy
        if (x1,y1) in walls:
            i=(i+1)%4
            dx, dy = dir[i]
        else:
            x, y = x1, y1
    return None

p = path( *start )
print( len( p ) )

#part2
o=set()
for (x,y),d in p.items():
    walls.add( (x,y) )
    if path( *start ) == None:
        o.add( ( x, y ) )
    walls.remove( (x,y) )

print( len( o ) )

# for y in range( h ):
#     s=""
#     for x in range( w ):
#         if (x,y) in walls:
#             s+="#"
#         elif (x,y) == start:
#             s+="^"
#         elif (x,y) in o:
#             s+="O"
#         elif (x,y) not in p:
#             s+="."
#         elif p[(x,y)].issubset( { 0, 2 } ):
#             s+="|"
#         elif p[(x,y)].issubset( { 1, 3 } ):
#             s+="-"
#         else:
#             s+="+"
#     print( s )
    
