from flask import Flask, flash, redirect, render_template, request, session, abort
 
import sys
import spotipy
import spotipy.util as util

import random

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('input.html')