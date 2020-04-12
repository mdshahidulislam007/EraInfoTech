import re

#
pattern='^a...s$'
str='abcas'
if(re.match(pattern,str)):
    print('Search Successful')
else:
    print('Search Unsuccessful')

#

pattern1='[abc]'
str1='ab'
print(re.findall(pattern1,str1))
