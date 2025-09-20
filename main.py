def on_overlap_tile(sprite, location):
    mySprite.set_position(10, 84)
    tiles.set_current_tilemap(tilemap("""
        level2
        """))
    mySprite.vx = 100
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_outer_east0,
    on_overlap_tile)

def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    pass
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile1
        """),
    on_overlap_tile2)

mySprite: Sprite = None
scene.set_background_color(8)
tiles.set_tilemap(tilemap("""
    level
    """))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . 3 3 3 3 3 3 3 3 . . . .
        . . . 3 d 3 3 3 3 3 3 c 3 . . .
        . . 3 c d 3 3 3 3 3 3 c c 3 . .
        . 3 c c d d d d d d 3 c c d 3 d
        . 3 c 3 a a a a a a a b c d 3 3
        . 3 3 a b b a b b b a a b d 3 3
        . 3 a b b b a b b b b a 3 3 3 3
        . a a 3 3 3 a 3 3 3 3 3 a 3 3 3
        . a a a a a a f a a a f a 3 d d
        . a a a a a a f a a f a a a 3 d
        . a a a a a a f f f a a a a a a
        . a f f f f a a a a f f f a a a
        . . f f f f f a a f f f f f a .
        . . . f f f . . . . f f f f . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
mySprite.ay = 400
mySprite.vx = 100
scene.camera_follow_sprite(mySprite)