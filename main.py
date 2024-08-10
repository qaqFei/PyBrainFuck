from sys import argv; from ctypes import windll; _, bf, memory, ptr = (print("Usage: main <brainfuck_program>"), windll.kernel32.ExitProcess(0)) if len(argv) < 2 else None, open(argv[1], "r", encoding="utf-8").read(), {}, 0
def flend(code, start):
    n = 0
    for i, c in enumerate(code[start:]):
        if c == "[": n += 1
        elif c == "]":
            n -= 1
            if n <= 0: return start + i
    windll.kernel32.ExitProcess(1) # segfault
def interpret(code):
    global ptr; cn = 0
    for i, c in enumerate(code):
        if cn > 0: cn -= 1; continue
        match c:
            case "+": memory[ptr] = ((memory[ptr] if ptr in memory else 0) + 1) % 255
            case "-": memory[ptr] = ((memory[ptr] if ptr in memory else 0) - 1) % 255
            case ">": ptr += 1
            case "<": ptr -= 1; windll.kernel32.ExitProcess(0) if ptr < 0 else None
            case ".": print(chr(memory[ptr] if ptr in memory else 0), end="")
            case ",": memory[ptr] = ord(input()[0])
            case "[":
                s, e = i, flend(code, i); cn += e - i
                while memory[ptr] if ptr in memory else 0: interpret(code[s + 1:e])
interpret(bf)