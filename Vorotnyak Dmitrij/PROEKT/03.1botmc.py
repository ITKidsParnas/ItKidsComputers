from javascript import require, On

mineflayer = require('mineflayer')
pathfinger = require('mineflayer-pathfinder')
GoalFollow = pathfinger.goals.GoalFollow

bot = mineflayer.createBot({
    'host':'pythoneatkids.aternos.me',
    'username':'IAMNOTBOT',
    'version':'1.16.5'
})

bot.loadPlugin(pathfinger.pathfinger)

@On(bot,'spawn')
def spawn(*args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinger.Movements(bot, mcData)

    @On(bot, 'chat')
    def msgHandler(this, user, message, *args):
        if user != 'IAMNOTBOT':
            if 'сюда'in message:
                player = bot.players[user]
                target = player.entity

                bot.pathfinger.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinger.setGoal(goal, True)
    