from stacks_code_lab import *

def eval_prefix(exp_str):
    operator = "+-*/"
    exp_lst = exp_str.split()
    args_stack = ArrayStack()

    for i in range(len(exp_lst)-1, -1, -1):
        token = exp_lst[i]
        if token not in operator: # when it's integer
            args_stack.push(int(token))
        else:
            arg1 = args_stack.pop()
            arg2 = args_stack.pop()
            if token == "+":
                res = arg1 + arg2
            elif token == "-":
                res = arg1 - arg2
            elif token == "*":
                res = arg1 * arg2
            else:
                if arg2 == 0:
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()     


exp_str = "- + * 16 5 * 8 4 20"
exp_str2 = "- * 3 4 10"
print(eval_prefix(exp_str))
print(eval_prefix(exp_str2))