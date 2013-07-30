from collections import Counter

string = raw_input("Enter string: ").lower()
stringlist = list(string)
vowels = filter(lambda x: x in "aeiou", stringlist)
vowelcounter = Counter(vowels)

print str(sum(vowelcounter.values())) + " vowels."
print str(vowelcounter['a']) + " 'A's"
print str(vowelcounter['e']) + " 'E's"
print str(vowelcounter['i']) + " 'I's"
print str(vowelcounter['o']) + " 'O's"
print str(vowelcounter['u']) + " 'U's"