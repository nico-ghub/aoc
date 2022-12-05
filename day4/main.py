s=0

for l in open( "input" ):
    a,b,c,d = map(int, l.strip().replace(",", "-").split("-"))
    if ( a <= c and b >= d ) or ( c <= a and d >= b ):
        s+=1

print( s )

s=0
for l in open( "input" ):
    a,b,c,d = map(int, l.strip().replace(",", "-").split("-"))
    if  a <= d and b >= c:
        s+=1

print( s )
