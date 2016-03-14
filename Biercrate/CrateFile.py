"""This is a model"""

class Crate(object):
    """This is a biercrate"""
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    print('im a biercrate')
    crateContent = [24]
    crateContent.append('stiegl')

    def Run(self,args):
        FillCrate()
        Print()

    def FillCrate(self):
        for x in crateContent:
            x = Bottle()

    def Print(self):
        print(crateContent)

class Bottle(object):
    """This is a Bottle"""
    print ("I am a Bottle")


