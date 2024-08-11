#!/usr/bin/env python3

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # Launch the publisher node
        launch_ros.actions.Node(
            package='pkg1',  # Replace with your package name
            executable='pub.py',  # Name of the executable for the publisher
            name='my_publisher',
            output='screen'),

        # Launch the subscriber node
        launch_ros.actions.Node(
            package='pkg1',  # Replace with your package name
            executable='sub.py',  # Name of the executable for the subscriber
            name='my_subscriber',
            output='screen'),
    ])

