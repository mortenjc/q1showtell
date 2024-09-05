''' z80 emulator '''

import z80

# Performs the first 10 instructions on the uninitialised system
# prints the program counter and three register values
# Performs the first 10 instructions on system initialised with
# inc a commands
# https://clrhome.org/table/
# add instruction opcodes/operands and more registers
# Performs the first 10 instructions on system initialised with a 'program'


MAX_INSTR_SIZE = 4
INCA = 0x3c

m = z80.Z80Machine()
b = z80.Z80InstrBuilder()

program = [0xc3, 0xe5, 0x01, 0xc3, 0x77, 0x00]

# A program loader emerges
for i in range(0x10):
    for i, inst in enumerate(program):
        m.memory[i] = inst

# A memory hexdump emerges
dump = [ f'{x:02x}' for x in m.memory[0:0x10]]
print('0000:',' '.join(dump))
print()

m.pc = 0x0000
for i in range(10):
    instr = b.build_instr(m.pc, bytes(m.memory[m.pc:m.pc + MAX_INSTR_SIZE]))
    instr_bytes = bytes(m.memory[instr.addr: instr.addr + instr.size])
    instr_bytes_str = ' '.join(f'{b:02x}' for b in instr_bytes)

    print(f'{m.pc:04x}: {instr_bytes_str:12} ; sp: {m.sp}, a: {m.a:02x}, bc: {m.bc}, de: {m.de}, hl: {m.hl}')
    m.ticks_to_stop = 1
    m.run()
