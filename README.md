ollis_python_excercise
======================

Simple web page monitor in Python

## Requirements

* python 2.7
* [requests http library](http://docs.python-requests.org/en/latest/)

```
pip install requests
```

## Usage

```
git clone https://github.com/ollijm/ollis_python_excercise.git
cd ollis_python_excercise
python src/main.py 30
```

> Webserver available at: localhost:8080

## About the software

I decided to write this small piece in Python despite the fact that I am not very experienced with it. I hope this is to show my ability to grab things quickly if needed. Also I know dynamic languages are very good for this kind of prototyping. However, there are probably some not so good practices to be seen in my code if looked at by a more seasoned Python programmer.

Of course the feature set in such a quickly written software is very limited. I would have liked to give a quite a lot more abstraction to the way the Web page content requirements are handled. Also there’s no scalability in this single-threaded application to handle a long list of URLs. In most cases I just wanted to do the simplest thing that would work.

In terms of having this web monitor to work in geographically distributed fashion, we would probably need a central API to send each web monitor’s statistics to. We would probably use SSL certificate to ensure we are talking to the authentic central API in secure manner. Also the central API might need to distribute API keys to each monitor application in order to identify and authorize its clients.
