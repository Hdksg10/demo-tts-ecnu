import tts
DrugDatabase = {
    "6911322033949":'聚维酮碘溶液',
    "6900233783173":'百令胶囊'
}
while True:
    name = input()
    try:
        tts.say(DrugDatabase[name])
    except KeyError:
        tts.say("药品尚未录入")