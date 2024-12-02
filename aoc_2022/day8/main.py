trees=[]
for line in open("input"):
    trees.append( list( map( int, line.strip() ) ) )

h=len( trees )
w=len( trees[0] )

maxt=[-1] * w
maxb=[-1] * w
maxl=[-1] * h
maxr=[-1] * h

visible = set()

def check( i, j, m, k ):
    if trees[i][j] > m[k]:
        m[k] = trees[i][j]
        visible.add( (i, j) )

for i in range( w ):
    for j in range( h ):
        check( i, j, maxt, j )
        check( i, j, maxl, i )
        check( w-i-1, j, maxb, j )
        check( i, h-j-1, maxr, i )

print( len( visible ) )

def visi( i, j, r, b ):
    v=0
    for k in r:
        v+=1
        if b:
            i2, j2 = k, j
        else:
            i2, j2 = i, k
        if trees[i][j] <= trees[i2][j2]:
            break
    return v

m=0
for i in range( 1, w-1 ):
    for j in range( 1, h-1 ):
        vr=visi( i, j, range( i+1, w      ), True )
        vl=visi( i, j, range( i-1, -1, -1 ), True )
        vb=visi( i, j, range( j+1, h      ), False )
        vt=visi( i, j, range( j-1, -1, -1 ), False )
        m=max(m, vr*vl*vt*vb )
        
print( m )

