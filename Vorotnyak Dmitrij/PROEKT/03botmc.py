from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')

random_number = id([]) % 1000 # Give us a random number upto 1000
BOT_USERNAME = f'programmist_{random_number}'

bot = mineflayer.createBot({ 'host': 'pythoneatkids.aternos.me', 'port': 63517, 'username': BOT_USERNAME, 'hideErrors': True })

@On(bot, 'playerJoin')
def end(this, player):
  bot.chat('Someone joined!')
@On(bot, 'chat')
def onChat(this, user, message, *rest):
  print(f'{user} said "{message}"')

  # If the message contains stop, remove the event listener and stop logging.
  if 'stop' in message:
    off(bot, 'chat', onChat)

@On(bot, 'chat') #jjjj
def breakListener(this, sender, message, *args):
  if sender and (sender != BOT_USERNAME):
    if 'break' in message:
      pos = bot.entity.position.offset(0, -1, 0)
      blockUnder = bot.blockAt(pos)
      if bot.canDigBlock(blockUnder):
        bot.chat(f"I'm breaking the '{blockUnder.name}' block underneath")
        # The start=True parameter means to immediately invoke the function underneath
        # If left blank, you can start it with the `start()` function later on.
        try:
          @AsyncTask(start=True)
          def break_block(task):
            bot.dig(blockUnder)
          bot.chat('I started digging!')
        except Exception as e:
          bot.chat(f"I had an error {e}")
      else:
        bot.chat(f"I can't break the '{blockUnder.name}' block underneath")
    if 'stop' in message:
      off(bot, 'chat', breakListener)
