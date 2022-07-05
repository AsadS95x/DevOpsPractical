from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Houses
import requests
from datetime import date