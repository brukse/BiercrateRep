import sys

def main():
    myCrate = Crate('olback')
    myCrate.Run()
    #myCrate.FillCrate()
    #myCrate.Print()


class Crate(object):
    """This is a biercrate"""

    """This is a biercrate constructor"""
    def __init__(self, cName):
        self.Name = cName
        self.crateContent = list()
        self.uniqueDrinks = list()    
    
    

    def FillUnique(self):
        self.uniqueDrinks.append(Bottle('Falcon',20,'Öl'))
        self.uniqueDrinks.append(Bottle('APA',20,'Öl'))
        self.uniqueDrinks.append(Bottle('IPA',20,'Öl'))
        self.uniqueDrinks.append(Bottle('Julmust',10,'Läsk'))
        self.uniqueDrinks.append(Bottle('Bingo',10,'Läsk'))
        self.uniqueDrinks.append(Bottle('Ramlösa',10,'Vatten'))

    def Run(self):
        mnuSel = 1
        self.FillUnique()
        try:
            while (mnuSel > 0 and mnuSel != 7):
                self.PrintMenu()
                mnuSel = int(input('Skriv en siffra: \n\r'))
                self.PySwitch(mnuSel)
                self.PrintCrate()

        except Exception as exinst:
            print(exinst.args)
            print(exinst)
       

   

    def PrintMenu(self):
        print('Hej och välkomna till ölbacken')
        print('Menyval:')
        print('1: Fyll backen med unika flaskor, en av varje sort.')
        print('2: Fyll backen med slumpvisa flaskor.')
        print('3: Fyll backen med valda flaskor.')
        print('4: Byt en sort mot en annan.')
        print('5: ???????')
        print('6: ???????')
        print('7: ???????')
        print('8: Töm allt innehåll i backen.')
        print('9: Skriv ut innehållet i backen.')
    
    def FillUniqueCrate(self):
        for b in self.uniqueDrinks:
            if b not in self.crateContent:
                self.FillCrate(b)

    def FillCrate(self,aBottle):
        self.crateContent.append(aBottle)
                


    def FillRandomCrate(self):
        print('Not implemented')

    def FillChosenBottles(self):
        print('Not implemented')
    
    def SwitchBottles(self):
        print('Not implemented')

    def EmptyCrate(self):
        self.crateContent = []

    def PrintCrate(self):
        for b in self.crateContent:
            print(b.bottleName , str(b.price) , b.drinktype)
 

    def PySwitch(self,mnuChoice):
        # map the inputs to the function blocks
        
        mnuoptions = {
                   1 : self.FillUniqueCrate,
                   2 : self.FillRandomCrate,
                   3 : self.FillChosenBottles,
                   4 : self.SwitchBottles,
                   5 : 'pass',
                   6 : 'pass',
                   7 : 'pass',
                   8 : self.EmptyCrate,
                   9 : self.PrintCrate,
        }
        func = mnuoptions.get(mnuChoice, lambda: "nothing")
        return func()

class Bottle(object):
    """This is a Bottle"""
    def __init__(self, bottleName=None, price=None, drinktype=None):
        self.bottleName = bottleName
        self.price = price
        self.drinktype = drinktype
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))