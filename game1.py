import pgzrun 
#add bgm music
music.play('bg')
music.play('bg')
b=Rect((50,50),(100,50))
#b=Actor('img1',(300,300))
vx,vy=3,5 #global variale
def draw():
    screen.fill('red ')
    screen.draw.filled_rect(b,"yellow")
def update():
    global vx,vy
    b.x+=vx
    b.y+=vy
    if b.right>800 or b.left<0:
        vx=-vx
    if b.bottom>600 or b.top<0:
        vy=-vy

#outside of all function
pgzrun.go()

