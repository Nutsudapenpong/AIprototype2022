import argparse #สำหรับ รับ input จ ากภายนอก
import subprocess #สำหรับ รัน terminal command

#import flask #สำหรับทำ web app และ webservice API


def print_other():
    print('something else')

def parse_input():
    parser = argparse.ArgumentParser(description='test program to learn about argparse and subprocess')
    parser.add_argument(
        'm',
        type=int,
        help='value of m positional argument')
                        
    parser.add_argument(
        '--x',
        type=int,
        help='value of x')

    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')
                                
    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = parse_input()
    x = args.x
    y = args.yval

    print(f'M = {args.m}')
    print(f'calculate {x} x {y} = {x*y}')
