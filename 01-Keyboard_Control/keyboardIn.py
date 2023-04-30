import pygame

#initialise a pygame window, we use this to easily grab controls.
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for e in pygame.event.get():
        pass
    keyIn = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyIn[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    print(getKey("a"))

if __name__ == '__main__':
    init()
    while True:
        main()