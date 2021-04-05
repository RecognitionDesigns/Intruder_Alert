#!/usr/bin/env python3

import http.client, urllib
import anki_vector
from anki_vector.util import degrees, Angle, Pose
from anki_vector.events import Events
import time
import requests
from keys import (token, user)

n = 0

def count(n):
    while n < 5:
        if robot.status.is_picked_up or robot.status.is_cliff_detected:
            print("Vector might be stuck!")
            print(n)
            n = n+1
            time.sleep(3)

        else:
            n = 0
            time.sleep(2)

    print("Vector is stuck!")
    robot.conn.request_control()
    image = robot.camera.capture_single_image()

    image.raw_image.save('stuck_pic.jpeg', 'JPEG')

    alert_message = ("Vector is stuck!")

    r = requests.post("https://api.pushover.net/1/messages.json", data = {
      "token": token,
      "user": user,
      "message": (alert_message)
    },
    files = {
      "attachment": ("image.jpg", open("stuck_pic.jpeg", "rb"), "image/jpeg")
    })
    print("Sending alert...")

    n = 0

    while True:
        time.sleep(10)
        if robot.status.is_picked_up or robot.status.is_cliff_detected:
            time.sleep(1)
        else:
            count(n)

def test_subscriber(robot, event_type, event):
#    print(f"Subscriber called for: {event_type} = {event}")

    for face in robot.world.visible_faces:
        print("I see a face")
        if face.name == '[ENTER NAME1 HERE]':
            print(f"Face name: {face.name}")
            robot.conn.request_control()
            robot.behavior.say_text(f"whats up : {face.name}?")
            time.sleep(2)
            robot.conn.release_control()

        if face.name == '[ENTER NAME2 HERE]':
            print(f"Face name: {face.name}")
            robot.conn.request_control()
            robot.behavior.say_text(f"Good Evening : {face.name}!")
            time.sleep(2)
            robot.conn.release_control()

        if face.name != '[ENTER NAME1 HERE]' or face.name != '[ENTER NAME2 HERE]':
            robot.conn.request_control()
            robot.behavior.set_head_angle(degrees(25.0))
            robot.behavior.set_lift_height(0.0)
            unknown_face = robot.camera.capture_single_image()
            robot.behavior.say_text("Unknown person detected! sending alert notification!")
            unknown_face.raw_image.save('unknown_face.jpeg', 'JPEG')
            alert_message = ("Unknown person detected!")

            r = requests.post("https://api.pushover.net/1/messages.json", data = {
              "token": token,
              "user": user,
              "message": (alert_message)
            },
            files = {
              "attachment": ("image.jpg", open("unknown_face.jpeg", "rb"), "image/jpeg")
            })
            print("Sending alert...")

            time.sleep(10)
            robot.conn.release_control()

with anki_vector.Robot(behavior_control_level=None, enable_face_detection=True) as robot:
    robot.events.subscribe(test_subscriber, Events.robot_changed_observed_face_id)
    robot.events.subscribe(test_subscriber, Events.robot_observed_face)
    print("Intruder alert program active!")
    count(n)
