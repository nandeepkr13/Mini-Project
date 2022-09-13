nominee1 = input("enter the nominee 1 name : ")
nominee2 = input("enter the nominee 2 name : ")

num1_votes = 0
num2_votes = 0

votes_id = [1, 2, 3, 4, 5]

num_of_voters =len(votes_id)
while True:
    if votes_id==[]:
        print("votng session over")
        if num1_votes>num2_votes:
            percent=(num1_votes/num_of_voters)*100
            print(nominee1,"has won","with", percent,"% votes")
            break

    elif num2_votes>num1_votes:
        percent=(num2_votes/num_of_voters)*100
        print(nominee2,"has won","with", percent,"% votes")
        break


    else:
        voter=int(input("enter your voter id no : "))
    if voter in votes_id:
        print("you are a voter")
        votes_id.remove(voter)
        vote = int(input("enter your vote 1 or 2 : "))
        if vote ==1:
            num1_votes+=1
            print("Thank you for casting your vote")

        elif vote==2:
            num2_votes+=1
            print("Thank you for casting your vote")
        else:
            print("you are not a voter here or you have already voted")


