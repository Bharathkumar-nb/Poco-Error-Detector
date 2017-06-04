import ast

'''
    Parameters :    node
    Description :   Utility function for check_matching_if_else.
                    Takes 'If' node as parameter and checks if it is properly constructed with matching else.
'''
def check_matching_if_else_util(node):
    result = []
    if len(node.orelse) == 0:
        result += ["No else part found for 'if' statement at Line number {}".format(node.lineno)]
    for sub_node in node.body:
        if isinstance(sub_node, ast.If):
            result += check_matching_if_else_util(sub_node)
    for sub_node in node.orelse:
        if isinstance(sub_node, ast.If):
            result += check_matching_if_else_util(sub_node)
    return result

'''
    Parameters :    tree
    Description :   Checks for matching if-else statements.
'''
def check_matching_if_else(tree):
    result = []
    for body in tree.body:
        if isinstance(body, ast.FunctionDef):
            for node in body.body:
                if isinstance(node, ast.If):
                    result += check_matching_if_else_util(node)
        if isinstance(body, ast.If):
            result += check_matching_if_else_util(body)
    return result


def format_result(result):
    output_error = ''
    for error in result:
        output_error += '<div class="well">'
        output_error += error
        output_error += '</div>'
    if len(result) == 0:
        output_error += 'No Errors'
    return output_error


def parseResult(form):
    code = form['code']
    print(form)
    print('code', code)
    try:
        tree = ast.parse(code)
        result = check_matching_if_else(tree)
    except Exception as e:
        result = [str(e)]
    return format_result(result)