from structural.bridge import RadioOne, RadioTwo, Emitter


class TestBridge:
    radio = RadioOne()
    radio_2 = RadioTwo()

    def test_should_return_proper_message_from_radio_1(self):
        emitter = Emitter(self.radio, "Message sent!", 52)
        assert emitter.operation() == "Message from RadioOne: Message sent! on 52 MHz"

    def test_should_return_proper_message_from_radio_2(self):
        emitter = Emitter(self.radio_2, "Transmission sent!", 32)
        assert emitter.operation() == "Transmission from RadioTwo: Transmission sent! on 32 MHz"
