#defining a function for removing characters
def remove_characters(word, n):
# return a slice of the string from n to the end
 return word[n:]

# test the function and print
print(remove_characters("Footlong", 4)) 