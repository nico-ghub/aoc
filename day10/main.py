def solve( file ):
    x=1
    c=0
    s=0
    l=""
    for line in open( file ):
        dc, dx = 1, 0
        if line.startswith('addx'):
            dc, dx = 2, int( line.split()[1] )
        for _ in range( dc ):
            if x <= ( c % 40 ) + 1 <= x+2:
                l+="#"
            else:
                l+="."
            if ( c % 40 ) == 39:
                print( l )
                l=""
            c+=1
            if ( c + 20 ) % 40 == 0:
                s+=c*x
        x+=dx
    print( s )

solve( "input_ex" )
solve( "input" )
