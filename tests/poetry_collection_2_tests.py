import pytest
from poetry_collection_2 import PoetryCollection2


def example_poem_data():
    test_list = []
    test_list.append({"title": "poem1", "author": "author1", "lines": ["line1", "line2"]})
    test_list.append({"title": "poem2", "author": "author1", "lines": ["line1", "line2", "line3"]})
    test_list.append({"title": "poem3", "author": "author2", "lines": ["line1", "line2"]})
    test_list.append({"title": "poem4", "author": "author3", "lines": []})
    test_list.append({"title": "poem5", "author": "author2", "lines": ["line1 is a really long line comparatively", "line2 is also a bit long"]})
    test_list.append({"title": "poem6", "author": "author3", "lines": ["many", "short", "lines", "here"]})
    test_list.append({"title": "poem7", "author": "author2", "lines": ["line1", "line2"]})
    return test_list


def test_creating_collection():
    my_poetry_collection = PoetryCollection2("My Test Poems", example_poem_data())
    print(my_poetry_collection)


def test_poem_count_for_author():
    my_poetry_collection = PoetryCollection2("My Test Poems", example_poem_data())
    assert my_poetry_collection.count_poems_for_author("author1") == 1
    assert my_poetry_collection.count_poems_for_author("author2") == 3
    assert my_poetry_collection.count_poems_for_author("author3") == 2


def test_most_poems():
    my_poetry_collection = PoetryCollection2("My Test Poems", example_poem_data())
    assert my_poetry_collection.find_author_with_most_poems() == "author2"


def test_find_longest_poem():
    my_poetry_collection = PoetryCollection2("My Test Poems", example_poem_data())
    longest_poem = my_poetry_collection.find_longest_poem()
    assert longest_poem.title == "poem5"
    assert longest_poem.author == "author2"
