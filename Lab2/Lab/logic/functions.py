import types
import builtins
import inspect

def get_vars(func):
    unbound_names = set()
    code = func.__code__

    if func.__closure__ is None:
        nonlocal_vars = {}
    else:
        nonlocal_vars = {
            var: cell.cell_contents
            for var, cell in zip(code.co_freevars, func.__closure__)
        }

    raw_globals = func.__globals__
    raw_biultins = raw_globals.get("__builtins__", builtins.__dict__)
    if inspect.ismodule(raw_biultins):
        raw_biultins = raw_biultins.__dict__
    global_vars = {}
    builtin_vars = {}

    for name in code.co_names:
        if name in ("None", "True", "False"):
            continue
        try:
            global_vars[name] = raw_globals[name]
        except KeyError:
            try:
                builtin_vars[name] = raw_biultins[name]
            except KeyError:
                unbound_names.add(name)
    return (global_vars,builtin_vars,nonlocal_vars)

def builtin_parse(builtins_dict):
    for x in builtins_dict.keys():
        if isinstance(builtins_dict[x],types.BuiltinFunctionType):
            builtins_dict[x] = {"decomposed":x,'type' : 'builtin'}
    return builtins_dict

def globals_parse(passed_function):
    func_vars = get_vars(passed_function) 
    for x in func_vars[0].keys():
        if isinstance(func_vars[0][x],types.FunctionType):
            func_vars[0][x] = {"decomposed":func_to_dict(func_vars[0][x]),'type' : 'func'}
        elif isinstance(func_vars[0][x],types.ModuleType):
            func_vars[0][x] = {"decomposed": func_vars[0][x].__name__,'type' : "module"}
        else:
            func_vars[0][x] = {"decomposed": x,'type' : "primitive"}
    builtin_parse(func_vars[1])
    _globals = {}
    _globals.update(builtin_parse(func_vars[1]))
    _globals.update(func_vars[0])
    return _globals

def read_globals(globals_dict):
    new_dict = {}
    for x in globals_dict.keys():
        if globals_dict[x]['type'] == 'module':
            exec(f'import {globals_dict[x]["decomposed"]}')
            new_dict[x] = eval(f'{globals_dict[x]["decomposed"]}')
            print(globals_dict[x])
        elif globals_dict[x]['type'] == 'func':
            new_dict[x] = dict_to_func(globals_dict[x]['decomposed'])
        elif globals_dict[x]['type'] == 'builtin':
            new_dict[x] = getattr(builtins,globals_dict[x]['decomposed'])
        elif globals_dict[x]['type'] == 'primitive':
            new_dict[x] = globals_dict[x]['decomposed']
    return new_dict

def func_to_dict(func):
    func_dict = {}
    func_dict["globals"] = globals_parse(func)
    func_dict["name"] = func.__name__    
    func_dict["defaults"] = func.__defaults__
    func_dict["code"] = code_to_dict(func.__code__)
    return func_dict

def code_to_dict(code):
    code_dict = {}
    code_dict["co_argcount"] = code.co_argcount
    code_dict["co_cellvars"] = code.co_cellvars
    code_dict["co_consts"] = code.co_consts
    code_dict["co_filename"] = code.co_filename
    code_dict["co_firstlineno"] = code.co_firstlineno
    code_dict["co_flags"] = code.co_flags  
    code_dict["co_freevars"] = code.co_freevars
    code_dict["co_kwonlyargcount"] = code.co_kwonlyargcount
    code_dict["co_lnotab"] = [ord(chr(x)) for x in code.co_lnotab]
    code_dict["co_name"] = code.co_name
    code_dict["co_names"] = code.co_names
    code_dict["co_nlocals"] = code.co_nlocals
    code_dict["co_stacksize"] = code.co_stacksize
    code_dict["co_varnames"] = code.co_varnames
    code_dict["co_posonlyargcount"] = code.co_posonlyargcount
    code_dict["co_code"] = [ord(chr(x)) for x in code.co_code ]
    return code_dict

def dict_to_code(_dict):
    interpreted_code = types.CodeType(_dict["co_argcount"],
    _dict["co_posonlyargcount"],
    _dict["co_kwonlyargcount"],
    _dict["co_nlocals"],
    _dict["co_stacksize"],
    _dict["co_flags"],
    bytes(_dict["co_code"]),
    tuple(_dict["co_consts"]),
    tuple(_dict["co_names"]),
    tuple(_dict["co_varnames"]),
    _dict["co_filename"],
    _dict["co_name"],
    _dict["co_firstlineno"],
    bytes(_dict["co_lnotab"]),
    tuple(_dict["co_freevars"]),
    tuple(_dict["co_cellvars"]))
    return interpreted_code

def dict_to_func(_dict):
    globals = read_globals(_dict['globals'])
    func = [dict_to_code(_dict["code"]),globals,_dict["name"],_dict["defaults"]]
    return types.FunctionType(*func)

