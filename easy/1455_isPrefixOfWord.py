# Problem Title - Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Date - 20260106

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Split the sentence to get the words (since it is stated that they are delimited by single space).
        Then just check every word if it starts with searchWord, and return the index.
        Keep a flag, just to return -1 if its not found.
        """
        words_list = sentence.split(' ')
        found_flag = False
        ind = 1
        for word in words_list:
            if word.startswith(searchWord):
                found_flag = True
                break
            ind += 1
    
        if not found_flag:
            return -1
        return ind