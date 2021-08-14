purchase_amount = 20.00
state = 'NY'
if state == 'CA':
    tax_amount = 0.075
    total_cost = purchase_amount*(1+tax_amount)
    print("your total cost is {} becasue you are from {}".format(total_cost, state))
elif state =='MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    print("your total cost is {} becasue you are from {}".format(total_cost, state))
elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    print("your total cost is {} becasue you are from {}".format(total_cost, state))
