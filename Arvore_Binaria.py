class BinaryTree:
    def __init__(self):
        self.tree = {}

    def insert(self, value):
        if not self.tree:
            self.tree[value] = [None, None]
        else:
            self._insert_recursively(value, next(iter(self.tree)))

    def _insert_recursively(self, value, current):
        if value < current:
            if self.tree[current][0] is None:
                self.tree[current][0] = value
                self.tree[value] = [None, None]
            else:
                self._insert_recursively(value, self.tree[current][0])
        else:
            if self.tree[current][1] is None:
                self.tree[current][1] = value
                self.tree[value] = [None, None]
            else:
                self._insert_recursively(value, self.tree[current][1])

    def remove(self, value):
        if value not in self.tree:
            print(f"Valor {value} não encontrado na árvore.")
            return
        self.tree, _ = self._remove_recursively(self.tree, value)

    def _remove_recursively(self, tree, value):
        if not any(tree[value]):
            del tree[value]
            return tree, None

        if tree[value][0] is None:
            right_child = tree[value][1]
            del tree[value]
            return tree, right_child

        if tree[value][1] is None:
            left_child = tree[value][0]
            del tree[value]
            return tree, left_child

        successor = self._find_min(tree, tree[value][1])
        tree[value][0], tree[value][1] = tree[successor][0], tree[successor][1]
        del tree[successor]
        return tree, None

    def _find_min(self, tree, node):
        current = node
        while tree[current][0] is not None:
            current = tree[current][0]
        return current

    def search(self, value):
        return self._search_recursively(value, next(iter(self.tree)), 0)

    def _search_recursively(self, value, current, level):
        if current is None or current not in self.tree:
            return None, -1
        if current == value:
            return current, level
        if value < current:
            return self._search_recursively(value, self.tree[current][0], level + 1)
        else:
            return self._search_recursively(value, self.tree[current][1], level + 1)

    def print_tree(self):
        print("Árvore Binária:", self.tree)

bt = BinaryTree()
bt.insert("15")
bt.insert("10")
bt.insert("20")
bt.insert("8")
bt.insert("12")
bt.insert("17")
bt.insert("25")

bt.print_tree()

value = "8"
node, level = bt.search(value)
print(f"Nó '{value}' {'encontrado' if node else 'não encontrado'} no nível {level}.")

bt.remove("10")
bt.print_tree()  # Visualizar após a remoção