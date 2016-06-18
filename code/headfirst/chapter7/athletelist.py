class AthleteList(list):

    def __init__(self, name, dob=None, times=[]):
        # intializing the derived from class, and then
        list.__init__([])
        # Assigning the arguments to the attributes
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
