import sys
import time
import subprocess
from subprocess import Popen

from py4j.java_gateway import JavaGateway, Py4JNetworkError

try:
    cmd = "java -jar J4Py.jar"
    proc = Popen(cmd, shell=True)
    print("process id = %s" % proc.pid, file=sys.stderr)

    gateway = JavaGateway()

    assert proc.poll() is None

    while True:
        try:
            # ping 的な処理
            gateway._gateway_client._get_connection()
            break
        except Py4JNetworkError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

    ex = gateway.jvm.org.kuryu.PDFExtractText

    with open("all.pdf", "rb") as fp:
        text = ex.convert(fp.read())

    print(text)
finally:
    proc.terminate()

proc.wait()

assert proc.poll() is not None
