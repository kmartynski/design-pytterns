from behavioral.state import Context, InitialState, FinalState


class TestState:

    def test_context_returns_states_for_initial(self):
        initial = InitialState()
        final = FinalState()
        context = Context(initial)
        context.request_1()
        assert initial._list_of_changes
        assert not final._list_of_changes

    def test_context_returns_states_for_final(self):
        final = FinalState()
        context = Context(final)
        context.request_1()
        assert final._list_of_changes