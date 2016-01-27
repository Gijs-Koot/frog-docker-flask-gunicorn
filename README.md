# frog-docker-flask-gunicorn
A flask / Docker wrapper around the NLP library [Frog](http://languagemachines.github.io/frog/), based on [LaMachine](https://github.com/proycon/LaMachine).

## Disclaimer

There is a server included with [Frog](http://languagemachines.github.io/frog/), which should work on it's own, but a had an [issue](https://github.com/proycon/LaMachine/issues/4) with it. This setup comes with the added benefit of an `HTTP / json` interface. The original server is probably much more efficient, and the base Docker image we use here is also not very small, because you can do a lot more with it.

## Usage

You need `docker-compose` and `docker`. You can start the server with

    docker-compose up

and send a text encoded as "text" in a `json` body. Using `httpie` for example, see below.

    $ cat test.json
    {
      "text": "Dit is een test."
    }

    $ http GET 'dockerhost:8080/frog' @test.json

Or as `GET` parameter:

    $ http '<dockerhost>:8080/frog?text=Dit is een test.'
    HTTP/1.1 200 OK
    Connection: close
    Content-Length: 1084
    Content-Type: application/json
    Date: Wed, 27 Jan 2016 13:21:23 GMT
    Server: gunicorn/19.4.5

    {
        "response": [
            {
                "chunker": "B-NP",
                "index": "1",
                "lemma": "dit",
                "morph": "[dit]",
                "ner": "O",
                "pos": "VNW(aanw,pron,stan,vol,3o,ev)",
                "posprob": 0.777085,
                "text": "Dit"
            },
            {
                "chunker": "B-VP",
                "index": "2",
                "lemma": "zijn",
                "morph": "[zijn]",
                "ner": "O",
                "pos": "WW(pv,tgw,ev)",
                "posprob": 0.999891,
                "text": "is"
            },
            {
                "chunker": "B-NP",
                [...]
                "posprob": 1.0,
                "text": "."
            }
        ],
        "text": "Dit is een test."
    }
