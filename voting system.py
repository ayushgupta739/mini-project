bjpVotes = 0
bspVotes = 0
aapVotes = 0
notaVotes = 0

while True:
    gender = input("Enter your gender (m if male or f if female, q to quit): ")
    
    if gender == 'q':
        break
    
    if gender == 'm':
        print("Male")
    elif gender == 'f':
        print("Female")
    else:
        print("Not valid, please enter again")
        continue

    name = input("\nEnter your name: ")

    if gender == 'm':
        print("Voter name is: Mr", name)
    elif gender == 'f':
        print("Voter name is: Ms", name)

    age = int(input("\nEnter your age: "))

    if age >= 18:
        print("Eligible for voting")
        print("Vote for a party as a number\n")
        print("1-BJP\n2-BSP\n3-AAP\n4-NOTA\n")
        vote = int(input())
        if vote == 1:
            print("BJP")
            bjpVotes += 1
        elif vote == 2:
            print("BSP")
            bspVotes += 1
        elif vote == 3:
            print("AAP")
            aapVotes += 1
        elif vote == 4:
            print("NOTA")
            notaVotes += 1
        else:
            print("You have entered a wrong value")
            print("Fill the details again")
            continue

        print("\nVote Counts:\n")
        print("BJP:", bjpVotes, "\nBSP:", bspVotes, "\nAAP:", aapVotes, "\nNOTA:", notaVotes)

        if bjpVotes >= bspVotes and bjpVotes >= aapVotes and bjpVotes >= notaVotes:
            print("BJP is the winner")
        elif bspVotes >= bjpVotes and bspVotes >= aapVotes and bspVotes >= notaVotes:
            print("BSP is the winner")
        elif aapVotes >= bjpVotes and aapVotes >= bspVotes and aapVotes >= notaVotes:
            print("AAP is the winner")
        else:
            print("Any one is not the winner")
    else:
        print("Not eligible")
