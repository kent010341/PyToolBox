def encode_json(_dict):
    import json

    return json.dumps(_dict)

def encode_letter_string(_str, code_list, tostring=False):
    code_dict = dict()
    opt = list()

    for i, element in enumerate(code_list):
        code_dict[element] = i

    if tostring:
        opt = str()
        for letter in _str:
            opt += code_dict[letter]
    else:
        opt = list()
        for letter in _str:
            opt.append(code_dict[letter])

    return opt
