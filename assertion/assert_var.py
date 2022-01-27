def assert_type(var, label, _type):
    assert isinstance(var, _type), '{} should be {} type'.format(label, _type)

def assert_iter(var, label, include_str=False):
    if not include_str:
        assert isinstance(var, str), '{} is not iterable'.format(label)
    else:
        assert hasattr(var, '__iter__'), '{} is not iterable'.format(label)

def assert_length(var, label, length, include_str=False, op='equal'):
    assert_iter(var, label, length, include_str)

    if op == 'eq':
        assert len(var) == length, 'The length of {} should be {}'.format(label, length)
    elif op == 'gt':
        assert len(var) > length, 'The length of {} should be greater than {}'.format(label, length)
    elif op == 'ge':
        assert len(var) >= length, 'The length of {} should be greater than or equal to {}'.format(label, length)
    elif op == 'lt':
        assert len(var) < length, 'The length of {} should be less than {}'.format(label, length)
    elif op == 'le':
        assert len(var) <= length, 'The length of {} should be less than or equal to {}'.format(label, length)
    elif op == 'nq':
        assert len(var) != length, 'The length of {} should not be {}'.format(label, length)
