import ptrace.debugger as ptd
import subprocess as sp
import binascii as ba
import signal as sig

## step through target process's execution
def step(process):
    process.singleStep()
    process.waitSignals(sig.SIGTRAP)

## injects instruction into target process
def run_instr(instr):
    prev_rip = process.getreg("rip")
    prev_vals = process.readBytes(prev_rip, len(instr))
    process.writeBytes(prev_rip, instr)
    step()

    if process.getreg("rip") == prev_rip + len(instr):
        process.setreg(prev_rip, prev_vals)
    
    process.writeBytes(prev_rip, prev_vals)




if __name__ == "__main__":

    ## sets up debugger env and 
    sh_cmd = ["./a.out"]
    c_proc = sp.Popen(sh_cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    pid = c_proc.pid
    debugger = ptd.PtraceDebugger()
    process = debugger.addProcess(pid, False)