# Print characters in ascending order of their frequency of occurence 
# in a given string.
# input string str1 = "assssdfffhrrdls"
# output=[s,f,r,d,a,l,]
        

def get_char_count(str1):
    mydict = {}
    for c in str1:
        mydict[c] = str1.count(c)
    print mydict
    return mydict

char_freq = get_char_count(str1)

sorted_list = sorted(char_freq.items(), key=lambda x: x[1])
# list of tuples.
# here sorting is based on the values and not the keys.
# [('s', 1), ('m', 1), ('d', 2), ('e', 2), ('g', 2), ('h', 2), ('a', 3), ('f', 3), ('n', 3)]

chars_list = [t[0] for t in sorted_list]
# ['s', 'm', 'd', 'e', 'g', 'h', 'a', 'f', 'n']
