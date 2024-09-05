import z80

# Performs the first 10 instructions on the uninitialised system
# prints the program counter and three register values

m = z80.Z80Machine()

print(list(bytes(m.memory[0:0x10])))

m.pc = 0x0000
for i in range(10):
    print(f'{m.pc:04x}:            ; sp: {m.sp}, a: {m.a:02x}, bc: {m.bc}')
    m.ticks_to_stop = 1
    m.run()
