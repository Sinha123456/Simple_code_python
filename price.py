points = 174

wooden_rabit_price = 'wooden rabbit'
no_price = 'no price'
second_highest_price = 'wafer-thin mint'
highest_price = 'penguin'

# write your if statement here

if points > 181:
    print("Congratulations! you won {}:".format(highest_price))

elif points <= 180:
    print("you won the second heighest price: {}".format(second_highest_price))
elif points <= 150:
    print('I am sorry you won nothing:'.format(no_price))
elif points <= 50:
    print('Yay, you go somthing that is:'.format(wooden_rabit_price))
else:
    print('There is something wrong.')
