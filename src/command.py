from subprocess import Popen

def cmd_run(command):
    log = open('log.txt', 'a')
    log.write('some text, as header of the file\n')
    log.flush()
    proc = Popen(command, stdout=log, stderr=log, shell=False)
    proc.wait()

cmd_run("sleep 5; ls -la; echo yusuf")
