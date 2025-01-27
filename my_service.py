#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # We'll use this service type for simplicity

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.service = self.create_service(AddTwoInts, 'square_service', self.handle_request)
        self.get_logger().info('Square service is ready.')

    def handle_request(self, request, response):
        response.sum = request.a * request.a
        self.get_logger().info(f'Received request: {request.a}. Responding with: {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SquareService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
