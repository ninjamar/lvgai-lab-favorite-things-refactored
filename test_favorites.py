import json
import pytest
from main import *

def test_save_favorites(tmp_path):
    favorites = {"food": "pizza"}
    file = tmp_path / "test.json"
    save_favorites(favorites, filename=str(file))
    with open(file) as f:
        data = json.load(f)
    assert data == favorites

def test_display_favorites(capsys):
    favorites = {"food": "pizza", "color": "blue"}
    display_favorites(favorites)
    captured = capsys.readouterr()

    assert "food" in captured.out
    assert "color" in captured.out

def test_lookup_favorite_found(monkeypatch, capsys):
    favorites = {"food": "pizza"}
    monkeypatch.setattr('builtins.input', lambda _: "food")
    lookup_favorite(favorites)
    captured = capsys.readouterr()
    assert "pizza" in captured.out

def test_lookup_favorite_not_found(monkeypatch, capsys):
    favorites = {"food": "pizza"}
    monkeypatch.setattr('builtins.input', lambda _: "drink")
    lookup_favorite(favorites)
    captured = capsys.readouterr()
    assert "not available" in captured.out

def test_add_favorite(monkeypatch):
    favorites = {}

    # The lambda is called everytime input() is called.
    # So, use iter and next to make this work

    inputs = iter(["music", "rock"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_favorite(favorites)
    assert favorites["music"] == "rock"

def test_update_favorite(monkeypatch, capsys):
    favorites = {"movie": "Cars"}
    inputs = iter(["movie", "Cars"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    update_favorite(favorites)
    assert favorites["movie"] == "Cars"

def test_update_favorite_not_found(monkeypatch, capsys):
    favorites = {}
    inputs = iter(["book"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    update_favorite(favorites)
    captured = capsys.readouterr()
    assert "not found" in captured.out

def test_delete_favorite(monkeypatch):
    favorites = {"game": "soccer"}
    monkeypatch.setattr('builtins.input', lambda _: "game")
    delete_favorite(favorites)
    assert "game" not in favorites

def test_delete_favorite_not_found(monkeypatch, capsys):
    favorites = {"game": "soccer"}
    monkeypatch.setattr('builtins.input', lambda _: "sport")
    delete_favorite(favorites)
    captured = capsys.readouterr()
    assert "not found" in captured.out
