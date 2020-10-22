from pya2l.parser import A2lParser


a2l_string = open(r'DASY_BASE_01_Copy.a2l', 'r').read()

a2l = A2lParser(a2l_string)

for i, node in enumerate(a2l.tree.project.module[0].get_node("MEASUREMENT")):
    print(node.name)
