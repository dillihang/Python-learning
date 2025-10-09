import string
import operator
"""
Executes a simple custom programming language with variables, arithmetic operations, and flow control.

The language supports the following commands:
- PRINT [value]: prints the value
- MOV [variable] [value]: assigns the value to the variable
- ADD [variable] [value]: adds the value to the variable
- SUB [variable] [value]: subtracts the value from the variable
- MUL [variable] [value]: multiplies the variable by the value
- [location]:: marks a line of code with a label for jumps
- JUMP [location]: jumps to the labeled line
- IF [condition] JUMP [location]: jumps to the label if the condition is true
- END: ends execution

Arguments:
    program (list): A list of strings, where each string is a line of code.

Returns:
    list: A list containing the results of all executed PRINT commands.

Notes:
- The program has 26 pre-defined variables, A to Z, all initialized to 0.
- [value] can be an integer or a variable.
- [condition] must use one of the operators: ==, !=, <, <=, >, >=
- The function assumes the program is correctly formatted and does not handle input validation.
"""
def run(program: list):

    operator_map = {
                    '<=': operator.le, 
                    '>=': operator.ge,
                    '==': operator.eq, 
                    '!=': operator.ne,
                    '<': operator.lt,
                    '>': operator.gt
                    }
    result_list=[]
    main_dict={}
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t=0
    i=0

    for char in alphabet:
        main_dict[char]=0

    while i < len(program):

        if "MOV" in program[i]:
            if program[i][6:] in string.ascii_letters:
                main_dict[program[i][4]]=int(main_dict[program[i][6]])
            else:
                main_dict[program[i][4]]=int(program[i][6:])
            
        elif "ADD" in program[i]:
            if program[i][6:] in string.ascii_letters:
                add_value=int(main_dict[program[i][4]]) + int(main_dict[program[i][6]])
                main_dict[program[i][4]]=add_value
            else:
                add_value=int(main_dict[program[i][4]]) + int(program[i][6])
                main_dict[program[i][4]]=add_value

        elif "MUL" in program[i]:
            if program[i][6:] in string.ascii_letters:
                mul_value=int(main_dict[program[i][4]]) * int(main_dict[program[i][6]])
                main_dict[program[i][4]]=mul_value
            else:
                mul_value=int(main_dict[program[i][4]]) * int(program[i][6])
                main_dict[program[i][4]]=mul_value

        elif "SUB" in program[i]:
            if program[i][6:] in string.ascii_letters:
                sub_value=int(main_dict[program[i][4]]) - int(main_dict[program[i][6]])
                main_dict[program[i][4]]=sub_value
            else:
                sub_value=int(main_dict[program[i][4]]) - int(program[i][6])
                main_dict[program[i][4]]=sub_value

        elif "PRINT" in program[i]:
            if program[i][6:] in string.digits:
                result_list.append(int(program[i][6:]))
            else:
                result_list.append(main_dict[program[i][6]])

        elif ":" in program[i]:
            marked_string=program[i]
            marked_location=i
            # print(marked_location)
            # print(marked_string)

        elif "JUMP" in program[i]:
            if program[i].startswith("JUMP"):
                check_string=program[i][5:] + ":"
                if check_string==marked_string:
                    i=marked_location
                
            else:
                jump_index=program[i].find("JUMP")
                condition_string=program[i][:jump_index]
                # print(condition_string)
                value = condition_string.split()
                # print(value)
                # IF=value[0].lower()
                firstvalue=value[1]
                secondvalue=value[3]
                compare_element=value[2]
                if firstvalue in string.ascii_letters and secondvalue in string.ascii_letters:
                    TorF = operator_map[compare_element](main_dict[firstvalue], main_dict[secondvalue])
                elif firstvalue in string.ascii_letters and secondvalue.isdigit():
                    TorF = operator_map[compare_element](main_dict[firstvalue], int(secondvalue))

                if TorF == True:
                    checkstring2=program[i][jump_index+5:]+":"
                    # print(checkstring2)
                    
                    while t<len(program):
                        if checkstring2 in program[t]:
                            i=t
                            # print(i)
                        t+=1
                else:
                    pass

        elif "END" in program[i]:
            break
        
        # print(i)

        i+=1
        t=0

    # print(main_dict)
        
    return result_list

if __name__=="__main__":

    # program1 = []
    # program1.append("MOV A 1")
    # program1.append("MOV B 2")
    # program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    # program1.append("END")
    # result = run(program1)
    # print(result)

    # program2 = []
    # program2.append("MOV A 1")
    # program2.append("MOV B 10")
    # program2.append("begin:")
    # program2.append("IF A >= B JUMP quit")
    # program2.append("PRINT A")
    # program2.append("PRINT B")
    # program2.append("ADD A 1")
    # program2.append("SUB B 1")
    # program2.append("JUMP begin")
    # program2.append("quit:")
    # program2.append("END")
    # result = run(program2)
    # print(result)

    # program3 = []
    # program3.append("MOV A 1")
    # program3.append("MOV B 1")
    # program3.append("begin:")
    # program3.append("PRINT A")
    # program3.append("ADD B 1")
    # program3.append("MUL A B")
    # program3.append("IF B <= 10 JUMP begin")
    # program3.append("END")
    # result = run(program3)
    # print(result)

    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
