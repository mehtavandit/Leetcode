class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def build_tree(words):
            root = TrieNode()

            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_word = True

            return root


        def dfs(board, i, j, node, path):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "#":
                return

            char = board[i][j]
            if char not in node.children:
                return

            board[i][j] = "#"
            node = node.children[char]
            path.append(char)

            if node.is_word:
                result.add("".join(path))

            dfs(board, i+1, j, node, path)
            dfs(board, i-1, j, node,path)
            dfs(board, i, j+1, node,path)
            dfs(board, i, j-1, node, path)

            board[i][j] = char
            path.pop()






        root = build_tree(words)
        result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, root, [])

        return list(result)