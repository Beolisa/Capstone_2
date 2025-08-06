# Generators spawn enemies over time.
# Skeletons are afraid of lightstones.

player = game.spawnPlayerXY("champion", 15, 35)
player.attackDamage = 60
player.maxSpeed = 8

game.addSurviveGoal()
game.addDefeatGoal()
game.spawnXY("x-mark-stone", 60, 35)
# Spawn a "generator"

# Spawn a "lightstone"

# Now beat your game!