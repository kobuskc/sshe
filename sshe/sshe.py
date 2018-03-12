'''
MIT License

Copyright (c) 2018 Kobus Coetzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
import argparse
import boto3
import subprocess
import sys
from botocore.exceptions import ClientError
from tabulate import tabulate

class sshe(object):

    def __init__(self):
        self.args = None
        self.s = boto3.Session()
        self.ec2 = None
        self.Agent = None
        self.Dynamic = None
        self.Local = None
        self.login = None
        self.quiet = None
        self.region = None
        self.timeout = None

    def set_cli_args(self):
        # Arguments we support
        parser = argparse.ArgumentParser()
        parser.add_argument('-Agent', action="store_true",
                            help="Enables forwarding of the authentication agent connection.")
        parser.add_argument('-Dynamic', type=str,
                            help="Specifies a local 'dynamic' application-level port forwarding.")
        parser.add_argument('-Local', type=str, help="Specifies a local port to forward to the remote server.")
        parser.add_argument('-login', type=str, default='ec2-user', help="The username you want to connect with." \
                            "The default is ec2-user")
        parser.add_argument('-quiet', action="store_true", help="Hide all SSH error messages")
        parser.add_argument('-region', type=str, help="Which region is the instance in?")
        parser.add_argument('-timeout', type=int, help="How many seconds do you want to wait?" \
                            "The default is 10 seconds.", default=10)

        cmdargs = parser.parse_args()

        self.Agent = cmdargs.Agent
        self.Dynamic = cmdargs.Dynamic
        self.Local = cmdargs.Local
        self.login = cmdargs.login
        self.quiet = cmdargs.quiet
        self.region = cmdargs.region
        self.timeout = cmdargs.timeout

    def ec2Instances(self):
        # Check if the region was specified, otherwise get the region from the current session
        if self.region:
            self.ec2 = boto3.resource('ec2', region_name=self.region)
        else:
            self.ec2 = boto3.resource('ec2', region_name=self.s.region_name)

        rows = []
        try:

            # Enumerate instances
            instances = self.ec2.instances.all()

            for i in instances:
                if i.state['Name'] == 'running':
                    instanceId = i.id
                    pubDns = i.public_dns_name
                    instanceName=''

                    for tag in i.tags:
                        if tag['Key'] == 'Name':
                            instanceName = tag['Value']
                            break
                    rows.append([instanceId, instanceName, pubDns])

        except ClientError as e:
            message = '\n' + e.response['Error']['Code'] + ': ' + e.response['Error']['Message']
            exit(message)
        except KeyError as e:
            message = 'The following Key does not exist: ' + str(e)
            exit(message)
        except:
            message = "An unexpected error occurred: ", sys.exc_info()[0]
            exit(message)

        return rows

    def printInstances(self, instances):
        count = instances.__len__()
        itr = (i for i, x in enumerate(instances))
        print(tabulate([(i, instances[i][0], instances[i][1]) for i in itr], headers=["#", "Instance", "Name"], tablefmt="simple"))

        print("\n%d Quit\n" % (count))

        while True:
            try:
                choice = int(input("Please select an instance: "))
            except ValueError:
                print("Please enter a valid option.")
                continue
            else:
                if 0 <= choice < (count):
                    return choice
                if choice == (count):
                    exit(0)
                else:
                    print("Please enter a valid option.")
                    continue

    def run(self):
        self.set_cli_args()
        instances = self.ec2Instances()
        choice = self.printInstances(instances)

        if self.Agent:
            agent = " -A"
        else:
            agent = ""

        if self.Dynamic:
            dynamic = " -D " + self.Dynamic + " "
        else:
            dynamic = ""

        if self.Local:
            local = "-L " + self.Dynamic + ":127.0.0.1:" + self.Local + " "
        else:
            local = ""

        if self.quiet:
            quiet = "-q"
        else:
            quiet = ""

        timeout = " -o ConnectTimeout=" + str(self.timeout) + " "

        args = agent + dynamic + local + quiet + timeout + self.login + "@" + instances[choice][2]
        print ("Args: %s" % args)

        try:
            retcode = subprocess.call("ssh " + args, shell=True)
            if retcode < 0:
                print("Child was terminated by signal", -retcode, file=sys.stderr)
            else:
                print("Child returned", retcode, file=sys.stderr)
        except OSError as e:
            print("Execution failed:", e, file=sys.stderr)

client = sshe()
