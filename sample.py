import sys
import time
import subprocess
from subprocess import Popen

from py4j.java_gateway import JavaGateway

try:
    cmd = "java -jar J4Py.jar"
    proc = Popen(cmd, shell=True)
    print("process id = %s" % proc.pid, file=sys.stderr)

    gateway = JavaGateway()

    while True:
        try:
            # ping 的な処理ないのかな
            print(gateway.jvm.org.kuryu.PDFExtractText, file=sys.stderr)
            break
        except Exception as e:
            time.sleep(1)
            print("waiting for jvm is ready", file=sys.stderr)

    ex = gateway.jvm.org.kuryu.PDFExtractText

    with open("all.pdf", "rb") as fp:
        text = ex.convert(fp.read())

    print(text)
finally:
    proc.terminate()
