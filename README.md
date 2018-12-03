# sshe
Utility lists the available EC2 Linux instances in the specified region and prompts you to choose one to connect to. If no region is specified, it will attempt to find the region from the current session.

You can also specify which user to connect as, enable dynamic port forwarding, forward your ssh agent and a custom timeout for the initial connection attempt.

There are similar utilities available online but I wanted to be able to pass options to the SSH client.

## Installation
You can install sshe using the install script. Example:
```
python3 setup.py install
Warning: 'classifiers' should be a list, got type 'tuple'
/usr/local/lib/python3.7/site-packages/setuptools/dist.py:470: UserWarning: Normalizing '0.1dev' to '0.1.dev0'
  normalized_version,
running install
running bdist_egg
running egg_info
writing sshe.egg-info/PKG-INFO
writing dependency_links to sshe.egg-info/dependency_links.txt
...
...
Using /usr/local/lib/python3.7/site-packages
Searching for six==1.11.0
Best match: six 1.11.0
Adding six 1.11.0 to easy-install.pth file

Using /usr/local/lib/python3.7/site-packages
Finished processing dependencies for sshe==0.1.dev0
```

## Usage
```
sshe -h
usage: sshe [-h] [-Agent] [-Dynamic DYNAMIC] [-Local LOCAL] [-login LOGIN]
            [-quiet] [-region REGION] [-timeout TIMEOUT]

optional arguments:
  -h, --help        show this help message and exit
  -Agent            Enables forwarding of the authentication agent connection.
  -Dynamic DYNAMIC  Specifies local 'dynamic' application-level port
                    forwarding.
  -Local LOCAL      Specifies a local port to forward to the remote server.
  -login LOGIN      The username you want to connect with.The default is
                    ec2-user
  -quiet            Hide all SSH error messages
  -region REGION    Which region is the instance in?
  -timeout TIMEOUT  How many seconds do you want to wait?The default is 10
                    seconds.
```
