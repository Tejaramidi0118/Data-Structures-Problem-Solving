class Codec:

    def serialize(self, root):
        if not root:
            return ""

        output = []
        q = [root]

        while q:
            node = q.pop(0)
            if node:
                output.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                output.append("null")

        while output and output[-1] == "null":
            output.pop()

        return ",".join(output)
        

    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        q = [root]
        i = 1

        while q and i < len(vals):
            node = q.pop(0)

            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root
