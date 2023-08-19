import json

def write():
    data = {}
    data['questions'] = []
    data['questions'].append({
        'id': 1,
        'question': 'Что закрыто на картинке?',
        'answer': ['а'],
        'type': 'close'})
    data['questions'].append({
        'id': 2,
        'question': 'Что закрыто на картинке?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 3,
        'question': 'Что закрыто на картинке?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 4,
        'question': 'Что закрыто на картинке?',
        'answer': ['г'],
        'type': 'close'})
    data['questions'].append({
        'id': 5,
        'question': 'Что закрыто на картинке?',
        'answer': ['в'],
        'type': 'close'})
    data['questions'].append({
        'id': 6,
        'question': 'Какая картинка верна?',
        'answer': ['правый', 'правая', 'справа'],
        'type': 'open'})
    data['questions'].append({
        'id': 7,
        'question': 'Какая картинка верна?',
        'answer': ['левый', 'левая', 'слева'],
        'type': 'open'})
    data['questions'].append({
        'id': 8,
        'question': 'Какая картинка верна?',
        'answer': ['левый', 'левая', 'слева'],
        'type': 'open'})
    data['questions'].append({
        'id': 9,
        'question': 'Какая картинка верна?',
        'answer': ['левый', 'левая', 'слева'],
        'type': 'open'})
    data['questions'].append({
        'id': 10,
        'question': 'Какая картинка верна?',
        'answer': ['левый', 'левая', 'слева'],
        'type': 'open'})
    data['questions'].append({
        'id': 11,
        'question': 'Какой вид спорта скрывается в ребусе?',
        'answer': ['баскетбол'],
        'type': 'open'})
    data['questions'].append({
        'id': 12,
        'question': 'Какой вид спорта скрывается в ребусе?',
        'answer': ['волейбол'],
        'type': 'open'})
    data['questions'].append({
        'id': 13,
        'question': 'Какой вид спорта скрывается в ребусе?',
        'answer': ['кёрлинг', 'керлинг'],
        'type': 'open'})
    data['questions'].append({
        'id': 14,
        'question': 'Какой вид спорта скрывается в ребусе?',
        'answer': ['шахматы'],
        'type': 'open'})
    data['questions'].append({
        'id': 15,
        'question': 'Какой вид спорта скрывается в ребусе?',
        'answer': ['водное поло'],
        'type': 'open'})
    data['questions'].append({
        'id': 16,
        'question': 'Кого мы соединили на картинке?',
        'answer': ['евгения загитова', 'женя загитова', 'загитова евгения', 'загитова женя'],
        'type': 'open'})
    data['questions'].append({
        'id': 17,
        'question': 'Кого мы соединили на картинке?',
        'answer': ['илья овечкин', 'овечкин илья'],
        'type': 'open'})
    data['questions'].append({
        'id': 18,
        'question': 'Кого мы соединили на картинке?',
        'answer': ['елена трусова', 'трусова елена', 'лена трусова', 'трусова лена'],
        'type': 'open'})
    data['questions'].append({
        'id': 19,
        'question': 'Кого мы соединили на картинке?',
        'answer': ['илья шарипов', 'шарипов илья'],
        'type': 'open'})
    data['questions'].append({
        'id': 20,
        'question': 'Кого мы соединили на картинке?',
        'answer': ['полина аверина', 'аверина полина', 'поля аверина', 'аверина поля'],
        'type': 'open'})
    data['questions'].append({
        'id': 21,
        'question': 'Как продолжается фраза?',
        'answer': ['а'],
        'type': 'close'})
    data['questions'].append({
        'id': 22,
        'question': 'Как продолжается фраза?',
        'answer': ['в'],
        'type': 'close'})
    data['questions'].append({
        'id': 23,
        'question': 'Как продолжается фраза?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 24,
        'question': 'Как продолжается фраза?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 25,
        'question': 'Как продолжается фраза?',
        'answer': ['г'],
        'type': 'close'})
    data['questions'].append({
        'id': 26,
        'question': 'Как продолжается фраза?',
        'answer': ['в'],
        'type': 'close'})
    data['questions'].append({
        'id': 27,
        'question': 'Как продолжается фраза?',
        'answer': ['а'],
        'type': 'close'})
    data['questions'].append({
        'id': 28,
        'question': 'Как продолжается фраза?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 29,
        'question': 'Как продолжается фраза?',
        'answer': ['г'],
        'type': 'close'})
    data['questions'].append({
        'id': 30,
        'question': 'Как продолжается фраза?',
        'answer': ['б'],
        'type': 'close'})
    data['questions'].append({
        'id': 31,
        'question': 'Какой слон бывает без хобота?',
        'answer': ['шахматный', 'шахматный слон', 'слон из шахмат'],
        'type': 'open'})
    data['questions'].append({
        'id': 32,
        'question': 'Сколько кошек можно поместить в пустую коробку объемом три литра? ',
        'answer': ['1', 'одну', 'одна', 'одну кошку', '1 кошку', 'одна кошка'],
        'type': 'open'})
    data['questions'].append({
        'id': 33,
        'question': 'Пожирает всё кругом:\nЗверя, птицу, лес и дом.\n'+\
        'Сталь сгрызёт, железо сгложет,\nКрепкий камень уничтожит,\n'+\
        'Власть его всего сильней,\nДаже власти королей.',
        'answer': ['время'],
        'type': 'open'})
    data['questions'].append({
        'id': 34,
        'question': 'Музыкант, певец, рассказчик – а всего труба и ящик.',
        'answer': ['грамофон'],
        'type': 'open'})
    data['questions'].append({
        'id': 35,
        'question': 'Как написать слово мышеловка пятью буквами?',
        'answer': ['кошка'],
        'type': 'open'})
    data['questions'].append({
        'id': 36,
        'question': 'Что в огне не горит, а в воде не тонет?',
        'answer': ['лёд', 'лед', 'льдина'],
        'type': 'open'})
    data['questions'].append({
        'id': 37,
        'question': 'Что с земли и ребенок поднимет, но через забор и силач не перекинет?',
        'answer': ['перо', 'перышко', 'пёрышко'],
        'type': 'open'})
    data['questions'].append({
        'id': 38,
        'question': 'Маленький, серенький, на слона похож.',
        'answer': ['слоненок', 'слонёнок'],
        'type': 'open'})
    data['questions'].append({
        'id': 39,
        'question': 'В каком веке ходили греки назад пятками?',
        'answer': ['всегда', 'в любом', 'в любых', 'во всех', 'в любом веке', 'в любых веках', 'во всех веках'],
        'type': 'open'})
    data['questions'].append({
        'id': 40,
        'question': 'Чем больше от нее берешь, тем больше ее становиться?',
        'answer': ['яма', 'ямка'],
        'type': 'open'})
    data['questions'].append({
        'id': 41,
        'question': 'Что было раньше: курица или яйцо?',
        'answer': ['яйцо'],
        'type': 'open'})
    data['questions'].append({
        'id': 42,
        'question': 'Зебра белая в черную полоску или черная в белую?',
        'answer': ['черная в белую полоску', 'чёрная в белую полоску', 'черная', 'чёрная'],
        'type': 'open'})
    data['questions'].append({
        'id': 43,
        'question': 'Кит и кашалот это одно и то же?',
        'answer': ['нет', 'разное'],
        'type': 'open'})
    data['questions'].append({
        'id': 44,
        'question': 'Ель и елка одно и то же?',
        'answer': ['да', 'одно', 'одно и то же'],
        'type': 'open'})
    data['questions'].append({
        'id': 45,
        'question': 'А и Б сидели на трубе. А уехал за границу, Б чихнул и лёг в больницу.\nЧто осталось на трубе?',
        'answer': ['б', 'буква б'],
        'type': 'open'})
    data['questions'].append({
        'id': 46,
        'question': 'Что люди не могут делать во сне?',
        'answer': ['чихать', 'чихнуть'],
        'type': 'open'})
    data['questions'].append({
        'id': 47,
        'question': 'Только на четверть пустыня сахара состоит из …',
        'answer': ['песка', 'песок'],
        'type': 'open'})
    data['questions'].append({
        'id': 48,
        'question': 'Кто может глотать и дышать одновременно?',
        'answer': ['младенец', 'младенцы', 'ребенок до года', 'ребёнок до года', 'дети до года'],
        'type': 'open'})
    data['questions'].append({
        'id': 49,
        'question': 'Какой закат на марсе?',
        'answer': ['синий', 'синего цвета'],
        'type': 'open'})
    data['questions'].append({
        'id': 50,
        'question': 'Самая большая пустыня находиться где?',
        'answer': ['антарктида', 'в антарктиде', 'на материке антарктида'],
        'type': 'open'})
    
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)#, ensure_ascii=False)

def save_team_list(teams):
    with open('teams.txt', 'w') as outfile:
        json.dump(teams, outfile)

def load_team_list():
    try:
        with open('teams.txt') as json_file:
            return json.load(json_file) 
    except:
        return 0


def read():
    with open('data.txt') as json_file:
        return json.load(json_file)