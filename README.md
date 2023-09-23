# Recipe Finder

## What does it do? 
This web application, using Python and Flask, allows you to enter one or more ingredients and search for recipes containing them. In the results, you can then see how to make it from start to finish and video demonstrations. 

## Usage
1. Install Python packages mentioned in the [requirements.txt](requirements.txt) file to meet the required imports in `main.py`.
2. Run the `python main.py` from within the folder to start the Flask web server application and a similar output should be displayed:
```terminal
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
3. Access web application via browser address as shown in terminal window.

### Requirements
The following packages are required for this script to work.
- Flask
- requests

To install these packages, you can simply run: `pip install -r requirements.txt`
