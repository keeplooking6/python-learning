import pygame
import random

# 游戏窗口尺寸
WIDTH = 640
HEIGHT = 480

# 贪吃蛇方块大小和速度
BLOCK_SIZE = 20
SNAKE_SPEED = 5

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 游戏时钟
clock = pygame.time.Clock()

# 显示得分
def show_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("得分: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

# 绘制贪吃蛇
def draw_snake(snake_body):
    if snake_body:
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE),0)

# 主游戏循环
def game_loop():
    game_over = False
    game_exit = False

    # 贪吃蛇初始位置和移动方向
    x = WIDTH / 2
    y = HEIGHT / 2
    dx = 0
    dy = 0

    # 贪吃蛇身体列表
    snake_body = []
    snake_length = 1

    # 食物位置
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_exit:
        while game_over:
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 50)
            text = font.render("游戏结束！再玩一次请按R键。", True, WHITE)
            screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != BLOCK_SIZE:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -BLOCK_SIZE:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy != BLOCK_SIZE:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy != -BLOCK_SIZE:
                    dx = 0
                    dy = BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += dx
        y += dy

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_body)
        show_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()

game_loop()