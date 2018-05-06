 import click
  import urlparse
  import textrank
 from flask import Flask
 from flask import request
  @click.group()
  def cli():
      pass
  @cli.command()
  def initialize():
      """Download required nltk libraries."""
      textrank.setup_environment()
  @cli.command()
  @click.argument('filename')
  def extract_summary(filename):
      """Print summary text to stdout."""
      with open(filename) as f:
          summary = textrank.extract_sentences(f.read())
          print(summary)
  @cli.command()
  @click.argument('filename')
  def extract_phrases(filename):
      """Print key-phrases to stdout."""
      with open(filename) as f:
          phrases = textrank.extract_key_phrases(f.read())
          print(phrases)
  @cli.command()
  @click.argument('text')
  def get_suma(text):
      suma = textrank.extract_sentences(text)
  get_suma()
 app = Flask(_name_)
 @app.route("/")
 def hello():
 txt = request.args.get('txt')
get_suma(txt)
   print "lmao"
     print "nubz"
print("nubv")