class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def construirArbol(self, valores):
        if not valores:
            return

        self.root = TreeNode(valores[0])
        cola = [self.root]

        i = 1
        while cola and i < len(valores):
            actual = cola.pop(0)

            if i < len(valores):
                actual.left = TreeNode(valores[i])
                cola.append(actual.left)
                i += 1

            if i < len(valores):
                actual.right = TreeNode(valores[i])
                cola.append(actual.right)
                i += 1

    def recorridoNivel(self):
        if not self.root:
            return

        cola = [self.root]

        while cola:
            actual = cola.pop(0)
            print(actual.value, end=" ")

            if actual.left:
                cola.append(actual.left)

            if actual.right:
                cola.append(actual.right)

    def recorridoPreorden(self):
        valores = []
        self._recorridoPreorden(self.root, valores)
        return valores

    def _recorridoPreorden(self, nodo, valores):
        if not nodo:
            return

        if nodo.value != -1:
            valores.append(nodo.value)

        self._recorridoPreorden(nodo.left, valores)
        self._recorridoPreorden(nodo.right, valores)

    def recorridoPostorden(self):
        valores = []
        self._recorridoPostorden(self.root, valores)
        return valores

    def _recorridoPostorden(self, nodo, valores):
        if not nodo:
            return

        self._recorridoPostorden(nodo.left, valores)
        self._recorridoPostorden(nodo.right, valores)

        if nodo.value != -1:
            valores.append(nodo.value)

    def recorridoInorden(self):
        valores = []
        self._recorridoInorden(self.root, valores)
        return valores

    def _recorridoInorden(self, nodo, valores):
        if not nodo:
            return

        self._recorridoInorden(nodo.left, valores)

        if nodo.value != -1:
            valores.append(nodo.value)

        self._recorridoInorden(nodo.right, valores)

    def obtenerRecorridoConMayorPrioridad(self, Preorder, Inorder, Postorder):
        if Preorder >= Inorder and Preorder >= Postorder:
            print("Preorder", Preorder, end='')
        elif Inorder >= Preorder and Inorder >= Postorder:
            print("Inorder", Inorder, end='')
        else:
            print("Postorder", Postorder, end='')
if __name__ == '__main__':
    arbol = BinaryTree()

    valores = list(map(int, input().split()))
    n = int(input())

    arbol.construirArbol(valores)

    preorden = arbol.recorridoPreorden()
    sumaPreorden = sum(preorden[:n])

    inorden = arbol.recorridoInorden()
    sumaInorden = sum(inorden[:n])

    postorden = arbol.recorridoPostorden()
    sumaPostorden = sum(postorden[:n])

    arbol.obtenerRecorridoConMayorPrioridad(sumaPreorden, sumaInorden, sumaPostorden)