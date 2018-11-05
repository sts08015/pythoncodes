
# coding: utf-8

# In[4]:


import pygame  # import pygame module   
import random  # import random module

# 더 추가한점
# 난이도 시스템을 추가하여 난이도에 따라서 FPS 증가값을 바꾸어 주었다. 

# MADE BY FISMA(2311 임동균)


# In[5]:


print("난이도를 선택하세요 1->하, 2->중, 3-> 상")
a = int(input())


# In[6]:


pygame.init()  #pygame 라이브러리 초기화
screen = pygame.display.set_mode((480,640)) # set screen size
FPS = 30  # set FPS 
fpsClock = pygame.time.Clock()  #시간 체크를 위한 변수 설정
asteroidtimer = 100
asteroids = [[20,0,0]]
score = 0
try: #파일 입력받고 시작 음악 출력
    spaceshipimg = pygame.image.load("./img/spaceship.png")  # 이미지를 코드에 적힌 대로 폴더에 넣으세요 !!!!!
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0,asteroid1,asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")
    
    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    takeoffsound.play()
except Exception as err: # 위의 파일로드가 안되는 경우, 에러문 출력
    print('그림 또는 효과음 삽입에 문제가 있습니다. : ', err)
    pygame.quit()
    exit(0)

def text(arg,x,y):
    font = pygame.font.Font(None,24) #기본 폰트
    text = font.render("Score: " + str(arg).zfill(6),True,(0,0,0))
    textRect = text.get_rect() # 출력위치 저장
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text,textRect) #텍스트 출력
    
running = True
while running:
    screen.fill((255,255,255)) #화면을 흰색으로 채우기 
    for event in pygame.event.get(): #이벤트 목록에서 순서대로 event에 저장
        if event.type == pygame.QUIT: # X클릭 게임 중간에 종료할 경우 
            pygame.quit()   #pygame 종료 
            exit(0)# 프로그램 종료
    score +=1
    text(score,400,10)
    if score%100 == 0: # 100마다 FPS 증가 
        if a==1:
            FPS+=2
        elif a== 2:
            FPS+=5
        else:
            FPS +=10
    position = pygame.mouse.get_pos() #마우스 좌표 받기 
    spaceshippos = (position[0],position[1]) #우주선 좌표
    screen.blit(spaceshipimg,spaceshippos) #우주선을 주어진 좌표에 출력
    spaceshiprect = pygame.Rect(spaceshipimg.get_rect())
    spaceshiprect.left = spaceshippos[0]
    spaceshiprect.top = spaceshippos[1]
    asteroidtimer -= 10
    if asteroidtimer <=0:
        asteroids.append([random.randint(5,475),0,random.randint(0,2)]) # 마지막 값 : 어떤 소행성인지 판별
        asteroidtimer = random.randint(50,200)                          # 첫번째, 두번째 값 : position of asteroid
    index = 0                                                           
    for stone in asteroids:
        stone[1]+=10
        if stone[1]>640:
            asteroids.pop(index) # 돌의 y좌표가 640보다 크면 pop 
        stonerect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stonerect.left = stone[0]
        stonerect.top = stone[1]
        if stonerect.colliderect(spaceshiprect): # 충돌
            landingsound.play()
            asteroids.pop(index)
            running = False# while 종료 
        screen.blit(asteroidimgs[stone[2]],(stone[0],stone[1])) #이미지그리기 
        index+=1 
    fpsClock.tick(FPS)
    pygame.display.flip() #화면 전체 업데이트 
screen.blit(gameover,(0,0))
text(score,screen.get_rect().centerx,screen.get_rect().centery)
pygame.display.flip() #화면 전체 업데이트
        
while True:  # 게임 종료 후 종료할 경우
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #X버튼 클릭
            pygame.quit() #pygame 종료
            exit(0)# 프로그램 종료
        

