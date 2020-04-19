#eval() builtin function in python
# It evaluates any expression you pass through it in the form of string
# but it can't evaluate a definition



list_str = eval("[1, 2, 44, 6]")



# exec() compiles and evaluates whatever you pass through it in the form of string

exec("def func(): print('Hello world')")
func()
