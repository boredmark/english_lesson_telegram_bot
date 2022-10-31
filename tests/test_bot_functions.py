import pytest
from bot import Bot
import sentences


def test_create_string_of_sentences():
    expected_result = 'The Consul watched as Kassad raised the death wand.\n-------------\n'
    expected_result_2 = 'No matched sentences'
    assert Bot.create_string_of_sentences('watched', 1) == expected_result
    assert Bot.create_string_of_sentences('bob', 1) == expected_result_2



