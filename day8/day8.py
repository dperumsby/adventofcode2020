def load_instructions():
    with open("input.txt", "r") as file:
        instructions = file.read().splitlines()
    return instructions


class HandheldDebugger:
    """For debugging whiny kids' handheld games consoles"""

    def __init__(self, instructions):
        self.acc_total = 0
        self.inst_counter = 0
        self.instructions = instructions
        
        self.operations = {
            "acc": self.acc,
            "jmp": self.jmp,
            "nop": self.nop,
        }

        self.cache = {}

    def acc(self, value):
        self.acc_total += int(value)

    def jmp(self, value):
        self.inst_counter += int(value)

    def nop(self, value):
        pass

    def run_code(self, instructions = None): # Stops immediately before loops (if any)
        if instructions == None:
            instructions = self.instructions
        
        self.inst_counter = 0
        self.acc_total = 0
        self.cache = {}

        while True:
            if self.inst_counter in self.cache: 
                break

            if self.inst_counter == len(self.instructions):
                return True
            
            self.cache[self.inst_counter] = True

            op = instructions[self.inst_counter][:3]
            value = instructions[self.inst_counter][4:]
            
            self.operations[op](value)

            if op != "jmp": self.inst_counter += 1
    
    def repair_corrupt_inst(self):
        self.run_code()
        original_cache = self.cache.keys()

        for inst_number in original_cache:
            alt_instructions = self.instructions.copy()
            op = self.instructions[inst_number][:3]
            value = self.instructions[inst_number][4:]
            
            if op == "jmp":
                alt_instructions[inst_number] = f"nop {value}"
            elif op == "nop":
                alt_instructions[inst_number] = f"jmp {value}"
            else:
                continue

            fixed = self.run_code(alt_instructions)

            if fixed:
                self.instructions = alt_instructions
                break
        

instructions = load_instructions()
kids_code = HandheldDebugger(instructions)

kids_code.run_code()
print(kids_code.acc_total) # 1749

kids_code.repair_corrupt_inst()
print(kids_code.acc_total) # 515
