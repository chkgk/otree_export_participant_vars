from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from random import randint

author = 'Christian König gen. Kersting'

doc = """
Demo app to show custom export of participant vars in oTree 2.6 (beta).
"""


class Constants(BaseConstants):
    name_in_url = 'part_vars_export'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # assign everyone a random number and store it in a participant var.
        for player in self.get_players():
            player.participant.vars['first_participant_var'] = randint(0, 100)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def custom_export(players):
    # header row
    yield ['session', 'participant_code', 'round_number', 'id_in_group', 'first_participant_var']
    for p in players:
        yield [p.session.code, p.participant.code, p.round_number, p.id_in_group, p.participant.vars.get('first_participant_var', None)]