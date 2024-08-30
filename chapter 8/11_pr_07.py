def remove_and_split(string,word):
        newStr=string.replace(word, "")
        return newStr.strip()
this="        REENU IS A GOOD GIRL           "
n=remove_and_split(this,"REENU")
print(n)