def dumps(obj:object):
    return pack(obj)

def dump(obj:object, fp=""):
    tokens = pack(obj)
    fp.write(tokens)

def loads(string:str):
    return decode(string)

def load(fp=""):
    buffer = fp.read()
    return decode(buffer)

def pack(obj:object):
    tokens = []
    if(isinstance(obj, dict)):
        tokens.append('{')
        tmp = {}
        while(obj.keys()):
            key, value = obj.popitem()
            tmp[key] = value
        obj = tmp
        while(obj.keys()):
            key, value = obj.popitem()
            if not isinstance(key, str):
                raise KeyError('Key must be a string')
            else:
                tokens.append(pack(key))
                tokens.append(': ')
                tokens.append(pack(value))
                if(obj.keys()):
                    tokens.append(', ')
        tokens.append('}')
    if(isinstance(obj, list)):
        tokens.append('[')
        obj.reverse()
        while(obj):
            value = obj.pop()
            tokens.append(pack(value))
            if(obj):
                tokens.append(', ')
        tokens.append(']')
    if(isinstance(obj, tuple) or isinstance(obj,set)):
        obj2 = [i for i in obj]
        tokens.append('[')
        obj2.reverse()
        while(obj2):
            value = obj2.pop()
            tokens.append(pack(value))
            if(obj2):
                tokens.append(', ')
        tokens.append(']')
    if((isinstance(obj, int) or isinstance(obj, float)) and not isinstance(obj, bool)):
        tokens.append(obj)
    if(obj in (True, False, None)):
        if obj is True:
            tokens.append('true')
        if obj is False:
            tokens.append('false')
        if obj is None:
            tokens.append('null')
    if(isinstance(obj, str)):
        tokens.append('"')
        tokens.append(obj)
        tokens.append('"')
    return ''.join(str(token) for token in tokens)


def decode(string:str):
    return unpack(string)[0]

def unpack(string : str):
    ptr = 0
    while ptr < len(string):
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1
            continue
        if string[ptr] == '{':
            ptr += 1
            result = unpack_dict(string[ptr : ])
            ptr += result[1]
            return result[0], ptr
        if string[ptr] == '[':
            ptr += 1
            result = unpack_list(string[ptr : ])
            ptr += result[1]
            return result[0], ptr
        if string[ptr] == '"':
            ptr += 1
            result = unpack_str(string[ptr : ])
            ptr += result[1]
            return result[0], ptr
        if not ptr == len(string) - 1:
            if string[ptr] == '-' and string[ptr + 1].isnumeric():
                ptr += 1   
                result = parse_nums(string[ptr : ])   
                ptr += result[1]   
                return -1 * result[0], ptr   
        if string[ptr].isnumeric():
            result = parse_nums(string[ptr : ])
            ptr += result[1]
            return result[0], ptr
        if string[ptr : ptr + 5] == 'false':
            ptr += 5
            return False, ptr
        if string[ptr : ptr + 4] == 'true':
            ptr += 4
            return True, ptr
        if string[ptr : ptr + 4] == 'null':
            ptr += 4
            return None, ptr
        ptr += 1
    return None, ptr

def unpack_dict(string : str):
    obj = {}
    ptr = 0
    while ptr < len(string):
        char = string[ptr]
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1   
            continue   
        if string[ptr] == '}':
            ptr += 1
            break
        result = unpack(string[ptr : ])
        key = result[0]
        ptr += result[1]   
        ptr = string.find(':', ptr) + 1   
        result = unpack(string[ptr : ])   
        obj[key] = result[0]   
        ptr += result[1]
    return obj, ptr

def unpack_list(string : str):
    obj = []
    ptr = 0
    while ptr < len(string):
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1
            continue
        if string[ptr] == ']':
            ptr += 1
            break
        result = unpack(string[ptr : ])
        obj.append(result[0])
        ptr += result[1]
    return obj, ptr

def unpack_str(string : str):
    obj = ""
    ptr = 0
    while ptr < len(string):
        if string[ptr] == '"':
            ptr += 1
            break
        obj += string[ptr]
        ptr += 1
    return obj, ptr

def parse_nums(string : str):
    obj = ""
    ptr = 0
    num_type = int
    while ptr < len(string):
        if not ptr == len(string) - 1:
            if string[ptr] == '.' and string[ptr + 1].isnumeric():
                num_type = float   
                obj += string[ptr]   
                ptr += 1   
                continue
        if not string[ptr].isnumeric():
            break
        obj += string[ptr]
        ptr += 1
    obj = int(obj) if num_type is int else float(obj)
    return obj, ptr