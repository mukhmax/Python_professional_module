import pytest
from main import Stack

test_data = [
    ('{((((([])))))}[]', True),
    ('({{{}}}((()))[[[]]])', True),
    ('((){}[]))', False),
    ('({[({[([{}])]})]})', True),
    ('((()){{{]]', False)
]
test_obj = Stack()


@pytest.mark.parametrize('brackets_set, result', test_data)
def test_check(brackets_set, result):
    check_result = test_obj.check(brackets_set)
    assert check_result == result
