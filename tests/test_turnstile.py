import pytest
import turnstile_kata as tk

def test_turnstile_exist():
    assert False == tk.Turnstile().state

def test_turnstile_push():
    assert False == tk.Turnstile().cross()

def test_inserting_coin_lets_me_through():
    turnstile = tk.Turnstile()
    assert False == turnstile.cross()
    turnstile.insert_coin()
    assert True == turnstile.cross()

def test_insert_coin_lets_me_through_once():
    turnstile = tk.Turnstile()
    assert False == turnstile.cross()
    turnstile.insert_coin()
    assert True == turnstile.cross()
    assert False == turnstile.cross()
