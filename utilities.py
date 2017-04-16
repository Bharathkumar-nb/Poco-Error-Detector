from mod9ch2 import mod9ch2

def get_func_name(module_no, challenge_no):
    return 'mod'+module_no+'ch'+challenge_no
    
def parseResult(form):
    func_map = {'mod9ch2':mod9ch2}
    
    result = func_map[get_func_name(form['opt_module'], form['opt_challenge'])](form['code'])
    return result