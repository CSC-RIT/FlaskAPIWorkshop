import uuid
from flask import Blueprint, request, jsonify
from db import db, save_db

devices_bp = Blueprint('devices_bp', __name__)

def get_devices():
    # get all devices stored in db
    pass

def get_device(device_id):
    # check if device with id exists in database

    # return it if so
    pass

def create_device():
    # verify that the request gave us a name, status, and room_id

    # verify that the room_id exists in our database

    # create a dictionary of the new device, with a unique id

    # add the device to the list of devices

    # return the new device in our request
    pass

def update_device_status(device_id):
    # verify that the request gave us a status

    # verify that the device with device_id exists in our dictionary

    # update the device status with the given status

    # return the entire updated device
    pass

def delete_device(device_id):
    # verify that the device with device_id exists

    # remove the device from the db, can be done by:
    # - .remove on the devices list (with the entire dictionary object)
    # - rebuilding the list without the excluded device

    # return that we have deleted the device
    pass
