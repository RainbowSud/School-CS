import random

class Part:
    def __init__(self):
        partA = ["pro", "intra", "de", "hyper", "hydraulic",
                 "flux", "pan", "ultra", "trans", "turbo", "mk 4"]
        partB = ["altoid", "neuro", "bio", "photon", "atomic", "particle",
                 "neutron", "ion", "flavinoid"]
        partC = ["attenuator", "sub-assembly", "generator", "drive", "capacitor",
                 "ionizer", "emitter", "reactor", "amplifier"]
        self.__partname = partA[random.randrange(0, len(partA))]
        self.__partname += "-" + partB[random.randrange(0, len(partB))]
        self.__partname += " " + partC[random.randrange(0, len(partC))]
        self.__partnum = random.randint(0,100000)

    def name(self):
        return self.__partname

    def number(self):
        return self.__partnum


def main():
    #part1 = Part()
    #print(format(part1.number(), "6.0f"), part1.name())

    partRack = []

    for i in range(10):
        p = Part()
        print("Mandalorian: [removes the ", p.name(),"]")
        partRack.append(p)

    for i in range(3):
        p = partRack.pop()
        print("Mandalorian: [re-installs the ", p.name(),"]")

    for i in range(5):
        p = Part()
        print("Mandalorian: [removes the ", p.name(),"]")
        partRack.append(p)

    for i in range(len(partRack)):
        p = partRack.pop()
        print("Mandalorian: [re-installs the ", p.name(),"]")



main()