from count_items import counter


def test_items_count():
    expected_result = {
        'apple': 2,
        'banana': 1,
        'kiwi': 1
    }
    assert counter(['apple', 'banana', 'apple', 'kiwi']) == expected_result

def test_2_items_count():
    expected_result = {
        'apple': 2,
        'banana': 1,
        'kiwi': 2
    }
    assert counter(['apple', 'banana', 'apple', 'kiwi', 'KIWI']) == expected_result