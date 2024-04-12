<h2>URLittle is a URL shortening service built with the Flask framework</h2>
For a live demo, you can visit <a href='https://www.urlittle.pp.ua'>www.urlittle.pp.ua</a>

## Building

Activate virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

But if you know Docker, then you can just:

    docker build -t urlittle .
    
## Using
Run:
    
    python main.py
    
if you are using Docker:

    docker run --rm -p 56733:56733 urlittle


Now you can access it in your web browser at http://localhost:56733.

![new](https://github.com/c45/urlittle/assets/60201776/f904765d-1cc3-4527-af73-8558d2d1a628)
![old](https://github.com/c45/urlittle/assets/60201776/9ed9f0b2-20f2-442a-8abb-2415558c0bd5)



