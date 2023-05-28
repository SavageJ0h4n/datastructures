class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node

        self.update_height(node)

        balance = self.calculate_balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def calculate_height(self, node):
        if node is None:
            return 0
        return node.height

    def calculate_balance_factor(self, node):
        if node is None:
            return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def get_node_distance(self, value1, value2):
        lca_node = self.find_lowest_common_ancestor(self.root, value1, value2)

        if lca_node is not None:
            dist1 = self.get_node_distance_from_node(lca_node, value1)
            dist2 = self.get_node_distance_from_node(lca_node, value2)

            return dist1 + dist2

        return -1

    def find_lowest_common_ancestor(self, node, value1, value2):
        if node is None:
            return None

        if node.value > value1 and node.value > value2:
            return self.find_lowest_common_ancestor(node.left, value1, value2)

        if node.value < value1 and node.value < value2:
            return self.find_lowest_common_ancestor(node.right, value1, value2)

        return node

    def get_node_distance_from_node(self, node, value):
        if node is None:
            return -1

        if node.value == value:
            return 0

        if node.value > value:
            return 1 + self.get_node_distance_from_node(node.left, value)

        return 1 + self.get_node_distance_from_node(node.right, value)


if __name__ == '__main__':
    avl_tree = AVLTree()

    nombres = ["Mongui", "Sachica", "Tinjaca", "Combita", "Chiquiza", "Sutamarchan", "Tibasosa", "Toca", "Guican",
               "Chivata", "Topaga", "Soraca", "Gameza", "Guayata", "Raquira", "Nobsa", "Tenza", "Aquitania"]

    for nombre in nombres:
        avl_tree.root = avl_tree.insert(avl_tree.root, nombre)

    elements1 = input().split(" ")

    value1 = elements1[0]
    value2 = elements1[1]
    distance = avl_tree.get_node_distance(value1, value2)

    if distance != -1:
        print(distance + 1, end='')