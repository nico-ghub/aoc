m=0
s=0
for l in open( "input" ):
    l=l.strip()
    if l=="":
        m=max( m, s )
        s=0
    else:
        s+=int( l )

print( m )

s=0
l=[]
for c in open( "input" ):
    c=c.strip()
    if c=="":
        l.append( s )
        s=0
    else:
        s+=int( c )

print( sum( sorted( l )[-3:] ) )
