import pygame
import sys
import random
import psycopg2
import json

# Initialize pygame
pygame.init()

# Constants
SW, SH = 800, 800
BLOCK_SIZE = 50
FONT_SIZE = 25
FONT = pygame.font.Font(None, FONT_SIZE)

# Setup the display
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

# Database connection
conn = psycopg2.connect(dbname='snakebase', user='postgres', password='2004', host='localhost', port='5433')
cur = conn.cursor()

def get_user_id(username):
    cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
    user_id = cur.fetchone()
    if user_id is None:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
        conn.commit()
        user_id = cur.fetchone()
    return user_id[0]

def save_game_state(user_id, score, level, snake_body):
    game_state = {'snake_body': [(rect.x, rect.y) for rect in snake_body]}
    cur.execute("INSERT INTO user_scores (user_id, score, level, game_state) VALUES (%s, %s, %s, %s);",
                (user_id, score, level, json.dumps(game_state)))
    conn.commit()

def get_record(user_id):
    cur.execute("SELECT MAX(score) FROM user_scores WHERE user_id = %s;", (user_id,))
    result = cur.fetchone()[0]
    return result if result else 0

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self, apple):
        if self.head.colliderect(apple.rect):
            self.body.append(pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
            apple.reset()
            return 'eat'

        for square in self.body[:-1]:
            if self.head.colliderect(square):
                self.dead = True
                break

        if self.dead:
            return 'dead'

        self.body.append(self.head.copy())
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.pop(0)

        if not 0 <= self.head.x < SW or not 0 <= self.head.y < SH:
            self.dead = True
            return 'dead'
        return 'ok'

class Apple:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, (SW // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.rect.y = random.randint(0, (SH // BLOCK_SIZE) - 1) * BLOCK_SIZE

def draw_game(snake, apple, score, level, record):
    screen.fill('black')
    pygame.draw.rect(screen, "orange", apple.rect)
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    score_text = FONT.render(f"Score: {score}", True, "white")
    level_text = FONT.render(f"Level: {level}", True, "white")
    record_text = FONT.render(f"Record: {record}", True, "white")
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (220, 10))
    screen.blit(record_text, (430, 10))

def main():
    running = True
    level = 1
    apples_eaten = 0
    snake = Snake()
    apple = Apple()
    username = input("Enter your username: ")
    user_id = get_user_id(username)
    record = get_record(user_id)
    current_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake.ydir == 0:
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP and snake.ydir == 0:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_RIGHT and snake.xdir == 0:
                    snake.ydir = 0
                    snake.xdir = 1
                elif event.key == pygame.K_LEFT and snake.xdir == 0:
                    snake.ydir = 0
                    snake.xdir = -1
                elif event.key == pygame.K_s:
                    current_score = len(snake.body)
                    save_game_state(user_id, current_score, level, snake.body)
                elif event.key == pygame.K_p:
                    pygame.time.wait(5000)  # Simple pause, waits 5 seconds

        game_state = snake.update(apple)
        current_score = len(snake.body)
        if game_state == 'dead':
            if current_score > record:
                save_game_state(user_id, current_score, level, snake.body)
            snake.reset()
            level = 1
            apples_eaten = 0
        elif game_state == 'eat':
            apples_eaten += 1
            if apples_eaten % 5 == 0:
                level += 1

        draw_game(snake, apple, current_score, level, record)
        pygame.display.update()
        clock.tick(4 + level * 0.1)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
