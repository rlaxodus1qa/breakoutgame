import pygame

pygame.init()

beige_marka = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)
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

screen = pygame.display.set_mode((screen_width, screen_height))
# 프로그램을 시작했을 떄 표시되는 제목
pygame.display.set_caption("벽돌 꺠기 게임")

# 메인 반복 구간
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 공 이동 (+=는 ball_x = ball_x + ball_dx와 동일)
    ball_x += ball_dx
    ball_y += ball_dy

    # 공이 벽에 부딪힐 떄 반사
    # 1. 공이 좌우 벽에 부딪힐 떄
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_dx = -ball_dx # 공의 x 방향을 반전함
    # 2. 공이 상하 벽에 부딪힐 떄
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        # 공의 y 방향을 반전함
        ball_dy = -ball_dy

    # 화면 배경 색 설정
    screen.fill(beige_marka)

    # 공 그리기
    pygame.draw.ellipse(screen, ford_dark_charcoal, (ball_x, ball_y, ball_width, ball_height))


    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 종료 처리
pygame.quit()
