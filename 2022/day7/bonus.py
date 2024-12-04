#premiere approche pour le pb 1 

s=0
d = []
lines=open( "input" ).read( ).split( "\n" )
while True:
    if len( lines ) > 0:
        line, *lines = lines
    elif len( d ) > 1:
        line = None
    else:
        break
    if line in [ None, "$ cd .." ]:
        if d[-1] <= 100000:
            s+=d[-1]
        d[-2]+=d[-1]
        del d[-1]
    elif line == "$ ls" or line.startswith( "dir" ):
        continue
    elif line.startswith( "$ cd" ):
        d.append( 0 )
    else:
        d[-1] += int( line.split( )[0] )

print( s )
