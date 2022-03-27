class Chance :

    def __init__(self):
        pass

    def get_assets(self,chance,bodypart):
        '''
        vive la doc yoohoo
        '''
        #################   PETITS TESTS  ######################
        assert bodypart in ['l','r'], "this bodypart doesn't exist | bodypart are → 'r' - 'l'"
        assert chance <= 100, "chance's too high | limited to 100"
        assert chance >= 1, "chance's too low | minimum to 1"
        #################   MAIN GAUCHE  #######################
        if bodypart == 'l':
            if chance <= 5 : return 'bracelet1.png'
            if chance <= 8 : return 'bracelet2.png'
            if chance <= 15 : return 'bracelet3.png'
            else : return 'void.png'
        #################   MAIN DROITE  #######################
        elif bodypart == 'r':
            if chance <= 10 : return 'iwatch.png'
            else : return 'void.png'


