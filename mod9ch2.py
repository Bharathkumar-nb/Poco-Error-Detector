import ast

def check_education(node):
    result = 'Success'
    if_body = None
    else_body = None
    # To check if education condition is present
    hasEducationCheck = False
    
    # Check if condition for graduate present
    if (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Graduate') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Graduate'))) or\
       (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Not Graduate') and (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Not Graduate'))):
           if_body, else_body = node.body, node.orelse
           hasEducationCheck = True
           print("Match if condition")
    elif (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Graduate') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Graduate'))) or\
         (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Not Graduate') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Not Graduate'))):
           if_body, else_body = node.orelse, node.body
           hasEducationCheck = True
           print('Match else condition')
    print(if_body, else_body)
    if not hasEducationCheck:
        result = "Error or No check for education in the tree"
    else:
        if len(else_body)>0:
            result = check_credit_history(if_body[0])
            if result == 'Success': # check the else part only if if_body is success
                result = check_property_area(else_body[0])
        else:
            result = 'No else part found for Education check'
    print(result)
    return result

def check_credit_history(node):
    result = 'Success'
    if_body = None
    else_body = None
    # To check if credit history condition is present
    hasCreditCheck = False
    
    # Check if condition for credit history present
    if (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Num) and node.test.comparators[0].n == 1) or (isinstance(node.test.left, ast.Num) and node.test.left.n == 1))) or\
       (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Num) and node.test.comparators[0].n == 0) or (isinstance(node.test.left, ast.Num) and node.test.left.n == 0))):
           print("Match if condition")
           if_body, else_body = node.body, node.orelse
           hasCreditCheck = True
    elif (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Num) and node.test.comparators[0].n == 1) or (isinstance(node.test.left, ast.Num) and node.test.left.n == 1))) or\
         (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Num) and node.test.comparators[0].n == 0) or (isinstance(node.test.left, ast.Num) and node.test.left.n == 0))):
           if_body, else_body = node.orelse, node.body
           hasCreditCheck = True
           print('Match else condition')
    print(if_body, else_body)
    if not hasCreditCheck:
        result = "Error or No check for credit history in the tree"
    else:
        if(len(else_body) > 0):
            result = check_final_statement(if_body[0],'Y')
            if result == 'Success': # check the else part only if if_body is success
                result = check_final_statement(else_body[0],'N')
        else:
            result = 'No else part found for Credit history check'
    
    return result

def check_property_area(node):
    result = 'Success'
    if_body = None
    else_body = None
    # To check if property condition is present
    hasProperty = False
    
    # Check if condition for property present
    if (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Rural') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Rural'))):
           if_body, else_body = node.body, node.orelse
           hasProperty = True
    elif (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Rural') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Rural'))):
           if_body, else_body = node.orelse, node.body
           hasProperty = True
    
    if not hasProperty:
        result = "Error or No check for property in the tree"
    else:
        if(len(else_body) > 0):
            result = check_married(if_body[0])
            if result == 'Success': # check the else part only if if_body is success
                result = check_final_statement(else_body[0],'N')
        else:
            result = 'No else part found for property check'
    
    return result
    
def check_married(node):
    result = 'Success'
    if_body = None
    else_body = None
    # To check if married condition is present
    hasMarriedCheck = False
    
    # Check if condition for married present
    if (isinstance(node.test.ops[0],ast.Eq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Yes') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Yes'))) or\
       (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'No') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'No'))):
           if_body, else_body = node.body, node.orelse
           hasMarriedCheck = True
    elif (isinstance(node.test.ops[0],ast.NotEq) and ((isinstance(node.test.comparators[0], ast.Str) and node.test.comparators[0].s == 'Yes') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'Yes'))) or\
         (isinstance(node.test.ops[0],ast.Eq) and (isinstance(node.test.comparators[0], ast.Str) and (node.test.comparators[0].s == 'No') or (isinstance(node.test.left, ast.Str) and node.test.left.s == 'No'))):
           if_body, else_body = node.orelse, node.body
           hasMarriedCheck = True
    
    if not hasMarriedCheck:
        result = "Error or No check for married in the tree"
    else:
        if(len(else_body) > 0):
            result = check_final_statement(if_body[0],'Y')
            if result == 'Success': # check the else part only if if_body is success
                result = check_final_statement(else_body[0],'N')
        else:
            result = 'No else part found for Married check'
    
    return result

def check_final_statement(node, ret_val):
    result = 'Success'
    if isinstance(node, ast.Return) or isinstance(node, ast.Assign):
        if (not isinstance(node.value, ast.Str)) or  node.value.s != ret_val:
            result = 'Wrong return value at ' + str(node.lineno)
    return result        
    
def mod9ch2(code):
    tree = ast.parse(code)
    #exec(compile(tree, filename="<ast>", mode="exec"))
    result = "Success"
    
    # To check if predictor Function exist
    hasPredictorFun = False
    
    for body in tree.body:
        if isinstance(body, ast.FunctionDef) and body.name == 'predictor':
            hasPredictorFun = True

            for node in body.body:
                # Check tree
                if isinstance(node, ast.If):
                     result = check_education(node)
                     print(result)
                     if result != "Error or No check for education in the tree":
                         break
            break
            
    if not hasPredictorFun:
        result = "No Module named 'predictor' found!! Please recheck the function name"
    
    return result
