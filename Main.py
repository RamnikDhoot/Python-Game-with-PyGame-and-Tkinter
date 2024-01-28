import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Player character class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))  # White color
        self.rect = self.surf.get_rect(center=(400, 300))

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 0, 0))  # Red color
        self.rect = self.surf.get_rect(center=(random.randint(20, 780), random.randint(20, 580)))

# Collectible class
class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 255, 0))  # Green color
        self.rect = self.surf.get_rect(center=(random.randint(20, 780), random.randint(20, 580)))

# Initialize player
player = Player()

# Initialize obstacles and collectibles
obstacles = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Add obstacles and collectibles to their groups
for _ in range(5):
    obstacle = Obstacle()
    obstacles.add(obstacle)
    all_sprites.add(obstacle)

for _ in range(3):
    collectible = Collectible()
    collectibles.add(collectible)
    all_sprites.add(collectible)

# Game loop
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Collision detection
    for entity in collectibles:
        if player.rect.colliderect(entity.rect):
            score += 1
            entity.kill()

    for entity in obstacles:
        if player.rect.colliderect(entity.rect):
            running = False  # Game Over

    # Update game window
    screen.fill((0, 0, 0))  # Clear the screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.update()

pygame.quit()
