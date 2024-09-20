# w.a.p to input a string and print the count of vowels and consonant in the string 

vowels = 'aeiou'
ip_str = input("Enter a string: ")


ip_str = ip_str.casefold()

count = {}.string(vowels,0)



for char in ip_str:

   if char in count:

       count[char] += 1

print(count)





