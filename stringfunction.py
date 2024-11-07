str="I am studying in SSIPMT in 3rd sem"
print(str.endswith("sem"))   #endswith function
print(str.endswith("pmt"))

str=str.capitalize() #capitalize function
print(str)

#replace function
print(str.replace("i","o"))

#find function - it search the element
print(str.find("t")) # it will return the number of place where the zero is
print(str.find("am"))
print(str.find("o"))  # o is not present there so it will return -1 , which do not exists in any String

#count that the word is existed how many times
print(str.count("in"))
print(str.count("t"))
