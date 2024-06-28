class IPL(object):
    def __init__(self, *args, **kw):
        pass

    def ipl_function(self):
        pass


class Stadium(IPL):
    def __init__(self, *args, **kw):
        IPL.__init__(self, *args, **kw)

    def ipl_function(self):
        print ("Component....")


class Team(IPL):
    def __init__(self, *args, **kw):
        IPL.__init__(self, *args, **kw)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def ipl_function(self):
        map(lambda x: x.ipl_function(), self.children)


class Player:
    pass
class Coach:
    pass
class CheerLeader:
    pass



team = Team()
chinnapaStadium = Stadium()
mumbaiStadium = Stadium()
team.append_child(chinnapaStadium)
team.append_child(mumbaiStadium)
team.ipl_function()