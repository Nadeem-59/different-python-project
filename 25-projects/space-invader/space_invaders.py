import streamlit as st
import pygame
import numpy as np
import sys
import os
from pygame.locals import *
from pygame import font

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Emojis
PLAYER_EMOJI = "🚀"  # Rocket ship
ENEMY_EMOJI = "👾"   # Space invader
BULLET_EMOJI = "💫"  # Shooting star

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('segoe ui emoji', 40)
        self.image = self.font.render(PLAYER_EMOJI, True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.font = pygame.font.SysFont('segoe ui emoji', 30)
        self.image = self.font.render(ENEMY_EMOJI, True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.font = pygame.font.SysFont('segoe ui emoji', 20)
        self.image = self.font.render(BULLET_EMOJI, True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

def main():
    st.title("Space Invaders 🚀👾")
    
    # Initialize game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders 🚀👾")
    clock = pygame.time.Clock()
    
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    # Create player
    player = Player()
    all_sprites.add(player)
    
    # Create enemies
    for row in range(5):
        for column in range(10):
            enemy = Enemy(column * 70 + 50, row * 50 + 50)
            all_sprites.add(enemy)
            enemies.add(enemy)
    
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
        
        # Update
        all_sprites.update()
        
        # Check for collisions
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            # Add score or other effects here
            pass
        
        # Check if enemies reach the bottom
        for enemy in enemies:
            if enemy.rect.bottom >= SCREEN_HEIGHT:
                running = False
        
        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        
        # Control game speed
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 