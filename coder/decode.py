def decode_json(_str):
    import json

    return json.loads(_str)

def decode_letter_string(_list, code_list, tostring=False):
    if tostring:
        opt = str()
        for i in _list:
            opt += code_list[i]
    else:
        opt = list()
        for i in _list:
            opt.append(code_list[i])

    return opt
