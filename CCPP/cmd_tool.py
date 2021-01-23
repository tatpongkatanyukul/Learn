import subprocess


def cmd(prefix, testcmd, suffix, itxt, rtime):

    runcmd = prefix + testcmd + suffix
    cmd_chain = runcmd.split(';')

    rout = ''

    for i, c in enumerate(cmd_chain):

        tcmd = c.strip()
        print('cmd_tool: run cmd {}: {}'.format(i, tcmd))

        ctokens = c.split(' ')
        if len(ctokens[0]) < 1:
            ctokens = ctokens[1:]

        # print('* ctokens:', ctokens)


        run_complete = True
        try:
            prc = subprocess.run(ctokens,
                                 input=str.encode(itxt),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 timeout=rtime)

            rout += str(prc.stdout, 'utf-8')

            if len(prc.stderr) > 0:
                print('* cmd tool: stderr = \n', prc.stderr)
                run_complete = False
                return run_complete, rout


        except Exception as e:
            print('* test case', i, ': exception: ' + str(e))

            run_complete = False
            return run_complete, rout


        # end try-except
    # end for
    return run_complete, rout

if __name__ == '__main__':
    r1, r2 = cmd("./", "Q_aux2.exe Q1.txt", "", "dummyinput", 1)
    print('r1 = ', r1)
    print('r2 = ', r2)
    r1, r2 = cmd("", "g++ P4.cpp -o p.exe; ./p.exe", "; python readhead.py P4.cpp", "dummyinput", 1)
    print('r1 = ', r1)
    print('r2 = ', r2)
