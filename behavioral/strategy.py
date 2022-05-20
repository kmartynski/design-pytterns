from abc import ABC, abstractmethod


class Mission(ABC):

    @abstractmethod
    def prepare_flight(self):
        pass


class MartianMission(Mission):
    def prepare_flight(self):
        return "Astronaut is prepared for 54 mln km (7 months)"


class VenusianMission(Mission):
    def prepare_flight(self):
        return "Astronaut is prepared for 61 mln km (8 months)"


class JovianMission(Mission):
    def prepare_flight(self):
        return "Astronaut is prepared for 588 mln km (7 years)"


class MoonMission(Mission):
    def prepare_flight(self):
        return "Astronaut is prepared for 384 400 km (2 weeks)"


class MissionDispatcher:

    def __init__(self, astronaut_name, mission_strategy: Mission):
        self.astronaut_name = astronaut_name
        self.mission_strategy = mission_strategy

    def dispatch(self):
        return self.mission_strategy.prepare_flight()


if __name__ == "__main__":
    mission_1 = MissionDispatcher("Brand", mission_strategy=JovianMission())
    mission_2 = MissionDispatcher("Cooper", mission_strategy=MoonMission())
    mission_3 = MissionDispatcher("Tars", mission_strategy=MartianMission())
    mission_4 = MissionDispatcher("Hellman", mission_strategy=VenusianMission())

