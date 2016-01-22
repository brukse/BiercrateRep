
class Crate(object):
    """This is a biercrate"""
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    print('im a biercrate')
    crateContent = [24]
    crateContent.append('stiegl')

    def Run(args):
        FillCrate()
        Print()

    def FillCrate():
        for x in crateContent:
            x = Bottle()

    def Print():
        print(crateContent)

class Bottle(object):
    """This is a Bottle"""
    print ("I am a Bottle")
    

