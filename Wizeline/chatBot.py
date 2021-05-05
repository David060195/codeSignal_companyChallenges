class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.listIndex = []
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, indexArr, index):
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        curNode.listIndex.append((indexArr, index))
        curNode.isEnd = True
    
    def search(self, word):
        curNode = self.root
        for char in word:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
        if curNode.isEnd:
            return curNode.listIndex

def chatBot(conversations, currentConversation):
    trie = Trie()
    listLength = [[set(), 0] for _ in range(len(conversations))]
    for index, arr in enumerate(conversations):
        for indexWord, word in enumerate(arr):
            trie.insert(word, index, indexWord)
    for word in currentConversation:
        curWord = trie.search(word)
        if curWord:
            for indexArr, indexWord in curWord:
                listLength[indexArr][0].add(word)
                if indexWord > listLength[indexArr][1]:
                    listLength[indexArr][1] = indexWord
    maxLength, indexList, cutIndexWord = 0, 0, 0
    for index, (seen, i) in enumerate(listLength):
        if len(seen) > maxLength:
            maxLength = len(seen)
            cutIndexWord = i
            indexList = index
    return currentConversation + conversations[indexList][cutIndexWord + 1:] if maxLength else currentConversation
