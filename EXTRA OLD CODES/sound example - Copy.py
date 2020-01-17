import pygame , os

pygame.mixer.init()


def sound(string_name) :
    try :
        pygame.mixer.music.load( os.path.join( 'Sounds' , "%s.wav" %string_name ) )
        return pygame.mixer.music.play()
    except :
        pass
    


sound("Alan Walker")

