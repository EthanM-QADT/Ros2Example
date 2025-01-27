#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Create MyNode node inherriting from Node
class MyNode(Node):
  def __init__(self):
    # Initalize node and define node name
    super().__init__("first_node")
    # Add additional functionality, such as starting a timer callback (loop)
    self.counter_ = 0
    self.create_timer(1.0, self.timer_callback)
    self.get_logger().info("Node started")
  # Callback loop
  def timer_callback(self):
    self.get_logger().info("Hello " +str(self.counter_))
    self.counter_ +=1

def main *args-None):
  # Initilize ros2 coms
  rcply.init(args=args)
  # Create the node
  node = MyNode()
  # Constantly run the node
  rclpy.spin(node)
  # Shutdown ros2 coms
  rcply.shutdown()

# Standard python convention for executable files
if __name__ == '__main__':
  main()
