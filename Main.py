import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))  # White color
        self.rect = self.surf.get_rect(center = (400, 300))

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

# Initialize player
player = Player()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(player.surf, player.rect)
    pygame.display.update()









    class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 0, 0))  # Red color
        self.rect = self.surf.get_rect(center=(random.randint(20, 780), random.randint(20, 580)))

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 255, 0))  # Green color
        self.rect = self.surf.get_rect(center=(random.randint(20, 780), random.randint(20, 580)))

# Initialize obstacles and collectibles
obstacles = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for _ in range(5):  # Adjust number of obstacles
    obstacle = Obstacle()
    obstacles.add(obstacle)
    all_sprites.add(obstacle)

for _ in range(3):  # Adjust number of collectibles
    collectible = Collectible()
    collectibles.add(collectible)
    all_sprites.add(collectible)
     # Collision detection
    for entity in collectibles:
        if player.rect.colliderect(entity.rect):
            score += 1
            entity.kill()

    for entity in obstacles:
        if player.rect.colliderect(entity.rect):
            running = False  # Game Over

    # Update game window
    screen.fill((0, 0, 0))  # Fill the screen with black
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

pygame.quit()