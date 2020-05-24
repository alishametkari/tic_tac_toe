def board( lis ) :
    #function to print board
    for i in range( len( lis ) ) :
        if i%3 == 0 :
            print( "\n| " + str( lis[i] ), end = " | " )
        else :
            print( lis[i], end = " | " )
def Input( lis, i, value ) :
    lis[i] = value
def getindexes( lis, value ) :
    index = []
    indexpos = 0
    while True :
        try:
            indexpos = lis.index( value,indexpos )
            index.append( indexpos )
            indexpos += 1
        except ValueError as e :
            break
    return index
def abnormal_end( lis ) :
    if lis.count( 'o' ) + lis.count( 'x' ) == 9 :
        return 1
    else :
        return 0
def check1( lis,win ) :
    for i in range( len( win ) ) :
        count1 = 0
        for j in range( len( win[i] ) ) :
            if win[i][j] in getindexes( lis,'o' ) :
                count1 += 1
        if count1 == 3 :
            return 1
def check2( lis, win ) :
    for i in range( len( win ) ) :
        count2 = 0
        for j in range( len( win[i] ) ) :
            if win[i][j] in getindexes( lis,'x' ) :
                count2 += 1
        if count2 == 3 :
            return 1
lis = [ '', '', '', '', '', '', '', '', '' ]           #empty board for game
board( lis )
print( "\n" )
win = [ [ 0, 3, 6 ], [ 1, 4, 7 ], [ 2, 5, 8 ], [ 0, 1, 2 ], [ 3, 4, 5 ], [ 6, 7, 8 ], [ 0, 4, 8 ], [ 2, 4, 6 ] ]
dic = { 'play1' : 'o', 'play2' : 'x' }
player1 = str( input( "enter name of player 1 : " ) )
player2 = str( input( "enter name of player 2 : " ) )
while True :
        while True :
            try :
                i = int( input( player1 + " enter your input :" ) )
                if lis[i] == 'o' or lis[i] == 'x' :
                    print( "Box is not empty. Plz try again!" )
                    continue
                else :
                    break
            except ( ValueError, IndexError ) :
                print( "IndexError and ValueError handled." )
                continue
        value = dic[ 'play1' ]
        Input( lis, i, value )
        board( lis )
        print( "\n" )
        if len( getindexes( lis, value ) ) >= 3 and check1( lis, win ) :
            print( player1 + " has won the game." )
            break
        if abnormal_end( lis ) :
            print( "Draw!" )
            break
        else :
            print( "Game Continues" )
            while True:
                try:
                    i = int( input( player2 + " enter your input :") )
                    if lis[i] == 'o' or lis[i] == 'x' :
                        print( "Box is not empty. Plz try again!" )
                        continue
                    else:
                        break
                except ( ValueError, IndexError ) :
                    print( "IndexError and ValueError handled" )
                    continue
            value = dic[ 'play2' ]
            Input( lis, i, value )
            board( lis )
            print( "\n" )
            if len( getindexes( lis, value ) ) >= 3 and check2( lis, win ) :
                print( player2 + " has won the game" )
                break
            if abnormal_end( lis ) :
                print( "Draw!" )
            else :
                print( "Game Continues" )
                continue