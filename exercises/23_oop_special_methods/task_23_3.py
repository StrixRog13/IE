
class Topology:

    def __init__(self, topology_dict):

        self.topology = self._normalize(topology_dict)



    def _normalize(self, topology_dict):

        topology = {}

        for src, dst in topology_dict.items():

            if topology.get(dst) != src:

                topology[src] = dst

        return topology



    def delete_link(self, src, dst):

        if self.topology.get(src) == dst:

            del self.topology[src]

        elif self.topology.get(dst) == src:

            del self.topology[dst]

        else:

            print("Такого соединения нет")



    def __add__(self, other):

        merged = dict(self.topology)

        merged.update(other.topology)

        return Topology(merged)

