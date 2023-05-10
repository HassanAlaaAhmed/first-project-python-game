from ursina import *
app=Ursina()

camera.orthographic='true'
camera.fov =10
car= Entity(
	model='quad',
	texture='assets1/car',
	collider='box',
	scale=(2,1),
	rotation_z=90
	)

road1 = Entity(
model='quad',
texture='assets1/road',
scale=15,
z=1
	)
road2=duplicate(road1,y=15)
pair =[road1, road2]

enemies = []
import random
def newenemy():
 val = random.uniform(-2,2)
 new = duplicate(
	car,
	texture='assets1/enemy',
	x= 2*val,
	y= 25,
	color=color.random_color(),
	rotation_z=
	90 if val <0
		else -90
    )
 enemies.append(new)
 invoke(newenemy, delay=0.5)
newenemy()

def update():
car.x -=held_keys['a']*5*time.dt
car.x +=held_keys['d']*5*time.dt
for road in pair:
raod.y += time.dt*6
if road.y < -15:
road.y +=30
for enemy in enemies:
if enemy.x <0:
enemy.y -= time.dt*10
else:
enemy.y -=  time.dt*5
if enemy.y < -10:
enemies.remove(enemy)
destroy(enemy)
if car.intersects().hit:
car.shake()

app.run()