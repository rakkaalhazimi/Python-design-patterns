class ElectricalOutlet:
    def __init__(self, power_plant):
        self.power_plant = power_plant

    def is_active(self):
        return self.power_plant.active


class Toaster:
    active = False

    def plug(self, outlet):
        if outlet.is_active():
            self.active = True
        
        print(f"Toaster is {'on' if self.active else 'off'}")


class SteamPowerPlants:
    def __init__(self, active):
        self.active = active



if __name__ == "__main__":
    power_plant = SteamPowerPlants(active=False)  # change active with True or False
    outlet = ElectricalOutlet(power_plant=power_plant)
    toaster = Toaster()
    toaster.plug(outlet)
