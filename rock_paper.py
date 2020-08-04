user1 = input("Enter your name\n?")
user2 = input("Enter your name\n")
user1_ans = input("%s, Choose rocks, paper or scissor\n"% user1)
user2_ans = input("%s, Choose rocks, paper or scissor\n"% user2)
if user1_ans == user2_ans:
    print("It's tie")
elif user1_ans == 'paper' and user2_ans == 'scissor':
    print("user2 won")
elif user1_ans == 'scissor' and user2_ans == 'rocks':
    print("user2 won")
elif user1_ans == 'rocks' and user2_ans == 'paper':
    print('user1 won')

