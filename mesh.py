from mininet.topo import Topo


class MeshTopo(Topo):

    def __init__(self, n=3):
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
            for j in range(len(s)-1):
                self.addLink(s[j], s[-1])
        '''    
        # Adding hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Adding switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Adding links between hosts and switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

        # Adding links between switches
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        # self.addLink(s1, s2)
        # self.addLink(s2, s3)
        # self.addLink(s3, s4)
        # self.addLink(s4, s1)
        '''

topos = {'mesh': (lambda: MeshTopo())}
