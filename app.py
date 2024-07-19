import pygame

pygame.init()

beige_marka = (250, 237, 201)

# 너비, 높이 설정 800x600
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
# 프로그램을 시작했을 떄 표시되는 제목
pygame.display.set_caption("벽돌 꺠기 게임")

# 메인 반복 구간
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 배경 색 설정
    screen.fill(beige_marka)

    # 화면 업데이트
    pygame.display.flip()

# 종료 처리
pygame.quit()