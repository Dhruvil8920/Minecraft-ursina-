from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


block_pick = 1
app = Ursina()

grass_texture = load_texture('main2/grass_block.png')
stone_texture = load_texture('main2/stone_block.png')
brick_texture = load_texture('main2/brick_block.png')
dirt_texture = load_texture('main2/dirt_block.png')
diamond_texture = load_texture('main2/diamond.png')
sky_texture = load_texture('main2/skybox.png')
arm_texture = load_texture('main2/arm_texture.png')


def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['left shift']:
        player.speed = 10
    else:
        player.speed = 5

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='main2/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
       )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4:
                    voxel= Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5:
                    voxel = Voxel(position=self.position + mouse.normal, texture=diamond_texture)

            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=200,
            double_sided=True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='main2/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.5, -0.7)
        )

    def active(self):
        self.position = Vec2(0.4, -0.58)

    def passive(self):
        self.position = Vec2(0.5, -0.6)


for z in range(40):
    for x in range(40):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()


app.run()