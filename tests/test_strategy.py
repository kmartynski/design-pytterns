from pytest import mark

from behavioral.strategy import (
    JovianMission,
    MartianMission,
    MissionDispatcher,
    MoonMission,
    VenusianMission,
)


class TestStrategy:

    @mark.parametrize(
        "mission, information",
        [
            (MartianMission(), "Astronaut is prepared for 54 mln km (7 months)"),
            (VenusianMission(), "Astronaut is prepared for 61 mln km (8 months)"),
            (JovianMission(), "Astronaut is prepared for 588 mln km (7 years)"),
            (MoonMission(), "Astronaut is prepared for 384 400 km (2 weeks)")
        ]
    )
    def test_should_return_message_related_to_mission(self, mission, information):
        strategy = MissionDispatcher("Brand", mission_strategy=mission)
        assert strategy.dispatch() == information

    @mark.parametrize(
        "astronaut_name",
        [
            "Brand", "Cooper", "Tars", "Hellman"
        ]
    )
    def test_should_return_correct_name(self, astronaut_name):
        mission_1 = MissionDispatcher(astronaut_name, mission_strategy=JovianMission())
        assert mission_1.astronaut_name == astronaut_name
