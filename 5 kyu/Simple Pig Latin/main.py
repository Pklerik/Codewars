import string

def pig_it(text:str) -> str:
    lst = text.split()
    for i, word in enumerate(lst):
        if word in (string.punctuation):
            continue
        lst[i] = word[1:] + word[0] + 'ay'
    return " ".join(lst)

print(pig_it("Quis custodiet ipsos custodes ?"))


        