"""CHALLENGE: Given a list 'person' which is a list of lists of two strings,
create a dictionary 'answer' that makes each first item ineach list a key
and the second item a corresponding value."""

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Let's do a dict comprehension!
answer = {person[i][0]:person[i][1] for i in range(len(person))}

print(answer)
