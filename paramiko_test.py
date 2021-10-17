from __future__ import print_function

import sys
import traceback

import paramiko
from paramiko_expect import SSHClientInteraction

def main():
    # Set login credentials and the server prompt
    hostname = ''
    username = 'root'
    password = ''
    # prompt = r'vagrant@paramiko-expect-dev:~\$\s+'
    # Use SSH client to login
    try:
        # Create a new SSH client object
        client = paramiko.SSHClient()

        # Set SSH key parameters to auto accept unknown hosts
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the host
        client.connect(hostname=hostname, username=username, password=password)

        # Create a client interaction class which will interact with the host
        interact = SSHClientInteraction(client, timeout=10, display=False)
        # interact.expect(prompt)

        # Send the tail command
        interact.send('tail -f -n 50 /home/lighthouse/1.log')

        # Now let the class tail the file for us
        interact.tail(line_prefix=hostname+': ',output_callback=output_func)

    except KeyboardInterrupt:
        print('Ctrl+C interruption detected, stopping tail')
    except Exception:
        traceback.print_exc()
    finally:
        try:
            client.close()
        except Exception:
            pass


def output_func(msg):
    # if msg:
    #     try:
    #         ws = CG_Client(ws_server)
    #         ws.connect()
    #         ws.send(msg)
    #         ws.run_forever()
    #     except KeyboardInterrupt:
    #         ws.close()

    sys.stdout.write(msg)
    sys.stdout.flush()



if __name__ == '__main__':
    main()