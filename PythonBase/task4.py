import re
# # #Q1.Find all words starting with s,p or r and ends at 'at
s="sat mat pat cat rat bat"
m=re.findall(r'[spr]at',s)
print(m)

# #
# # #Q2.Find all words starting with except s,p or r and ends at 'at'
s="sat mat pat cat rat bat"
m=re.findall(r'[^spr]at',s)
print(m)

# # #
# # #Q3.Find all 3,4 and 5 digit numbers from the string
s="123 6738 34556 355666 76767564 445222"
m=re.findall(r'\b[0-9]{3,5}\b',s)
print(m)

# # #
# # #Q4.Find all 3,4 and 5 letter words from the string
s="The quick brown fox jumps over the lazy dog"
m=re.findall(r'\b[a-z]{3,5}\b',s)
print(m)
# #
# #Q5.Write a program to find filenames with particular extension
s="s.html,k.txt,m.jpeg,l.py,a.jpeg"
m=re.findall(r'[a-z].py',s)
print('file name with .py :',m)

# #Q6.Write a program to find words containing 'z' from a string
s="abcdz abzcd zabcd hjklj"
m=re.findall(r'\wz*\w*',s)
print('words contain z :',m)
#
# #Q7.Check whether the given string contains only lowercase, uppercase,digits and underscore
# import re
s="57767fafafaf"
m=re.search(r'^\w+$',s)
if m:
    print('match : ',m.group())
else:
    print('error!')

# # #Q8.Write a program to extract year/month/date from a url
s="www.washingtonpost.com/news/football-insider/wp/2016/09/02"
m=re.search('[0-9]+/[0-9]+/[0-9]+',s)
if m:
    print('yyyy/mm/dd : ',m.group())
else:
    print('error!!')

# #
# #Q9.Replace \n with space
s="""Keep the blue flag
flying high
Chelsea"""
m=re.sub(r'\n'," ",s)
print(m)

# #output:Keep the blue flag flying high Chelsea
#
# #Q10.Replace dot,comma and space  with :
s="Python is a,Programming language."
m=re.sub(r'[., ]',':',s)
print(m)

# # output:"Python:is:a:Programming:language:"
#
# #Q11.Remove all alphanumeric characters from the string
s="adfsgdhvj5678 &#%%^&& sfdhfhj _RfGGGG"
m=re.sub(r'[a-zA-Z0-9]','',s)
print(m)
# #output:" &#%%^&&  _"

# # #Q12.Find all words starting with vowel and ends with vowel from the given string
s="red green orange"
m=re.findall(r'\b[aeiou]\w*[aeiou]\b',s)
print('Vowels : ',m)

# #Q13.Find the count of numbers in the string
s="One 1 two 2 three 3 four 4456787"
m=re.findall(r'[0-9]+',s)
print('count of numbers in the string : ',len(m))
