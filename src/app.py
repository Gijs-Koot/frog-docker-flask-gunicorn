from flask import Flask, jsonify, request
import frog
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

frog = frog.Frog(frog.FrogOptions(parser=False), "/etc/frog/frog.cfg")

@app.route('/ping')
def ping():

    app.logger.info("Logger is working.")
    return jsonify({
        "message": "Hi!"
    })

@app.route('/frog')
def frog_process():

    text = request.json["text"] if request.json and "text" in request.json else request.args.get('text', '')
    if not text:
        return jsonify({
            "message": "You must include a text as GET parameter or in the body."
        }), 400

    app.logger.debug("Analyzing text ..")
    app.logger.debug(text.replace('\n', ' '))

    return jsonify({
        "response": frog.process(text),
        "text": text
    })

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080")
