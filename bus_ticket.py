age = 40
free_up_to_age = 4
child_upto_age = 18
senior_frpm_age = 65
concession_ticket = 1.50
adult_ticket = 2.80

if age<=free_up_to_age:
    bus_ticket = 0
elif age<=child_upto_age:
    bus_ticket = concession_ticket
elif age>=senior_frpm_age:
    bus_ticket = concession_ticket
else:
    bus_ticket = adult_ticket

message = "Someone who is {} years old will pay ${} for the bus fair.".format(age, bus_ticket)
print(message)