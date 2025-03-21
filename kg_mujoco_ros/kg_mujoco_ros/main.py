#!/usr/bin/env python

from kg_mujoco_ros.mujoco_ros import MujocoRos
import rclpy


def main(args=None):
    rclpy.init(args=args)
    mujoco = MujocoRos()
    rclpy.spin(mujoco)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
