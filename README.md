ollis_python_excercise
======================

Simple web page monitor in Python

## Requirements

* python 2.7
* requests http library - http://docs.python-requests.org/en/latest/

```
pip install requests
```

## Usage

```
git clone https://github.com/ollijm/ollis_python_excercise.git
cd ollis_python_excercise
python src/main.py 30
```

Webserver available at http://localhost:8080/

For changing the web page requirement list, edit `src/urls.py`

## About the software

I decided to write this small piece in Python despite the fact that I am not very experienced with it. I hope this is to show my ability to grab things quickly if needed. Also I know dynamic languages are very good for this kind of prototyping. However, there are probably some not-so-great practices to be seen in my code if looked at by a more seasoned Python programmer.

Of course the feature set in such a quickly written software is very limited. For the content check, I chose to test only HTTP status code and that Content-Type header starts correctly. Instead of having a separate configuration file with possible character escape issues, I chose to have configuration as python code at this point. There is no validation at the configuration content. Test requirement expectations and results are poorly encapsulated into WebPage class and this would require much abstraction to ever make it extensible. Also there’s no scalability in this single-threaded application to handle a long list of URLs for example. There are no unit tests. In most aspects I have done the simplest thing that would work.

In terms of having this web monitor to work in geographically distributed fashion, we would probably need a central API to send each web monitor’s statistics to. We would probably use SSL certificate to ensure we are talking to the authentic central API in secure manner. Also the central API might need to distribute API keys to each monitor application in order to identify and authorize its clients.
