import pygame, random, sys, mysql.connector 

# Defining movement and collision used in the loop .
def projectile_movement():
    global projectile_speed_x, projectile_speed_y, user_score, enemy_score 

    # Assigning variables to both x and y so we can seperately reverse speed.
    projectile.x += projectile_speed_x
    projectile.y += projectile_speed_y

    # Giving the projectile movement bounds set by the display size.
    if projectile.top <= 0 or projectile.bottom >= display_height:
        projectile_speed_y *= -1

    # Updating the score.
    if projectile.left <= 0:
        projectile_reset()
        user_score += 1

    if projectile.right >= display_width:
        projectile_reset()
        enemy_score += 1

    # Detecting collision between ball and user/enemy
    if projectile.colliderect(user) or projectile.colliderect(enemy):
        projectile_speed_x *= -1

def user_movement():
    # Restricting user movement to display size only.
    user.y += user_speed
    if user.top <= 0:
        user.top = 0
    if user.bottom >= display_height:
        user.bottom = display_height

def enemy_movement():
    # Making enemy move on y axis based on projectile position.
    if enemy.top < projectile.y:
        enemy.top += enemy_speed
    if enemy.bottom > projectile.y:
        enemy.bottom -= enemy_speed 

    # Restricting enemy movement to display size only.
    if enemy.top <= 0:
        enemy.top = 0
    if enemy.bottom >= display_height:
        enemy.bottom - display_height

def projectile_reset():
    global projectile_speed_x
    global projectile_speed_y
    # Resetting the projectile position.
    projectile.center = (display_width/2, display_height/2)

    # Launching projectile in random direction by multiplying x and y speed randomly.
    projectile_speed_x *= random.choice((1,-1))
    projectile_speed_y *= random.choice((1,-1))

# Start and game over screen.
def start():
    display1 = game_over_font1.render('WELCOME TO PONG PING!', False, projectile_color)
    display.blit(display1,(130,300))
    display2 = game_over_font2.render('Press any key to begin!', False, user_enemy_color)
    display.blit(display2, (130, 400))
    pygame.display.update()
    waiting = True
    while waiting:
        time.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def game_over():
    # Getting the current score and finding the highscore.
    global score_list
    highscore = 0
    highscore_check = False

    #Connecting to our database via MySQL connector
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "pongpingdb"
    )
    cursor = db.cursor()

    first_score = []
    first_score.append(max(score_list))

    # Checking if a previous highscore exists and saving it.
    cursor.execute("SELECT * FROM highscore")
    saved_score = cursor.fetchall()
    if len(saved_score) == 0 or first_score[0] > saved_score[0][0]:
        highscore = first_score[0]
        highscore_check = True
    else:
        highscore = saved_score[0][0]

    
        
    display1 = game_over_font1.render('GAME OVER', False, projectile_color)
    display.blit(display1, (400, 200))  

    # Shows your current score and your highscore.
    display2 = game_over_font2.render(f'SCORE: {first_score[0]} HIGHSCORE: {highscore}', False, user_enemy_color)
    display.blit(display2, (400, 300))

    # Checking if you've reached a new highscore and checking if there is a previous highscore.
    if highscore_check == True: 
        display3 = game_over_font2.render(f'NEW HIGH SCORE!', False, ('gold'))
        display.blit(display3, (400, 400))
        display4 = game_over_font2.render(f'PRESS SPACE TO RESTART', False, user_enemy_color)
        display.blit(display4, (400, 500))
    else:
        display4 = game_over_font2.render(f'PRESS SPACE TO RESTART', False, user_enemy_color)
        display.blit(display4,(400,400))
    
    pygame.display.flip()
    waiting = True
    # Handling input.
    while waiting:
        time.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                waiting = False 
# Function that saves rewrites your current highscore or makes a new one if there is none.
def highscore_sql():
    global score_list
    current_score = [] 
    current_score.append(max(score_list))
    #Connecting to the database.
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "pongpingdb"
    )

    cursor = db.cursor()
        
    cursor.execute("SELECT * FROM highscore")
    old_score = cursor.fetchall()
    # Checkig if a previous score exists.
    if len(old_score) == 0:
        sql = ("INSERT INTO highscore (score)"
               "VALUES(%s)"
              )
        cursor.execute(sql,current_score)
        db.commit()
        db.close()
    else:
        # Assigning the scores to int variables since you cant use lists and tuples with WHERE clauses in MySQL-connector.
        old_score_int = old_score[0][0]
        current_score_int = current_score[0]
        # Updating the highscore if your current score is bigger.
        if old_score and current_score_int > old_score_int:
            cursor.execute("""
                           UPDATE highscore
                           SET score=%s
                           WHERE score=%s
                           """,
                           (current_score_int,old_score_int)
                          )
            db.commit()
            db.close()
    score_list.clear()


pygame.init();
time = pygame.time.Clock()

# Setting up the main pygame display
display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pong Ping')

# Defining the shapes that will be used in the game 
projectile = pygame.Rect(display_width / 2 - 15, display_height/2 - 50, 30, 30) 
user = pygame.Rect(display_width - 20, display_height/ 2 - 70, 15, 150)
enemy = pygame.Rect(10, display_height / 2 - 70, 15, 150)

# Assigning colors used in the program to variables
background_color = pygame.Color('gray30')
user_enemy_color = pygame.Color('cornsilk1')
projectile_color = pygame.Color('firebrick3')
line = pygame.Color('gainsboro')

# Assigning variables to speed used by rectangles
user_speed = 0
enemy_speed = 9
# Assigning speed and a random x and y start direction    
projectile_speed_x = 10 * random.choice((1,-1))
projectile_speed_y = 10 * random.choice((1,-1))

# Assigning variables to use for fonts and score (These are the same for now but can be easily swapped out since they're already defined.)
start_font = pygame.font.Font('freesansbold.ttf', 32)
score_font = pygame.font.Font('freesansbold.ttf',32)
quit_font = pygame.font.Font('freesansbold.ttf',32)
game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

# Assigning variables to keep track of score
score_list = []
user_score = 0
enemy_score = 0
# Setting up booleans which we will use for states of the game to display a start and game over screen
running = True
game_done = True 
# The loop that runs the game itself.
while running:
    if game_done:
        display.fill('gray0')
        start() 
        game_done = False
        user_score = 0
        enemy_score = 0

    for event in pygame.event.get():
    # Handling input
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                user_speed += 9
            if event.key == pygame.K_DOWN:
                user_speed -= 9

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user_speed -= 9
            if event.key == pygame.K_DOWN:
                user_speed += 9
            if event.key == pygame.K_ESCAPE:
                game_done = True;
                score_list.append(user_score)
                display.fill('grey0')
                game_over()
                highscore_sql()

          
            

    # Using earlier defined movement 
    projectile_movement()
    user_movement()
    enemy_movement()
        
    # Drawing the shapes on the display using assigned variables
    display.fill(background_color)
    pygame.draw.rect(display,user_enemy_color,user)
    pygame.draw.rect(display,user_enemy_color,enemy)
    pygame.draw.aaline(display,line,(display_width/2,0),(display_width/2,display_height))
    pygame.draw.ellipse(display,projectile_color,projectile)

    # Drawing the defined fonts and using blit to put it on the main surface
    quit_text = quit_font.render('PRESS ESCAPE TO QUIT THE GAME.',False,user_enemy_color)
    display.blit(quit_text,(660,70))
    user_text = score_font.render(f'{user_score}',False,user_enemy_color)
    display.blit(user_text,(660,370))
    enemy_text = score_font.render(f'{enemy_score}',False,user_enemy_color)
    display.blit(enemy_text,(600,370))

    # Updating the display and setting the frames per second
    pygame.display.flip()
    time.tick(60)

        