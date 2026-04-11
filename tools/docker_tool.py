import subprocess


def build_docker():

    subprocess.run("docker build -t ml-agent .",shell=True)