import pygame, sys , random

from pygame.constants import QUIT

def ball_animation(): #hàm di chuyển của bóng
    global ball_speed_x,ball_speed_y,player_score,opponent_score,score_time #khai báo biến global
    ball.x += ball_speed_x 
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height: #nếu top của bóng <0 hoặc bottom của bóng lớn hơn screen thì sẽ bị đập lại ( speed = -1 )
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1 

    if ball.left <= 0: #nếu ball đi qua bên trái kịch  thì player_score sẽ cộng thêm 1
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width: #nếu ball đi qua bên trái kịch  thì opponent_score sẽ cộng thêm 1
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) <10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) <10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
def player_animation(): #hàm di chuyển của player
    player.y += player_speed
    if player.top <= 0: #nếu player chạm đến top thì sẽ cho speed bằng 0
        player.top =0
    if player.bottom >= screen_height: #nếu player chạm bottom thì sẽ cho speed bằng 0
        player.bottom = screen_height

def opponent_animation(): #hàm di chuyển của opponent
    if opponent.top < ball.y: #nếu top của opponent dưới ball thì sẽ cho opponent di chuyển lên bằng quả bóng
        opponent.top += opponent_speed
    if opponent.bottom > ball.y: #nếu bottom của opponent dưới ball thì sẽ cho opponent di chuyển xuống bằng quả bóng
        opponent.bottom -= opponent_speed
    if opponent.top <= 0: #tương tự như player
        opponent.top = 0
    if opponent.bottom >= screen_height:
        player.bottom = screen_height

def ball_start(): #hàm ball start (dùng khi bắt đầu game và lúc ghi điểm sẽ set lại)
    global ball_speed_x, ball_speed_y,score_time #khai báo biến global

    current_time = pygame.time.get_ticks() #set current time bằng hàm pygame.get_ticks
    ball.center = (screen_width/2, screen_height/2) #set vị trí ball ở center

    #Thời gian đếm ngược trước khi bắt đầu chơi
    if current_time - score_time < 700: 
        number_three = game_font.render("3",False,red_color)
        screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_number = game_font.render("2",False,red_color)
        screen.blit(number_number,(screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,red_color)
        screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else: #cho ball bắt đầu di chuyển theo hướng random
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None
        



# General setup
pygame.init()  #Khởi động pygame
clock = pygame.time.Clock() #Set clock cho game

# Setting up the main window
screen_width = 1280 #set chiều rộng của giao diện game
screen_height = 960 #set chiều dài của game
screen = pygame.display.set_mode((screen_width,screen_height)) #render chiều dài,chiều rộng đã set lên màn hình chính
pygame.display.set_caption('Pong') #set caption của game

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30) #tạo ball bằng hàm rectangles
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140) #tạo player và opponent bằng hàm rectangles
opponent = pygame.Rect(10, screen_height/2 -70,10,140)

bg_color = pygame.Color('#2F373F') #set màu background chủ đạo của game
light_grey = (27,35,43) 
red_color = (168,35,35)


ball_speed_x = 7 * random.choice((1, -1)) #set tốc độ di chuyển của bóng theo chiều ngang
ball_speed_y = 7 * random.choice((1, -1)) #set tốc độ di chuyển của bóng theo chiều đứng
player_speed = 0 #set tốc độ của player,khởi đầu bằng 0
opponent_speed = 25 #set tốc độ của opponent 
ball_moving = False
score_time = True

# Text Variables
player_score = 0 #điểm của player
opponent_score = 0 #điểm của opponent
game_font = pygame.font.Font("freesansbold.ttf",32) #set font chữ hiển thị trên màn hình game


#SOund
pong_sound = pygame.mixer.Sound("1.wav")
score_sound = pygame.mixer.Sound("2.wav")

# Score Timer
score_time = 1

#Hàm bắt tất cả các sự kiện của game
while True:
    # Handling input
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #hàm pygame.quit dùng để thoát hẳn chương trình game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #hàm dùng để điều khiển player.
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation() #Hàm chuyển động của bóng
    player_animation() #hàm chuyển động của player
    opponent_animation() #hàm chuyển động của opponent

    # Visuals
    screen.fill(bg_color) #render màu đã set cho screen
    pygame.draw.rect(screen,red_color, player) #render ra thanh ngang của player
    pygame.draw.rect(screen,red_color, opponent) #render ra thanh ngang của opponent
    pygame.draw.ellipse(screen,red_color,ball) #render ra ball
    pygame.draw.aaline(screen,light_grey, (screen_width/2,0), (screen_width/2,screen_height)) #render ra thanh chia đôi màn hình ở giữa


    if score_time:
        ball_start() #hàm mặc định khi ball bắt đâu di chuyển

    player_text = game_font.render(f"{player_score}",False,red_color) 
    screen.blit(player_text,(660,470)) #vị trí của điểm player

    opponent_text = game_font.render(f"{opponent_score}",False,red_color)
    screen.blit(opponent_text,(600,470)) #vị trí của điểm opponent

    # Updating the window
    pygame.display.flip()
    clock.tick(60)