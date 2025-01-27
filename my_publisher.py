#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Float64, 'number_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_number)  # Publish every second
        self.number = 0.0

    def publish_number(self):
        msg = Float64()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.number += 1.0

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
