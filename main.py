import pygame
from pygame.locals import *
import sys


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400

        self.dark_blue = 12, 80, 97
        self.speed = [1, 1]

        self.ball = pygame.image.load("images/ball.gif")
        self.ballrect = self.ball.get_rect()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Bomberman')
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        self.on_init()
        #if self.on_init() == False:
        #    self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.ballrect = self.ballrect.move(self.speed)
            if self.ballrect.left < 0 or self.ballrect.right > self.width:
                self.speed[0] = -self.speed[0]
            if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
                self.speed[1] = -self.speed[1]

            self._display_surf.fill(self.dark_blue)
            self._display_surf.blit(self.ball, self.ballrect)
            pygame.display.flip()

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()