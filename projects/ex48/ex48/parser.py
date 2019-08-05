class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject=subject[1]
        self.verb=verb[1]
        self.object=obj[1]
    
    def peek(self,word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(self,word_list,expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self,word_list,word_type):
        while self.peek(word_list)==word_type:
            self.match(word_list,word_type)

    