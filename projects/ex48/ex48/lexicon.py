def scan(string):
    ret = []

    # seperate words in sentence
    words = string.split()

    # describe keywords
    directions = ["north","south","east","west"]
    verbs = ["go","kill","eat"]
    stops = ["the","in","of"]
    nouns = ["bear","princess"]
    
    for word in words:
        try:
            ret.append(("number",int(word)))
        except ValueError:
            if word in directions:
                ret.append(("direction",word))
            elif word in verbs:
                ret.append(("verb",word))
            elif word in stops:
                ret.append(("stop",word))
            elif word in nouns:
                ret.append(("noun",word))
            else:
                ret.append(("error",word))
    return ret
            

