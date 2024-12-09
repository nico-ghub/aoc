file="example.txt"
file="input.txt"

d = list( map( int, next( open( file ) ).strip() ) )

#part1
f=d[0::2]
e=d[1::2]

b, l = 1, len( f ) -1

i=d[0]
c=0

while b <= l:
    ne, *e = e
    while ne > 0 and b <= l:
        m=l
        if ne >= f[l]:
            n = f[l]
            l-=1
        else:
            n = ne
            f[l]-=ne
        
        c+=m*n*(2*i+n-1)//2
        ne-=n
        i+=n

    if b > l:
        break
    m = b
    n=f[b]
    c+=m*n*(2*i+n-1)//2
    i+=n
    b+=1
    

print( c )

#part2
f=d[0::2]
e=d[1::2]

i=d[0]
c=0
r = []

while b < len( f ):
    if len( e ) > 0:
        ne, *e = e
        for l in range( len( f ) -1, b-1, -1 ):
            if l in r:
                continue
            m=l
            n = f[l]
            if ne >= n:
                l-=1
                c+=m*n*(2*i+n-1)//2
                ne-=n
                i+=n
                r.append( m )
                if ne == 0:
                    break
        i+=ne

    if b in r:
        i+=f[b]
        b+=1
        continue
        
    m = b
    n=f[b]
    c+=m*n*(2*i+n-1)//2
    i+=n
    b+=1

print( c )
