# Strings
Name=" Rajani "
description="i am watching web series"
details='''i am 
learning python course
in ignitive labz'''
print(f"{Name}  {description}    {details}  {Name[4]}    {description[2]}   {details[6]}  {Name[1:4]}  {description[:15]}   {details[:]}  {len(description)}   {Name.strip()}    {description.lower()}   {details.upper()}   {Name.replace('a','i')}")


# string program
str1,str2,int1="rajani","is a good girl", 20
print(f"{str1+str2}  {str1+str2+str(int1)}")

# string2 example
str1,str2,str3,str4="the basket ","contains ",63,"apples "
# using f string
resultf=f"{str1}{str2}{str3}{str4}"
print(resultf)

""" # using format
print(str1,str2,str(str3), str4)
result=(str1, str2, str3, str4)
print(result, sep=" ") """