from paramiko import SSHClient
from scp import SCPClient

from config.configuration import SCP_TARGETS


# src https://github.com/jbardin/scp.py
# TODO Expand, dependant on API direction.

def run_target(target):
    """
    SCPs file over to target.
    :param target: 
    :return: 
    """
    print(f'Connecting to {target}')
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(target)
    scp = SCPClient(ssh.get_transport())
    try:
        scp.put("test.txt")
    except Exception as e:
        print(e)
    finally:
        scp.close()


def execute():
    """
    Execute each scp transfer.
    :return: 
    """
    [run_target(target) for target in SCP_TARGETS]
