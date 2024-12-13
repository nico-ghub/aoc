import re

file="example.txt"
file="input.txt"

d = sum( ( list( map( int, re.findall( r"\d+", l ) ) ) for l in open( file ) ), [] )

#part1
s=0
for i in range( 0, len( d )-1, 6 ):
    x1, y1, x2, y2, x3, y3 = d[i:][:6]
    for k in range( min( x3 // x1, y3//y1 ) + 1 ):
        q, r = divmod( x3-k*x1, x2 )
        if (r == 0) and ( ( y1*k + y2*q ) == y3 ):
            s+=3*k+q
            s1=(k,q)
            break

print( s )

# part2
s=0
for i in range( 0, len( d )-1, 6 ):
    x1, y1, x2, y2, x3, y3 = d[i:][:6]
    x3+=10000000000000
    y3+=10000000000000
    q, r = divmod( x3*y1 - x1*y3, x2*y1 - x1*y2 )
    if r == 0:
        q1, r1 = divmod( x3-x2*q, x1 )
        if r1 == 0:
            s+=3*q1+q
        
print( s )