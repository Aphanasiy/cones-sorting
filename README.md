## Переливашка

На сегодняшний день в этих ваших app-сторах развирусилась игра, в которой у тебя есть колбочки и шарики/слои жидкости. Задача же игрока переливанием этих субстанций добиться того, чтобы во всех колбах было только по одному цвету. При этом доливать слой сверху ты можешь только в пустую колбу или на тот цвет, который уже сверху в этой колбе.

И естественно эти подделки теперь суют в рекламе всех приложений. Я купился на парочку таких и прошёл несколько сотен уровней. А потом начал задумываться...

У подделок есть две общие черты
  - В колбе всегда помещается 4 единицы какой-то субстанции
  - На каждом уровне всегда две свободные колбы.

И вот мой мозг поставил мне задачку - правда ли, что мне всегда хватит двух колб для того, чтобы закончить игру, насколько велико дерево ситуаций и как найти решение.

В этом репозитории находится небольшой скрипт, который позволит вам поиграть в эту игру на Linux прямо из консоли. Странные сочетания цветов вам помогут лучше ориентироваться в игре.

Пока что на этом всё. Если меня посетит вдохновение ещё раз, я попробую закончить свои исследования, а сейчас - это чилловая игрушка для вашего кудахтера. Welcome!

Для того, чтобы запустить уровень, запустите `./main.py {level_num}`. Выбрать можно любой уровень из уже существующих на текущий момент. Все уровни можно пройти.
На каждом шаге вы должны написать два числа - из какой и в какую колбу перелить субстанцию.

Если уровни закончились, вы можете запустить `./level_generator.py` и он сам добавит в папку `levels` следующий уровень с таким количеством колбочек, которое вы пропишете в программе, после чего вы сможете продолжить играть.

Если вы нашли какой-то стоящий уровень, то вы можете добавить его в официальный level-set через issues. При этом вы должны будете предоставить последовательность, при которой уровень решается. Без неё уровень не будет аппрувнут.

По всем вопросам обращайтесь ко мне в телеграм: [@Aphanasiy](https://t.me/Aphanasiy "Телеграм автора репозитория")