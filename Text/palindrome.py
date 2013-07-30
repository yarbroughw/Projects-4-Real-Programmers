forward = raw_input("Enter string: ").lower()
reverse = forward[::-1]
if forward == reverse:
    print "Palindrome detected"
else:
    print "Not a palindrome"