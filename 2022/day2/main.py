s=0

d={ "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
    }

print( sum( d[i.strip()] for i in open( "input" ) ) )


d={ "A X": 0 + 3, # R > C = 3
    "A Y": 3 + 1, # R = R = 1
    "A Z": 6 + 2, # R < P = 2
    "B X": 0 + 1, # P > R = 1
    "B Y": 3 + 2, # P = P = 2
    "B Z": 6 + 3, # P < C = 3
    "C X": 0 + 2, # C > P = 2
    "C Y": 3 + 3, # C = C = 3
    "C Z": 6 + 1, # C < R = 1
    }

print( sum( d[i.strip()] for i in open( "input" ) ) )
