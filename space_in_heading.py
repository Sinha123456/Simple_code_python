headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
new_ticker = ""
for lines in headlines:
    new_ticker += lines + " "
    if len(new_ticker) >= 140:
        new_ticker = new_ticker[:140]
        break
print(new_ticker)
