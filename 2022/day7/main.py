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
