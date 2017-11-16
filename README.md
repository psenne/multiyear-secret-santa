# multiyear-secret-santa

This script chooses secret santa partners over several years without repeating gifter-giftee selections. My famiy does a random secret santa drawing each year, and I swear I've gotten my mother-in-law the last 2 out of 4 years. My script won't allow that repitition until each famiy member cycles through everyone in the family.

The script also incorporates couples/roomates/whatever exclusions. So pair up people who aren't allowed to buy for each other, and the script will ensure that they don't.

How to use:

#add as many members as you want
members = ['Husband', 'Wife', 'Dad', 'Mom', 'Sister', 'Brother-in-law', 'Brother', 'Sister-in-law', 'Grandma']

#define exclusion sets. These names should match the ones above
couples = [('Husband', 'Wife'), ('Dad', 'Mom', 'Grandma'?), ('Sister', 'Brother-in-law'), ('Brother', 'Sister-in-law')]

Run the script and use the final output as pairings.
