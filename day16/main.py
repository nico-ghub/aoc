import re

def solve( file ):
    v1=[]
    p={}
    for line in open( file ):
        m = re.match( r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", line )
        if m==None:
            print( line )
        n, r, l = re.match( r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", line ).groups()
        if r != "0":
            p[n] = int( r )
        v1.append( ( n, l.replace(" ","").split(",") ) )

    v = { i: { j: 1 for j in l } for i,l in v1 }

    for i in range( len( v ) ):
        for n1, l in v1:
            for n2 in l:
                for n3 in v[n1]:
                    if not n3 in v[n2] and n3 != n2:
                        v[n2][n3] = v[n1][n3]+1
    
    def rec1( c1, n, o ):
        l = [ (c2, n - v[c1][c2] - 1) for c2 in o if 0 < n - v[c1][c2] - 1 ]
        if len( l ) == 0:
            return 0
        return max( 0, *( i*p[c2] + rec1( c2, i, tuple( c3 for c3 in o if c3 != c2 ) ) for c2, i in l ) )
        
    print( rec1( "AA", 30, p.keys() ) )

    def rec2( c1, n1, c2, n2, o ):
        if n2 > n1:
            c1, n1, c2, n2 = c2, n2, c1, n1
        l = [ (c3, n1 - v[c1][c3] - 1) for c3 in o if 0 < n1 - v[c1][c3] - 1 ]
        if len( l ) == 0:
            return rec1( c2, n2, o )
        return max( 0, *( i*p[c3] + rec2( c2, n2, c3, i, tuple( c4 for c4 in o if c4 != c3 ) ) for c3, i in l ) )

    print( rec2( "AA", 26, "AA", 26, p.keys() ) )

#solve( "input_ex" )
solve( "input" )
