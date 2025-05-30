from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    position: str
    holiday_entitlement: int = 25

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."
@dataclass
class Manager(Employee):
    car: str = ""
frantisek = Manager("František Novák", "konstruktér", 25, "Škoda Octavia")
print(frantisek.car)