#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Create MyNode node inherriting from Node
class MyNode(Node):
  def __init__(self):
    # Initalize node and define node name
    super().__init__("first_node")
    # Add additional functionality, such as logging hello
    self.get_logger().info("HELLO QADT")

def main *args-None):
  # Initilize ros2 coms
  rclpy.init(args=args)
  # Create the node
  node = MyNode()
  # Shutdown ros2 coms
  rclpy.shutdown()

# Standard python convention for executable files
if __name__ == '__main__':
  main()

