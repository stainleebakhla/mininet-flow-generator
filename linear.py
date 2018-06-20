from mininet.topo import Topo


class LinearTopo(Topo):

    def __init__(self, n=2):
        # Initialize topology
        Topo.__init__(self)
        h = []
        s = []
        for i in range(1, n+1):
            str_h = 'h' + str(i)
            str_s = 's' + str(i)
            h.append(self.addHost(str_h))
            s.append(self.addSwitch(str_s))
            self.addLink(h[-1], s[-1])
            if i > 1:
                self.addLink(s[i-1], s[i-2])


topos = {'linear': (lambda: LinearTopo())}
