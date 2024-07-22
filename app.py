import pygame

pygame.init()

beige_marka = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)
black=(0, 0, 0)
dark_green = (0, 100, 0)
cornflower_blue = (100, 149, 237)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 너비, 높이 설정 800x600
screen_width = 800
screen_height = 600

# 공 설정
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
ball_dx = 3
ball_dy = -3

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 40
paddle_dx = 0
paddle_speed = 6

screen = pygame.display.set_mode((screen_width, screen_height))
# 프로그램을 시작했을 떄 표시되는 제목
pygame.display.set_caption("벽돌 꺠기 게임")

# 게임 오버 상태
game_over = False



def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_x, game_over
    ball_x = screen_width // 2 - ball_width // 2
    ball_y = screen_height // 2 - ball_height // 2
    ball_dx = 3
    ball_dy = -3
    paddle_x = screen_width // 2 - paddle_width // 2
    game_over = False


# 메인 반복 구간
running = True
clock = pygame.time.Clock()

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN -> 키가 눌렷을 떄 발생
        if event.type == pygame.KEYDOWN:
            # K_LEFT -> 키보드의 왼쪽 화살표 키
            if event.key == pygame.K_LEFT:
                # paddle_dx = 음수로 설정해서 패들이 왼쪽으로 이동
                paddle_dx = -paddle_speed
            # K_RIGHT -> 키보드의 오른쪽 화살표 키
            if event.key == pygame.K_RIGHT:
                # paddle_dx = 양수로 설정해서 패들이 오른쪽으로 이동
                paddle_dx = paddle_speed
            if event.key == pygame.K_r and game_over:
                reset_game()
        # KEYUP -> 키가 떼어졌을 떄 발생
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # 패들이 멈추게 한다
                paddle_dx = 0

    if not game_over:
        # 패들 이동
        # 패들의 위치를 업데이트 하는 녀석
        paddle_x += paddle_dx
        # 패들이 화면의 왼쪽 경계를 넘지 않도록
        if paddle_x < 0:
            paddle_x = 0
        # 패들이 화면의 오른쪽 경계를 넘지 않도록
        if paddle_x > screen_width - paddle_width:
            paddle_x = screen_width - paddle_width

        # 공 이동 (+=는 ball_x = ball_x + ball_dx와 동일)
        ball_x += ball_dx
        ball_y += ball_dy

        # 공이 벽에 부딪힐 떄 반사
        # 1. 공이 좌우 벽에 부딪힐 떄
        if ball_x <= 0 or ball_x >= screen_width - ball_width:
            # 공의 x 방향을 반전함
            ball_dx = -ball_dx
        # 2. 공이 상하 벽에 부딪힐 떄
        if ball_y <= 0 or ball_y >= screen_height - ball_height:
            # 공의 y 방향을 반전함
            ball_dy = -ball_dy

        # 공이 화면 바닥에 도달하면 게임 오버
        if ball_y >= screen_height - ball_height:
            game_over = True

    # 화면 배경 색 설정
    screen.fill(beige_marka)

    # 공 그리기
    pygame.draw.ellipse(screen, ford_dark_charcoal, (ball_x, ball_y, ball_width, ball_height))

    # 패들 그리기
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, black, paddle_rect)

    # 게임 오버 화면 표시
    if game_over:
        game_over_text = font.render("Game Over - Press 'R' to Restart", True, dark_green)
        screen.blit(game_over_text, (
            screen_width // 2 - game_over_text.get_width() // 2,
            screen_height // 2 - game_over_text.get_height() // 2
        ))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 종료 처리
pygame.quit()
