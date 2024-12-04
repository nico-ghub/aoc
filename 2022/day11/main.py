from operator import mul
from functools import reduce

def solve( file, r, n ):
    monkeys=[]
    for line in open( file ):
        if ":" in line:
            c, d = line.strip().split(":")
            if c.startswith( "Monkey" ):
                monkeys.append( {} )
            elif c == "Starting items":
                monkeys[-1]["w"]=list( map( int, d.split(",") ) )
            elif c == "Operation":
                exec( f'monkeys[-1]["o"]=lambda old:{ d.split( "=" )[-1]}' )
            elif c == "Test":
                monkeys[-1]["d"]=int( d.split()[-1] )
            elif c == "If true":
                monkeys[-1][True]=int( d.split()[-1] )
            elif c == "If false":
                monkeys[-1][False]=int( d.split()[-1] )
    
    d = reduce( mul, ( m["d"] for m in monkeys ) )
    t = [ 0 for _ in monkeys ]
    for r in range( r ):
        for i, m in enumerate( monkeys ):
            for w in m["w"]:
                t[i]+=1
                w=( m["o"]( w ) // n ) % d
                monkeys[m[ w  % m["d"]  == 0 ]]["w"].append( w )
            m["w"]=[]

    print( mul( *sorted( t )[-2:] ) )

solve( "input", 20, 3 )
solve( "input", 10000, 1 )
