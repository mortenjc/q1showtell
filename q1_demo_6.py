import z80

# Performs the first 10 instructions on the uninitialised system
# prints the program counter and three register values
# Performs the first 10 instructions on system initialised with
# inc a commands
# https://clrhome.org/table/
# add instruction opcodes/operands and more registers
# Performs the first 10 instructions on system initialised with a 'program'
# Performs the first 10 instructions on system initialised with two program
# snippets: program, program2
# add assembly mnemonics

MAX_INSTR_SIZE = 4
INCA = 0x3c

m = z80.Z80Machine()
b = z80.Z80InstrBuilder()

program = [0xc3, 0xe5, 0x01, 0xc3, 0x77, 0x00]
program2 = [0xed, 0x56, 0x3e, 0x04, 0xd3, 0x01, 0x11, 0x3f, 0x00,0x21, 0x80]

# A program loader emerges
for i, inst in enumerate(program):
    m.memory[i] = inst
for i, inst in enumerate(program2):
    m.memory[0x01e5 + i] = inst


# A memory hexdump emerges
dump = [ f'{x:02x}' for x in m.memory[0:0x10]]
print('0000:',' '.join(dump))
print()

m.pc = 0x0000
for i in range(10):
    instr = b.build_instr(m.pc, bytes(m.memory[m.pc:m.pc + MAX_INSTR_SIZE]))
    instr_str = f"{instr}"
    instr_bytes = bytes(m.memory[instr.addr: instr.addr + instr.size])
    instr_bytes_str = ' '.join(f'{b:02x}' for b in instr_bytes)

    print(f'{m.pc:04x}: {instr_bytes_str:12} ; {instr_str:25} | sp: {m.sp}, a: {m.a:02x}, bc: {m.bc}, de: {m.de:04x}, hl: {m.hl:04x}')
    m.ticks_to_stop = 1
    m.run()
