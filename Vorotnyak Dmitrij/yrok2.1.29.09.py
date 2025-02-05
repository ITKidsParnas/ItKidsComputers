text = input('На улице идет дождь?')
if text == 'ДА' or text == 'да' or text == "da" or text == "Да" or text == 'yes':
    print('не выходи на удицу')
elif text == "нет" or text == 'Нет' or text == 'НЕТ' or text == 'no' or text == 'net':
    print('виходи на удицу')


text2 = input('На улице идет снег?') 
if text2 == 'ДА' or text == 'да' or text == "da" or text == "Да" or text == 'yes':
    print('иди играть в снежки')
elif text2 == "нет" or text == 'Нет' or text == 'НЕТ' or text == 'no' or text == 'net':
    print('жди')
else:
    print('не понял (да или нет)')

