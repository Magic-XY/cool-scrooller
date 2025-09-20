scene.onOverlapTile(SpriteKind.Player, assets.tile`tile1`, function (sprite2, location2) {
	
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.greenOuterEast0, function (sprite, location) {
    mySprite.setPosition(10, 84)
    tiles.setCurrentTilemap(tilemap`level2`)
    mySprite.vx = 100
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -200
    }
})
let mySprite: Sprite = null
scene.setBackgroundColor(8)
tiles.setTilemap(tilemap`level`)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.ay = 400
mySprite.vx = 100
scene.cameraFollowSprite(mySprite)
