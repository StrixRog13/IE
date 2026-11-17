class Topology:
    def __init__(self, topology_dict):
        self.topology = {}
        for src, dst in topology_dict.items():
            if self.topology.get(dst) != src:
                self.topology[src] = dst

    def delete_link(self, src, dst):
        if self.topology.get(src) == dst:
            del self.topology[src]
        elif self.topology.get(dst) == src:
            del self.topology[dst]
        else:
            print("Такого соединения нет")

    def delete_node(self, node):
        deleted = False
        for src, dst in list(self.topology.items()):
            if src[0] == node or dst[0] == node:
                del self.topology[src]
                deleted = True
        if not deleted:
            print("Такого устройства нет")
