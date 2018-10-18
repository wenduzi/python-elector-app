import os
import time
import urllib.request


def printrole():
    if determinemaster():
        print("I am the master,pod name is %s" % (os.environ["HOSTNAME"]))
    else:
        print("This node is not the cluster leader so won't execute the job")


def determinemaster():
    mypodname = os.environ["HOSTNAME"]
    with urllib.request.urlopen('http://localhost:4040') as response:
        html = response.read()
        leaderpodname = html.split()
        print(html)
    return mypodname == leaderpodname


def main():
    while True:
        time.sleep(5)
        printrole()

if __name__ == "__main__":
    main()
