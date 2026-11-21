
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

# Game settings
MOVEMENT_SPEED = 5
FONT_SIZE = 36

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Game")

# TODO 1: Background
background_image = pygame.image.load("pet_bg.jpg")
background_image = pygame.transform.scale(
    background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# TODO 2: Font
font = pygame.font.SysFont("Arial", FONT_SIZE)


# Pet class
class Pet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((60, 60))
        self.image.fill((139, 69, 19))

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    # TODO 3: Keep pet inside screen
    def move(self, x_change, y_change):

        self.rect.x = max(
            0,
            min(SCREEN_WIDTH - self.rect.width,
                self.rect.x + x_change)
        )

        self.rect.y = max(
            0,
            min(SCREEN_HEIGHT - self.rect.height,
                self.rect.y + y_change)
        )


# Food class
class Food(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 165, 0))

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


# Create pet and food
pet = Pet()
pet_food = Food()

# Create sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(pet)
all_sprites.add(pet_food)

# Game variables
food_collected = False
running = True

clock = pygame.time.Clock()

# Main game loop
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background_image, (0, 0))

    if not food_collected:

        # TODO 4: Move the pet
        keys = pygame.key.get_pressed()

        x_change = (
            keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        ) * MOVEMENT_SPEED

        y_change = (
            keys[pygame.K_DOWN] - keys[pygame.K_UP]
        ) * MOVEMENT_SPEED

        pet.move(x_change, y_change)

        # TODO 5: Collision detection
        if pet.rect.colliderect(pet_food.rect):

            all_sprites.remove(pet_food)
            food_collected = True

    # Draw sprites
    all_sprites.draw(screen)

    # TODO 6: Display message
    if food_collected:

        message = font.render(
            "Food Collected!", True, pygame.Color("black")
        )

        text_x = (SCREEN_WIDTH - message.get_width()) // 2
        text_y = (SCREEN_HEIGHT - message.get_height()) // 2

        screen.blit(message, (text_x, text_y))

    # Update screen
    pygame.display.update()

    clock.tick(60)

# Quit game
pygame.quit()
