import pygame
from obj.circle import Circle
from obj.square import Square
from system.camera import Camera
from system.animation import animation
from random import randint

# 귀차나
F = False
T = True

# pygame 세팅
pygame.init()
screen = pygame.display.set_mode((500, 1000))
clock = pygame.time.Clock()

# 환경변수
center = (screen.get_size()[0] / 2, screen.get_size()[1] / 2)
originh = 400
d = 0
originhight = 150
jumphight = originhight
jumped = F

# 타이머 세팅
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 2)
uptimer = pygame.USEREVENT + 2
pygame.time.set_timer(uptimer, 1000)

# 카메라 세팅
camera = Camera((0, 0))

# 오브젝트 세팅
circle1 = Circle(screen, (250, 250), (255, 0, 0), 5, camera)
dedline = Square(screen, (int(center[0]), 800), (100, 0, 0), 500, 30, camera)

superjumps = []
squares = []
deads = []

objvalue = [0, 0, 0]

squares.append(Square(screen,
                      (250, 450),
                      (0, 0, 0),
                      100,
                      15,
                      camera
                      )
               )

# 오브젝트 생성
for i in range(11):
    objvalue[0] = i
    squares.append(Square(screen,
                          (randint(30, 470), -((i - 1) * 100) + 500),
                          (0, 0, 0),
                          100,
                          15,
                          camera
                          )
                   )

for i in range(2):
    objvalue[1] = i
    superjumps.append(Square(screen,
                             (randint(30, 470), -((i - 1) * 1000) + randint(400, 1000)),
                             (0, 255, 0),
                             30,
                             10,
                             camera
                             )
                      )

for i in range(2):
    objvalue[2] = i
    deads.append(Square(screen,
                        (randint(30, 470), -((i - 1) * 1000) + randint(100, 1000)),
                        (255, 0, 0),
                        150,
                        10,
                        camera
                        )
                 )

font = pygame.font.Font(None, 30)

# 벡터 계산을 위한 이전 위치 저장
last_pos = circle1.position


def addid(objid: int):
    global objvalue

    if objid == 0:
        objvalue[0] += 1
        squares.append(Square(screen,
                              (randint(30, 470), -((objvalue[0] - 1) * 100) + 500),
                              (0, 0, 0),
                              100,
                              15,
                              camera
                              )
                       )
    elif objid == 1:
        objvalue[1] += 1
        superjumps.append(Square(screen,
                                 (randint(30, 470), -((objvalue[1] - 1) * 1000) + randint(0, 500)),
                                 (0, 255, 0),
                                 30,
                                 10,
                                 camera
                                 )
                          )
    elif objid == 2:
        objvalue[2] += 1
        deads.append(Square(screen,
                            (randint(30, 470), -((objvalue[2] - 1) * 1000) + randint(0, 500)),
                            (255, 0, 0),
                            150,
                            10,
                            camera
                            )
                     )


t = 1
score = 0
running = T
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = F
        elif event.type == TIMER_EVENT:
            d += 0.002
            camera.position = (camera.position[0], (camera.position[1] + .1 * t))
        elif event.type == uptimer:
            t += 0.01

    # 점수 업데이트
    if circle1.position[1] < -score:
        score = -int(circle1.position[1])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle1.move(-4)
    if keys[pygame.K_RIGHT]:
        circle1.move(4)

    if circle1.position[1] + camera.position[1] > screen.get_size()[1]:
        running = F

    if d >= 0.5:
        jumped = F
    else:
        jumped = T

    screen.fill((255, 255, 255))

    # 충돌 처리
    if not jumped and dedline.check_collision(circle1):
        running = F

    for square in squares:
        if square.isoutofscreen():
            addid(0)
            squares.pop(0)
        else:
            if not jumped and square.check_collision(circle1):
                jumphight = originhight
                originh = int(circle1.position[1])
                d = 0
        square.draw()

    for jumppad in superjumps:
        if jumppad.isoutofscreen():
            addid(1)
            superjumps.pop(0)
        else:
            if not jumped and jumppad.check_collision(circle1):
                jumphight = originhight * 3
                originh = int(circle1.position[1])
                d = 0
        jumppad.draw()

    for dead in deads:
        if dead.isoutofscreen():
            addid(2)
            deads.pop(0)
        else:
            if dead.check_collision(circle1):
                running = F
            dead.draw()

    # 화면 경계 처리
    if circle1.position[0] < 0:
        circle1.position = (screen.get_size()[0], circle1.position[1])
    elif circle1.position[0] > screen.get_size()[0]:
        circle1.position = (0, circle1.position[1])

    # 점프 애니메이션
    circle1.position = (circle1.position[0], animation(d, jumphight, originh))

    # 지금 위치 저장
    curr_pos = circle1.position

    # 벡터x랑 y저장
    vx = curr_pos[0] - last_pos[0]
    vy = curr_pos[1] - last_pos[1]

    # 화면상의 좌표 그래서 카메라 있음
    sx = int(curr_pos[0])
    sy = int(curr_pos[1] + camera.position[1])

    # 벡터 xy축에 10 곱해주고
    end_pos = (sx + vx * 10, sy + vy * 10)

    # 표시한후
    pygame.draw.line(screen, (0, 0, 255), (sx, sy), end_pos, 2)

    # 다시 현 위치 저장
    last_pos = curr_pos

    text = font.render(str(score), True, (0, 0, 0))
    screen.blit(text, (center[0], 10))
    circle1.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
