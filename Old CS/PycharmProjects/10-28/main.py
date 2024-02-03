class HallOfFlags:
    def __init__(self, flagMontage):
        self.__montage = flagMontage

    def display(self):
        print(self.__montage)

    def genes(self):
        index = self.__montage.find("usa")
        print(index)
        s = self.__montage[index+3:]
        print(s)
        index = s.find("usa")
        s = s[:index]
        print(s)



def main():
    sunroom = HallOfFlags("peruusacanadaboliviarussiaukusamontanausazimbabwe")

    sunroom.display()
    sunroom.genes()



main()

