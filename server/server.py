from flask import Flask, jsonify, render_template, redirect, request, session, flash, Response
# # from food_model import db, connect_to_db, Food, Food_record, Record, User
# from datetime import datetime
# import pytz
# from flask_cors import CORS
# # import trie
import time

app = Flask(__name__)
# app.secret_key = 'SOMEKEY'


@app.route('/')
def get_current_time():
    return {'time': time.time()}
