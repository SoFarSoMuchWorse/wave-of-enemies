@namespace
class SpriteKind:
    Special_Projectile = SpriteKind.create()

def on_b_pressed():
    global mySpecial, SpecialCooldown
    if SpecialCooldown == 0:
        mySpecial = sprites.create(img("""
                2 2 2 2 3 3 1 1
                2 2 2 2 2 3 3 1
                2 2 2 2 2 2 3 3
                2 2 2 2 2 2 2 3
                2 2 2 2 2 2 2 2
                a 2 2 2 2 2 2 2
                a a 2 2 2 2 2 2
                a a a 2 2 2 2 2
                """),
            SpriteKind.Special_Projectile)
        mySpecial.set_position(mySprite.x, mySprite.y)
        mySpecial.set_velocity(200, 0)
        SpecialCooldown = 20
    else:
        mySprite.say_text("On cooldown!")
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global myProjectile
    myProjectile = sprites.create(img("""
            4 5 5 . . . . .
            4 5 5 5 5 . . .
            4 5 5 5 1 1 5 .
            4 5 5 5 5 5 1 5
            4 5 5 5 5 5 5 4
            4 5 5 5 5 4 4 .
            4 5 5 4 4 . . .
            4 4 4 . . . . .
            """),
        SpriteKind.projectile)
    myProjectile.x = mySprite.x
    myProjectile.y = mySprite.y
    myProjectile.vx = 200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    info.change_score_by(1)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
sprites.on_overlap(SpriteKind.Special_Projectile,
    SpriteKind.enemy,
    on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(sprite2)
    sprites.destroy(otherSprite2)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    sprites.destroy(otherSprite3)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
HugeWave = 0
myProjectile: Sprite = None
mySpecial: Sprite = None
SpecialCooldown = 0
mySprite: Sprite = None
info.set_life(3)
mySprite = sprites.create(img("""
        ........................
        ..ffffffff..............
        fff555555fff............
        f4555555555f............
        f4555555f55f............
        f45555555f5f............
        f45555555f5f............
        f4555555555fffffffffff..
        ff44444444fffcccccccff..
        .ffffffffff.fcffffffff..
        ..ff6999fffffcf.........
        .f6f6999f95ffff.........
        .f5f6666fff.............
        .ffffffff...............
        ...f8ff8f...............
        ...ffffff...............
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 50, 50)
info.set_score(0)

def on_update_interval():
    global SpecialCooldown
    if SpecialCooldown > 0:
        SpecialCooldown += -1
game.on_update_interval(1000, on_update_interval)

def on_forever():
    global HugeWave
    HugeWave = 0
    pause(30000)
    HugeWave = 1
    pause(30000)
forever(on_forever)

def on_forever2():
    global myEnemy
    pause(randint(1, 2500 - HugeWave * 2000))
    myEnemy = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . f f f f f f . .
            . . . . . . . f 6 6 6 6 6 7 f .
            . . . . . . . f f 6 6 f 6 7 f .
            . . . . . . . f 6 6 6 6 6 7 f .
            . . f f f f f f 2 2 2 2 6 7 f .
            . . f 6 6 6 6 7 f f f f f f . .
            . . f f f f f f f c c c a f . .
            . . . f 6 6 6 7 f c c c a f . .
            . . . f f f f f f f c a f . . .
            . . . . . . . . . f c a f . . .
            . . . . . . . . f c c c a f . .
            . . . . . . . . f f f f f f . .
            . . . . . . . . . f 6 f 6 f . .
            . . . . . . . . . f 7 f 7 f . .
            . . . . . . . . . f f f f f . .
            """),
        SpriteKind.enemy)
    myEnemy.set_position(160,
        (max(mySprite.y + randint(-100, 100), 0) + min(mySprite.y + randint(-100, 100), 120)) / 2)
    myEnemy.vx = -50
forever(on_forever2)
