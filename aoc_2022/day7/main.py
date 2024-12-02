pwd=[]
files={}

for line in open( "input" ):
    line=line.strip()
    if line == "$ ls" or line.startswith( "dir" ):
        continue
    elif line == "$ cd ..":
        del pwd[-1]
    elif line.startswith( "$ cd" ):
        pwd.append( line.split( )[2] )
    else:
        size, file= line.split( )
        path = "/".join( pwd + [file] )
        files[ path ] = int( size )

dirs={}
for path, size in reversed( list( files.items() ) ):
    pwd=""
    for d in path.split("/")[:-1]:
        pwd += f"/{d}"
        dirs.setdefault( pwd, 0 )
        dirs[pwd]+=size

print( sum( size for path, size in  dirs.items( ) if size <= 100000 ) )

required = 30000000 - ( 70000000 - dirs["/"] )
print( min( size for path, size in  dirs.items( ) if size >= required ) )


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

