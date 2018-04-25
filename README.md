py4j経由でpythonからapache pdfboxでテキストを抽出する。

# 構成

```
$ tree
.
├── J4Py.java
├── README.md
├── build.sh
├── manifest.mf
├── org
│   └── kuryu
│       └── PDFExtractText.java
├── pdfbox-app-2.0.8.jar
└── py4j0.10.6.jar -> /Users/kuryu/.pyenv/versions/anaconda3-5.0.1/share/py4j/py4j0.10.6.jar
```

# py4j setting

cf. https://qiita.com/arc279/items/5f547de8978a790e8523

```sh
$ pip show py4j
Name: py4j
Version: 0.10.6
Summary: Enables Python programs to dynamically access arbitrary Java objects
Home-page: https://www.py4j.org/
Author: Barthelemy Dagenais
Author-email: barthelemy@infobart.com
License: BSD License
Location: /Users/kuryu/.pyenv/versions/anaconda3-5.0.1/lib/python3.6/site-packages
Requires:
Required-by:

# pyenv使用の場合
$ python-config --exec-prefix
/Users/kuryu/.pyenv/versions/anaconda3-5.0.1

$ ln -s $(python-config --exec-prefix)/share/py4j/py4j0.10.6.jar .
```

# pdfbox 取得

```
wget -nc http://central.maven.org/maven2/org/apache/pdfbox/pdfbox-app/2.0.8/pdfbox-app-2.0.8.jar
```

# Java Gateway Server

## bulid

```sh
#!/bin/bash

javac org/kuryu/*.java -cp pdfbox-app-2.0.8.jar
jar cvf kuryu.jar org/kuryu/*.class

javac J4Py.java -cp py4j0.10.6.jar
jar cvfm J4Py.jar manifest.mf J4Py.class
```

## run

```sh
java -jar J4Py.jar
```

# python usage

## サンプルデータ取得

平成29年版 厚生労働白書

```
wget -nc http://www.mhlw.go.jp/wp/hakusyo/kousei/17/dl/all.pdf
```

## sample usage

```python
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()

ex = gateway.jvm.org.kuryu.PDFExtractText

with open("all.pdf", "rb") as fp:
  text = ex.convert(fp.read())

print(text)
```
