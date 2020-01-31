

import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)
df = pd.Series(doc)
print(df.head(10))
temp=df.to_string()
common_string=df.str.extractall(r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)\b')
## (1) 04/20/2009; 04/20/09; 4/20/09; 4/3/09 (20 points)

# The first part is to extract the dates with the above patterns
# The code is already given

a_1 = df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2}|\d{4})\b')
print("*******")
print("Part 1")
print("*******")
print(a_1)
#print(len(a_1)) -->125


## (2)Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009; (20 points)

# Please extract the dates with the above patterns
# Please finish your code here
#print(df.head(5))
a_2=df.str.extractall(r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[\.\s-]*(\d{1,2})[,\s\-]*(\d{4})\b')
print("*******")
print("Part 2")
print("*******")
print(a_2)
#print(len(a_2)) --> 34
## (3) 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009 (20 points)
# Please extract the dates with the above patterns
# Please finish your code here
print("*******")
print("Part 3")
print("*******")
a_3=df.str.extractall(r'(\d{1,2})+\s((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[\s\.,]*(\d{4})\b')
print(a_3)
#print(len(a_3)) -->69
## (4) Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009 (20 points)

# Please extract the dates with the above patterns
# Please finish your code here
a_4=df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s(\d{1,2}[st|nd|rd|th],\s\d{4})\b')
print("*******")
print("Part 4")
print("*******")
#print(len(a_4))  -->0
print(a_4)

## (5) 6/2008; 12/2009 (20 points)
# Please extract the dates with the above patterns
# Please finish your code here
a_5=df.str.extractall(r'(\d{1,2}[/]\d{4})\b')
print("*******")
print("Part 5")
print("*******")
#print(len(a_5)) -->137
print(a_5)


#Please contact all 5 parts together
final = pd.concat([a_1,a_2,a_3,a_4,a_5])
print("*******")
print("Final")
print("*******")
print(final)