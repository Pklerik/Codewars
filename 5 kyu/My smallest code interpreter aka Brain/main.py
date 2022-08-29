class BrainFuck():
    pass
def brain_luck(code:str, program_input:str) -> str:

    def next_ins_tacker(i_code:int, code:str) -> int: #TODO find error in count [] method shoud find next, not first
        counter = 0
        for i, code_elem in enumerate(code[i_code:]):
            if code_elem == "[":
                counter += 1
            elif code_elem == "]":
                if counter == 0:
                    return i #+ i_code
                counter -= 1
                
    def prev_ins_tacker(i_code:int, code:str) -> int:
        counter = 0
        for i, code_elem in enumerate(code[i_code - 1::-1]):
            if code_elem == "]":
                counter += 1
            elif code_elem == "[":
                if counter == 0:
                    return i_code - (i + 1)
                counter -= 1
    pointer = 0
    data = {}
    out = ""
    i_code = 0
    len_code = len(code)
    while i_code < len_code:
        code_elem = code[i_code]
        match code_elem:
            case ">":
                pointer += 1
            case "<":
                pointer -= 1
            case "+":
                try:
                    if data[pointer] + 1 > 255:
                        data[pointer] += 1 - 256
                    else:
                        data[pointer] += 1
                except:
                    data.update({pointer: 0})
                    if data[pointer] + 1 > 255:
                        data[pointer] += 1 - 256
                    else:
                        data[pointer] += 1
            case "-":
                try:
                    if data[pointer] - 1 < 0:
                        data[pointer] = data[pointer] - 1 + 256
                    else:
                        data[pointer] = data[pointer] - 1
                except:
                    data.update({pointer: 0})
                    if data[pointer] + 1 > 255:
                        data[pointer] += 1 - 256
                    else:
                        data[pointer] += 1
            case ".":
                out += chr(data[pointer])
                # data.pop(pointer)
                # pointer = 0

            case ",":
                if len(program_input) == 0:
                    break

                data.update({pointer: ord(program_input[0])})
                program_input = program_input[1:]   

            case "[":
                if data.get(pointer) == 0 or data.get(pointer) == None:
                    i_next = next_ins_tacker(i_code,code)
                    i_code = i_next
                # elif data[pointer] == chr(0):
                #     i_next = next_ins_tacker(i_code,code)
                #     i_code = i_next
            case "]":
                if data.get(pointer) != 0 and data.get(pointer) != None:
                    i_prev = prev_ins_tacker(i_code,code)
                    i_code = i_prev
                if data.get(pointer) == 0 or data.get(pointer) == None:
                    pass
                # elif data[pointer] != chr(0):
                #     i_code = i_prev   
        i_code += 1      
    return out

print(
brain_luck(',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]', chr(10))
)