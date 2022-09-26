import logging
import os
import re
import requests
import asyncio
import time
from flask import Flask, Blueprint, make_response, request, render_template
from flask_apscheduler import APScheduler
from flask_restful import Api, Resource
from flask_wtf.csrf import CSRFProtect
from flask_paginate import Pagination, get_page_args
from datetime import date, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
from dotenv import load_dotenv

load_dotenv()


# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    WTF_CSRF_ENABLED = False


# Logging Setup
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

DATABASE_STRING = os.getenv("DATABASE_STRING")
client = MongoClient(DATABASE_STRING)

app = Flask(__name__)
app.config.from_object(Config())

csrf = CSRFProtect()
csrf.init_app(app)

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()
