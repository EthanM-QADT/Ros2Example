#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class SquareClient(Node):
    def __init__(self):
        super().__init__('square_client')
        self.client = self.create_client(AddTwoInts, 'square_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the service to be available...')
        self.get_logger().info('Service is available.')

    def send_request(self, number):
        request = AddTwoInts.Request()
        request.a = number
        request.b = 0  # Unused, as we're squaring `a`
        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    node = SquareClient()
    number_to_square = 5  # Replace with any number you want to square
    node.send_request(number_to_square)
    node.get_logger().info(f'Sent request to square {number_to_square}')

    rclpy.spin_until_future_complete(node, node.future)
    if node.future.result() is not None:
        response = node.future.result()
        node.get_logger().info(f'Received response: {response.sum}')
    else:
        node.get_logger().error('Service call failed.')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
