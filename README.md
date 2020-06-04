# Github Pins Scraper 🛠️

### Why this program? 🤠

I build this program because the Github API does not provide a user pinned repositories name, description and main language used.

### External libraries used. 📚

[Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

### How does it work? ⚙️

It uses Beautiful Soup to web scrape a users profile, fetching data and storing it in a JSON file. Just as an API. To update the JSON you should run the script again.

### Installation 📲

Install the dependecies in the requirements

`user@hostname git clone https://github.com/joaoofreitas/pinned-repositories-scraper.git`

`user@hostname pip3 install -r requirements.txt`

### Running the script 📟

To run the script just type

`user@hostname python3 scraper.py <user>`

>__NOTE:__ Replace <user> with your github username.
