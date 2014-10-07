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

# Start the monitor with 30 second poll interval
python src/main.py 30
```

Webserver available at http://localhost:8080/

For changing the web page requirement list, edit `./src/urls.py`

Each request and the content test result is logged at `./request.log`

## About the software

I decided to write this small piece in Python despite the fact that I am not very experienced with it. I hope this is to show my ability to grab things quickly if needed. Also I know dynamic languages are very good for this kind of prototyping. However, there are probably some not-so-great practices to be seen in my code if looked at by a more seasoned Python programmer.

In most aspects I have done the simplest thing that would work. For the content check, I chose to test only HTTP status code and that Content-Type header starts correctly. Instead of having a separate configuration file with possible character escape issues, I chose to have configuration as python code at this point. There is no validation at the configuration content. Test requirement expectations and results are poorly encapsulated into WebPage class and this would require much abstraction to ever make it extensible. Also there’s no scalability in this single-threaded application to handle a long list of URLs for example. Scheduler is not smart because if the interval is exceeded while reading the web pages, the software start to fall behind schedule.

For such a small software I did not find it reasonable to start splitting it into different modules because file level separation seemed enough. There are no unit tests. 

In terms of having this web monitor to work in geographically distributed fashion, we would probably need a central API to send each web monitor’s statistics to. We would probably use SSL certificate to ensure we are talking to the authentic central API in secure manner. Also the central API might need to distribute API keys to each monitor application in order to identify and authorize its clients.
