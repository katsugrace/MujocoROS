#!/usr/bin/env python

from rclpy.node import Node


class MujocoRos(Node):
    NODE_NAME = 'mujoco'

    def __init__(self):
        super().__init__(MujocoRos.NODE_NAME)
