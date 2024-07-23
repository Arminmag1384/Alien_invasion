import sys
import pygame
from settings import  Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion: 

    
    def __init__(self):

        pygame.init()
        
        self.Clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_widht = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):

        while True:

            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.Clock.tick(60)

    def _check_events(self):
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                     
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

               # elif event.type == pygame.K_SPACE:
               #     self._fire_bullet()
               

    def _check_keydown_events(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True  

        if event.key == pygame.K_ESCAPE:
            sys.exit()    

        if event.key == pygame.K_SPACE:
            self._fire_bullet()    


    def _check_keyup_events(self, event):
         
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
            
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
                
            self.ship.blitme()

            pygame.display.flip()
            




if __name__ == '__main__':

  ai = AlienInvasion()                    
  ai.run_game()