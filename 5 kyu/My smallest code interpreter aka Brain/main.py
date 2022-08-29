

class BrainFuck():
    pointer = 0
    data = {}
    out = ""
    i_code = 0

    def __init__(self, code, program_input) -> None:
        self.program_input = str(program_input)
        self.code = code
        self.len_code = len(code)
        self.commands = {
            ">": self.inc_pointer,
            "<": self.dec_pointer,
            "+": self.inc_data,
            "-": self.dec_data,
            ".": self.write_output,
            ",": self.read_input,
            "[": self.start_cycle,
            "]": self.end_cycle,
        }

    def inc_pointer(self):
        self.pointer += 1

    def dec_pointer(self):
        self.pointer -= 1

    def inc_data(self):
        self.data_in_pointer = self.data.get(self.pointer)
        if not self.data_in_pointer:
            self.data.update({self.pointer: (0 + 1) % 256})
        else:
            self.data.update({self.pointer: (self.data_in_pointer + 1) % 256})
    
    def dec_data(self):
        self.data_in_pointer = self.data.get(self.pointer)
        if not self.data_in_pointer:
            self.data.update({self.pointer: (0 - 1) % 256})
        else:
            self.data.update({self.pointer: (self.data_in_pointer - 1) % 256})
    
    def write_output(self):
        self.out += chr(self.data[self.pointer])
        
    def read_input(self):
        if len(self.program_input) != 0:
                self.data.update({self.pointer: ord(self.program_input[0])})
                self.program_input = self.program_input[1:]

    def next_ins_tacker(self, i_code:int, code:str) -> int:
        counter = 0
        for i, code_elem in enumerate(code[i_code + 1:]):
            if code_elem == "[":
                counter += 1
            elif code_elem == "]":
                if counter == 0:
                    return i_code + 1 + i
                counter -= 1
                
    def prev_ins_tacker(self, i_code:int, code:str) -> int:
        counter = 0
        for i, code_elem in enumerate(code[i_code - 1::-1]):
            if code_elem == "]":
                counter += 1
            elif code_elem == "[":
                if counter == 0:
                    return i_code - (i + 1)
                counter -= 1
    
    def start_cycle(self):
        if self.data.get(self.pointer) == 0 or self.data.get(self.pointer) == None:
                    self.i_next = self.next_ins_tacker(self.i_code,self.code)
                    self.i_code = self.i_next

    def end_cycle(self):
        if self.data.get(self.pointer) != 0 and self.data.get(self.pointer) != None:
            self.i_prev = self.prev_ins_tacker(self.i_code,self.code)
            self.i_code = self.i_prev


def brain_luck(code:str, program_input:str) -> str:
    
    brainLuck = BrainFuck(code=code, program_input=program_input)
    while brainLuck.i_code < brainLuck.len_code:
        code_elem = code[brainLuck.i_code]
        brainLuck.commands.get(code_elem)()
        brainLuck.i_code += 1
        out = brainLuck.out
    return brainLuck.out

print(
brain_luck('>++++[-<+++++++++++>]>,[>++++++[-<-------->]>+++++++++[-<<<[->+>+<<]>>[-<<+>>]>]<<[-<+>],]<<+++++.-----.+++++.----->-->+>+<<[-<.>>>[->+>+<<]<[->>>+<<<]>>[-<<+>>]>[->+<<<+>>]>[>>>>++++++++++<<<<[->+>>+>-[<-]<[->>+<<<<[->>>+<<<]>]<<]>+[-<+>]>>>[-]>[-<<<<+>>>>]<<<<]<[>++++++[<++++++++>-]<-.[-]<]<<<<]', "9")
)

