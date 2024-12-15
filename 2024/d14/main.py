import re

file, w, h ="example.txt", 11, 7
file, w, h="input.txt", 101, 103

r=[ list( map( int, re.findall( r"-?\d+", line ) ) ) for line in open( file ) ]

#part1
a, b, c, d = 0, 0, 0, 0

n=100
for x, y, dx, dy in r:
    x=(x+n*dx)%w
    y=(y+n*dy)%h
    if x < ( w // 2 ):
        if y < ( h // 2 ):
            a+=1
        if y > ( h // 2 ):
            b+=1
    if x > ( w // 2 ):
        if y < ( h // 2 ):
            c+=1
        if y > ( h // 2 ):
            d+=1

print( a*b*c*d )

#part2
