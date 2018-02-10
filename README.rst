sshe
==========

Utility lists the available EC2 Linux instances in the specified reqion and prompts you to choose one to connect to. If no region is specified, it will attempt to find the region from the current session.

You can also specify which user to connect as, enable dynamic port forwarding, forward your ssh agent and a custom timeout for the initial connection attempt.

There are similar utilities available online but I wanted to be able to pass options to the SSH client.

Installation
------------

You can install sshe using the install script. Example:

::

    sudo -H python setup.py install

Usage
-----

::

usage: sshe [-h] [-Agent] [-Dynamic DYNAMIC] [-login LOGIN] [-region REGION]
            [-timeout TIMEOUT]

optional arguments:
  -h, --help        show this help message and exit
  -Agent            Enables forwarding of the authentication agent connection.
  -Dynamic DYNAMIC  Specifies a local ``dynamic'' application-level port
                    forwarding.
  -login LOGIN      The username you want to connect with.The default is
                    ec2-user
  -region REGION    Which region is the instance in?
  -timeout TIMEOUT  How many seconds do you want to wait?The default is 10
                    seconds.
