moves = 0
biggest_moves = 2

Input = 2
biggest_tester = 1

thousand = Input + 1000000

def calc(starter):
    global biggest_tester, Input, biggest_moves, moves, thousand
    while starter == 1:
        

        tester = Input
        
        
            
        while tester != 1:
            
            if (tester % 2) == 0:
                tester = tester / 2
                moves = moves + 1

            elif (tester % 2) == 1:
                tester = tester * 3 + 1
                moves = moves + 1

        if moves > biggest_moves:
            biggest_moves = moves
            moves = 0
            biggest_tester = Input
            Input = Input + 1
            print("the biggest tester so far is", biggest_tester, "it took", biggest_moves, "to reach one")
            tester = Input 

        elif biggest_moves > moves:
            moves = 0
            Input = Input + 1
            tester = Input

        if Input == thousand:
            print("now testing in the",str(thousand) + "'s")
            thousand = thousand +1000000


calc(1)
        
