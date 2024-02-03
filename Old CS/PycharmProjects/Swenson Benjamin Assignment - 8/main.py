# Benjamin Swenson - CS1400 Section 1
class Genome:  # My Class
    def __init__(self, gene="a"):  # keeps the shabang nice and neat if there is no input from consumer boys
        self.__gene = gene

    def display(self):  # This be the display method
        s = str(self.__gene)  # converts into a str
        s = s.upper()  # upper case
        for i in "BDEFHIJKLMNOPQRSUVWXYZ./:;{}|[]?!@#$%^&*()1234567890-=_+`~<>,":
            # my lazy way of filtering out everything but TAGC
            s = s.replace(i, "")
        print(s)

    def genes(self):  # This is the gene thing to display the genes in the genome
        # Gene starts after ATG - Ends before TAG TAA or TGA
        # Gene is a multiple of 3 - does NOT contain ATG TAG TAA or TGA
        s = self.__gene.find("ATG")  # This section finds the first ATG and chops off the string up to there
        if s == -1:  # This shows if there is no ATG in the string, then there is no Gene present
            return print("no gene is found")
        s = self.__gene[s+3:]
        index1 = s.find("TAG")  # These indexes find if any gene ending triplets are present
        index2 = s.find("TAA")
        index3 = s.find("TGA")
        if index1 == -1:  # This part adds the length of the string to the index value, because if the find function
            index1 += len(s)  # Does not find the character it returns a -1, and that messes with my min function
        if index2 == -1:
            index2 += len(s)
        if index3 == -1:
            index3 += len(s)
        t = s[:min(index1, index2, index3)]  # Finds the minimum of these indexes to know which comes first
        if len(t) % 3 == 0:  # This checks if the gene is a multiple of 3
            print(t)
        for i in range(1000):  # This for loop, loops finding any other ATGs and cuts them off
            index = s.find("ATG")  # It basically copies lines 17-32, and finds the rest of the genes
            if index == -1:  # The 1000 is just to make it loop a ton of times, but it cuts off fast cause of this line
                return
            s = s[index+3:]
            index1 = s.find("TAG")
            index2 = s.find("TAA")
            index3 = s.find("TGA")
            if index1 == -1:
                index1 += len(s)
            if index2 == -1:
                index2 += len(s)
            if index3 == -1:
                index3 += len(s)
            t = s[:min(index1, index2, index3)]
            if len(t) % 3 == 0:
                print(t)


def main():

    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
