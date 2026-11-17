from task_23_3 import Topology as BaseTopology


class Topology(BaseTopology):
    def __iter__(self):
        return iter(self.topology.items())
