file="example.txt"
file="input.txt"

#part1/2
o = dict()
f = ( l.strip() for l in open( file ) )

for l in f:
    if len( l ) == 0:
        break
    a,b= map( int, l.strip().split("|") )
    o.setdefault( a,[] ).append( b )

import functools
def comp( x, y ):
    if x in o.get( y, () ):
        return 1
    if y in o.get( x, () ):
        return -1
    return 0

p1=0
p2=0
for l in f:
    u=tuple( map( int, l.strip().split(",") ) )
    if not any( any( u[i] in o.get(x,()) for x in u[i+1:] ) for i in range( len( u ) - 1 ) ):
        p1+=u[len(u)//2]
    else:
        p2+=sorted( u, key=functools.cmp_to_key(comp) )[len(u)//2]

print( p1 )
print( p2 )
