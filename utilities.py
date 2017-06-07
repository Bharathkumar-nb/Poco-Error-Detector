import ast

'''
    Parameters :    node
    Description :   Utility function for check_matching_if_else.
                    Takes 'If' node as parameter and checks if it is properly constructed with matching else.
'''
def check_matching_if_else_util(node, return_variable_name):
    result = []

    if len(node.orelse) == 0:
        result += ["No else part found for 'if' statement at Line number {}".format(node.lineno)]
    
    if len(node.body) > 1:
        result += ["More than one executable statement in the 'if' branch. Please check line numbers {} to {} for errors".format(node.body[0].lineno, node.body[0].lineno+len(node.body)-1)]
    
    if len(node.orelse) > 1:
        result += ["More than one executable statement in the 'else' branch. Please check line numbers {} to {} for errors".format(node.orelse[0].lineno, node.orelse[0].lineno+len(node.orelse)-1)]
    
    if len(node.body) == 1:
        sub_node = node.body[0]
        if isinstance(sub_node, ast.If):
            result += check_matching_if_else_util(sub_node)
        elif not (isinstance(sub_node, ast.Assign) and sub_node.targets[0].id == return_variable_name):
            result += ["The statement at Line number {} is neither 'if statement' nor assigning prediction.".format(sub_node.lineno)]
            if isinstance(sub_node, ast.Assign) and sub_node.targets[0].id != return_variable_name:
                result[-1] += '<br/>Please make sure that return variable name matches assigned variable name'
            

    if len(node.orelse) == 1:
        sub_node = node.orelse[0]
        if isinstance(sub_node, ast.If):
            result += check_matching_if_else_util(sub_node)
        elif not (isinstance(sub_node, ast.Assign) and sub_node.targets[0].id == return_variable_name):
            result += ["The statement at Line number {} is neither 'if statement' nor assigning prediction.".format(sub_node.lineno)]
        if isinstance(sub_node, ast.Assign) and sub_node.targets[0].id != return_variable_name:
                result[-1] += '<br>Please make sure that return variable name matches assigned variable name'
    return result

'''
    Parameters :    tree
    Description :   Checks for matching if-else statements.
'''
def check_matching_if_else(tree):
    result = []
    isPredictorFunctionFound = False
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and 'predict' in node.name.lower():
            isPredictorFunctionFound = True
            last_statement = node.body[-1]
            return_variable_name = None
            if isinstance(last_statement, ast.Return):
                if not isinstance(last_statement.value, ast.Name):
                    result += ["Return statement expects to return 'prediction' variable"]
                    break
                else:
                    return_variable_name = last_statement.value.id
            if return_variable_name == None:
                result += ['Predictor function has no return statement.']
                break
            isIfStatementFound = False
            for func_node in node.body:
                if isinstance(func_node, ast.If):
                    isIfStatementFound = True
                    result += check_matching_if_else_util(func_node, return_variable_name)
            if not isIfStatementFound:
                result += ["No if statements found in the '{}' function".format(node.name)]
    if not isPredictorFunctionFound:
        result = ['No predictor function found!']
    return result


def format_result(result):
    output_error = ''
    for error in result:
        output_error += '<div class="well">'
        output_error += error
        output_error += '</div>'
    if len(result) == 0:
        output_error += '<div class="well">No Errors</div>'
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