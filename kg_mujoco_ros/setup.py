from setuptools import setup

PACKAGE_NAME = 'kg_mujoco_ros'

setup(
    name=PACKAGE_NAME,
    version='0.0.0',
    data_files=[
        ('share/' + PACKAGE_NAME, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Victor',
    maintainer_email='victor.drobizov@gmail.com',
    description='Mujoco ROS2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
          'mujoco_control = kg_mujoco_ros.main:main'
        ],
    },
)
