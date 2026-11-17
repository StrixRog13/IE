class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        topology = {}
        for src, dst in topology_dict.items():
            if topology.get(dst) != src:
                topology[src] = dst
        return topology
