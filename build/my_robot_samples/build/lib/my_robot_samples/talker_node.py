#!/usr/bin/env python3
import rclpy
from rclpy import node

def myTalkerNode(Node):
    
    def __init__(self):
        rclpy.__init__("talker_node")
        self.get_logger().info("Hello!")

def main(args=None):

    rclpy.init(args=args)
    node = myTalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()