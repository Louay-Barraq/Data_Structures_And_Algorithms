class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces_number = ' ' * self.get_level() * 3
        prefix = "|-" if self.parent else ""

        print(str(spaces_number) + prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()
