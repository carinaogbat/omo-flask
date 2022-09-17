"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page.
    You can enter the site and get compliments <a href="http://localhost:5000/hello"> here. </a>
    <div>
    Or if you're feeling moody you can find insults 
    <a href="http://localhost:5000/diss"> here. </a>
    </div>
    </html>"""


@app.route('/diss')
def insult():
  """Insults user and prompts for name"""

  return """<!doctype html> 
  <html>
  Wow you are really ugly! What is your name?
  <div>
  <form action="/insult">
  <input type="text" name="person">
  <label Input Name>
  <div>
  <label for="insult"> What insult would you like to choose? </label>
    <select name="insult" id="selected_insult">
    <option value="dumb"> Dumb </option>
    <option value="out_of_shape"> Out of shape </option>
    <option value="funny_looking"> Funny looking </option>
    </select>
  </div>
  <input type="Submit" value="Submit">
  </form>
  </div>
   </html>"""

@app.route('/insult')
def create_insult():
    """Insults user by name"""
    user = request.args.get("person")
    insult = request.args.get("insult")

    return """<!doctype html>
  <html>
  <h1>An Insult:</h1>
  <body>
  Wow {user} not only are you ugly, you are {insult}!
  </body>
  </html>
  """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
        <div>
        <div>
          Pick a compliment below:
        </div>
          <input type="radio" name="compliment" value="amazing" id="amazing">
          <label for="amazing">Amazing</label>
          <input type="radio" name="compliment" value="great" id="great>
          <label for="Great">Great</label>
          <input type="radio" name="compliment" value="fantastic" id="fantastic">
          <label for="Fantastic">Fantastic</label>
        </div>
          <input type="submit" value="Submit">

        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
