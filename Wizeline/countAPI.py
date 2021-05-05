class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.word = ''
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.word = char
            current.count += 1
    def subProjects(self):
        def helper(root, currentWord, ans, deep):
            currentWord = deep * '--' + root.word + ' (' + str(root.count) + ')'
            ans.append(currentWord)
            for node in root.children.values(): 
                helper(node, currentWord, ans, deep + 1)
        ans = []
        helper(self.root, '', ans, 0)
        return ans[1:]
def countAPI(calls):
    trie = Trie()
    for project in calls:
        words = project.split('/')[1:]
        trie.insert(words)
    return trie.subProjects()