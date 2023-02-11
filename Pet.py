class Pet:
    name = "Pet"
    color = "Pet"
    Happy = 0
    Angry = 0
    def __init__(self,nm,cl,Hp,Ag):
        self.name = nm
        self.color = cl
        self.Happy = Hp
        self.Angry = Ag
    
    def show_status(self):
        show = f"Name --> {self.name}\nColor --> {self.color}\nHappy --> {self.Happy}\nAngry --> {self.Angry}"
        print(show)
    
    def Go(self):
        self.Happy += 10
        print(f"You walking the {self.name}\n +10 Happy")
    
    def Kick(self):
        self.Happy -= 5
        self.Angry += 10
        print(f"You can kicking the pet :(\n-5 happy\n+10 angry")
        if self.Angry == 20:
            print(f"Arrrr\nYour pet kill you you death")

blacky = Pet(nm="Blacky",cl="Black",Hp=0,Ag=0)
blacky.show_status()
blacky.Go()
blacky.show_status()
blacky.Kick()
blacky.Kick()
blacky.show_status()
