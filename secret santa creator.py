import random

members = ['Husband', 'Wife', 'Dad', 'Mom', 'Sister', 'Brother-in-law', 'Brother', 'Sister-in-law']
couples = [('Husband', 'Wife'), ('Dad', 'Mom'), ('Sister', 'Brother-in-law'), ('Brother', 'Sister-in-law')]

def getRemaining(gifter, gifted):
    global members
    global couples
    global matches
    
    remaining = list(set(members) - set(gifted) - set(gifter))
    
    for couple in couples:
        if gifter in couple:
            remaining = list(set(remaining) - set(couple))
    
    return remaining

    

    
def checkPreviousYears(gifter, listOfChoices):
    return list(set(listOfChoices) - set(matches[gifter]))

    
def initMatches():
    gMatches = {}
    
    for member in members:
        gMatches[member] = []
    
    return gMatches

    

matches = initMatches()

while len(matches[members[-1]]) < len(members) - max(map(len, couples)):  #loops for multiple rounds/years. stops when every member has gotten a gift for every other member
    random.shuffle(members) #so the choosing order changes each year
    gifted = []
    
    while len(gifted) < len(members):  #keeps looping until each family member receives a gift
        for gifter in members:
            remaining = getRemaining(gifter, gifted) #get allowed list of remaining family members
            
            if len(remaining) is 0 and len(gifted) is not len(members):
                # start over if there are no allowable family members to choose from,
                # yet nt every famiy member has gotten a gift
                # ex: mom is the last to choose and only family member left is dad
                print("Matches not found this year.")
                gifted = []
                break
            
            remaining = checkPreviousYears(gifter, remaining)
            if not remaining:
                print("No more possibe matches. Starting over.")
                matches = initMatches()
                gifted = []
                break
            
            giftee = random.choice(remaining)
            
            matches[gifter].append(giftee)
            gifted.append(giftee)
        
        print("Year complete.")

print("\r\n", matches)


