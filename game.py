from main import *

enamy = Enemy(n = "Eminem",h=50,d=10,a=1)
yura = Hero(n="Yura",h=70,d=15,a=3)

yura.atack_enemy(enamy)
enamy.atack_hero(yura)

enamy.show_stats()
yura.show_stats()