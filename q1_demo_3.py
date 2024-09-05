''' z80 emulator '''

import z80

# Performs the first 10 instructions on the uninitialised system
# prints the program counter and three register values
# Performs the first 10 instructions on system initialised with
# inc a commands
# https://clrhome.org/table/
# add instruction opcodes/operands and more registers

MAX_INSTR_SIZE = 4
INCA = 0x3c

m = z80.Z80Machine()
b = z80.Z80InstrBuilder()

for i in range(0x10):
    m.memory[i] = INCA
print(bytes(m.memory[0:0x10]))

m.pc = 0x0000
for i in range(10):
    instr = b.build_instr(m.pc, bytes(m.memory[m.pc:m.pc + MAX_INSTR_SIZE]))
    instr_bytes = bytes(m.memory[instr.addr: instr.addr + instr.size])
    instr_bytes_str = ' '.join(f'{b:02x}' for b in instr_bytes)

    print(f'{m.pc:04x}: {instr_bytes_str:12} ; sp: {m.sp}, a: {m.a:02x}, bc: {m.bc}, de: {m.de}, hl: {m.hl}')
    m.ticks_to_stop = 1
    m.run()
