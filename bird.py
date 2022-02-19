class Bird():
    def __init__(self, energy, max_speed) -> None:
        self.energy = energy
        self.max_speed = max_speed

    def get_max_speed(self):
        #Показывает максимальную скорость птицы
        print(f"Максимальная скорость птицы {self.max_speed} км/ч") 

    def show_energy(self):
        #Показывает сколько энергий у птицы
        print(f"У птицы {self.energy} энергий")
    
    def bird_fly(self):
        #Птица взлетает
        print('Flapping wings')
    
    def bird_land(self):
        #Птица приземляется
        print('Landing')
    
    def energy_wasting(self):
        #Трата энергий у птицы
        self.energy -= 2

