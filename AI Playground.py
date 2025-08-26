import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter with Power-Ups")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

# Player settings
player_size = 50
player_speed = 7
max_health = 5

# Enemy settings
enemy_size = 40
enemy_speed = 7
spawn_delay = 50  # spawn every 500 milliseconds

# Bullet settings
bullet_speed = 10
bullet_size = 5
normal_fire_delay = 400  # milliseconds between shots

# Power-up settings
powerup_size = 30
powerup_spawn_delay = 10000  # spawn every 10 seconds
powerup_duration = 5000  # 5 seconds for rapid fire

font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Classes
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, player_size, player_size)
        self.speed = player_speed
        self.health = 100
        self.last_shot = 0  # time since last bullet fired
        self.fire_delay = normal_fire_delay
        self.rapid_fire_end_time = 0

    def move(self, keys):
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot >= self.fire_delay

    def shoot(self, mouse_pos):
        self.last_shot = pygame.time.get_ticks()
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1
        direction = (dx / dist, dy / dist)
        return Bullet(self.rect.centerx, self.rect.centery, direction)

    def activate_rapid_fire(self):
        self.fire_delay = normal_fire_delay // 2
        self.rapid_fire_end_time = pygame.time.get_ticks() + powerup_duration

    def update(self):
        if self.rapid_fire_end_time and pygame.time.get_ticks() > self.rapid_fire_end_time:
            self.fire_delay = normal_fire_delay
            self.rapid_fire_end_time = 0

class Enemy:
    def __init__(self):
        x = random.choice([random.randint(-100, -enemy_size), random.randint(WIDTH + enemy_size, WIDTH + 100)])
        y = random.randint(0, HEIGHT - enemy_size)
        self.rect = pygame.Rect(x, y, enemy_size, enemy_size)
        self.speed = enemy_speed

    def move_towards_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, bullet_size, bullet_size)
        self.speed = bullet_speed
        self.direction = direction

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.rect)

class PowerUp:
    def __init__(self):
        self.type = random.choice(['health', 'rapid_fire'])
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - powerup_size),
            random.randint(0, HEIGHT - powerup_size),
            powerup_size,
            powerup_size
        )
        self.color = YELLOW if self.type == 'health' else PURPLE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def draw_health(surface, health):
    text = font.render(f'Health: {health}', True, WHITE)
    surface.blit(text, (10, 10))

def draw_score(surface, score):
    text = font.render(f'Score: {score}', True, WHITE)
    surface.blit(text, (WIDTH - 150, 10))

def draw_powerup_timer(surface, player):
    if player.rapid_fire_end_time:
        remaining = (player.rapid_fire_end_time - pygame.time.get_ticks()) / 1000
        text = font.render(f'Rapid Fire: {remaining:.1f}s', True, PURPLE)
        surface.blit(text, (WIDTH // 2 - 80, 10))

def main():
    player = Player()
    enemies = []
    bullets = []
    powerups = []
    score = 0

    spawn_enemy_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_enemy_event, spawn_delay)  # Set to spawn every 500ms

    spawn_powerup_event = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_powerup_event, powerup_spawn_delay)

    running = True
    while running:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == spawn_enemy_event:
                enemies.append(Enemy())
            if event.type == spawn_powerup_event:
                powerups.append(PowerUp())

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.update()

        # Shooting bullets with fire rate limit
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Left mouse button held down
            if player.can_shoot():
                bullet = player.shoot(mouse_pos)
                bullets.append(bullet)

        # Move enemies
        for enemy in enemies[:]:
            enemy.move_towards_player(player)
            if enemy.rect.colliderect(player.rect):
                player.health -= 1
                enemies.remove(enemy)
                if player.health <= 0:
                    running = False

        # Move bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
                bullets.remove(bullet)
            else:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        enemies.remove(enemy)
                        if bullet in bullets:
                            bullets.remove(bullet)
                        score += 1
                        break

        # Check powerup collisions
        for powerup in powerups[:]:
            if player.rect.colliderect(powerup.rect):
                if powerup.type == 'health' and player.health < max_health:
                    player.health += 1
                elif powerup.type == 'rapid_fire':
                    player.activate_rapid_fire()
                powerups.remove(powerup)

        # Draw everything
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for powerup in powerups:
            powerup.draw(screen)

        draw_health(screen, player.health)
        draw_score(screen, score)
        draw_powerup_timer(screen, player)

        pygame.display.flip()

    # Game Over screen
    screen.fill(BLACK)
    game_over_text = font.render(f'Game Over! Final Score: {score}', True, WHITE)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
