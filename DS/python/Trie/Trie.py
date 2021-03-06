import string, unittest

class Node:
    """"""
    def __init__(self):
        """"""
        self.count = 0
        self.nodes = [None] * 256 # 256 charset

    def next(self, c):
        """"""
        return self.nodes[ord(c)]

    def add_child(self, c):
        """"""
        self.nodes[ord(c)] = Node()

class Trie(object):
    """"""
    def __init__(self):
        """"""
        self.__root = Node()

    def __get_root(self):
        """"""
        return self.__root

    def query(self, s):
        """"""
        if not s:
            return 0
        current = self.__get_root()
        for char in s:
            if not current:
                return 0
            current = current.next(char)
        return current.count

    def insert(self, s):
        """"""
        if not s:
            raise RuntimeError("Empty String")
        current = self.__get_root()
        for char in s:
            if not current.next(char):
                current.add_child(char)
            current = current.next(char)
        current.count += 1
        return current.count

    def delete(self, s):
        if not s:
            raise RuntimeError("Empty String")
        current = self.__get_root()
        for char in s:
            if not current:
                raise RuntimeError('String %s does not exist in the trie.' % s)
            current = current.next(char)
        if current.count == 0:
            raise RuntimeError('String %s does not exist in the trie.' % s)
        current.count -= 1

    def update(self, old, new):
        """"""
        try:
            self.delete(old)
        except RuntimeError:
            pass
        finally:
            self.insert(new)

class TrieTests(unittest.TestCase):
    """"""
    def test01(self):
        """"""
        trie = Trie()
        self.assertRaises(RuntimeError, trie.insert, "")

    def test02(self):
        trie = Trie()
        s = "abc"
        trie.insert(s)
        self.assertEquals(trie.query(s), 1)
        trie.insert(s)
        self.assertEquals(trie.query(s), 2)

        trie.delete(s)
        self.assertEquals(trie.query(s), 1)
        trie.delete(s)
        self.assertEquals(trie.query(s), 0)

    def test03(self):
        """"""
        trie = Trie()
        self.assertRaises(RuntimeError, trie.delete, "")

    def test04(self):
        """"""
        trie = Trie()
        s = "abc"
        self.assertRaises(RuntimeError, trie.delete, "random")
        trie.insert(s)
        trie.insert(s)
        self.assertEquals(trie.query(s), 2)
        trie.delete(s)
        self.assertEquals(trie.query(s), 1)
        trie.delete(s)
        self.assertRaises(RuntimeError, trie.delete, s)

    # TODO Add more tests

if __name__ == '__main__':
    unittest.main()
