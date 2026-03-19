import uuid
from flask import Blueprint, request, jsonify
from db import db, save_db

rooms_bp = Blueprint('rooms_bp', __name__)

def get_rooms():
    # get all rooms stored in db
    pass

def get_room(room_id):
    # check if room exists

    # get devices belonging to room
    pass

def create_room():
    # verify name header is in request

    # create new room dictionary

    # add it to db
    pass