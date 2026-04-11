import subprocess


def install(package):

    subprocess.run(f"pip install {package}",shell=True)