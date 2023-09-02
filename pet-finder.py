import requests
import os

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

app = Flask(__name__)


@app.get("/animals")
def show_book_info():
    """Return info about animals"""
    headers = {'Authorization': f"Bearer {"Oauth"}"}

    resp = requests.get("https://api.petfinder.com/v2/animals",
    params={"limit": 100})
    header=headers

    pet_data = resp.json()
    # using the APIs JSON data, render full HTML page
    return render_template("", )