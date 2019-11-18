"""This prog takes a string of normal text(plaintext)
 and turn it to visual gibberish!"""


class Scrambler:
        
    @staticmethod
    def scramble(plaintext, scramble_level):
        if scramble_level == 1:
            scrambletext = '&$#'.join(plaintext)
        return scrambletext








    
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
s1 = Scrambler()
print(s1.scramble(my_string, 1))
