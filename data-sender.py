#!/usr/bin/env python3

import random
import time
from datetime import datetime
import argparse
import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv


def write_points_to_influxdb(token, url, org, bucket, num_points, interval):
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    field1 = 50.0
    field2 = 50.0
    field3 = 50.0

    for i in range(num_points):
        point = Point("stat")\
            .tag("unit", "temperature")\
            .field("field1", field1)\
            .field("field2", field2)\
            .field("field3", field3)\
            .time(datetime.utcnow())

        try:
            write_api.write(bucket, org, point)
        except Exception as e:
            print(f"Error writing point: {e}")

        field1 += random.randint(-100, 100) / 10
        field2 += random.randint(-100, 100) / 10
        field3 += random.randint(-100, 100) / 10

        time.sleep(interval)


if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("INFLUXDB_TOKEN")

    if not token:
        raise ValueError(
            "InfluxDB token not found in the environment. Please set it in the .env file.")

    parser = argparse.ArgumentParser(
        description='Write random data points to InfluxDB.')
    parser.add_argument(
        '--url',
        default='http://localhost:8086',
        help='InfluxDB URL (default: http://localhost:8086)')
    parser.add_argument(
        '--org',
        default='organization',
        help='InfluxDB organization')
    parser.add_argument('--bucket', default='bucket', help='InfluxDB bucket')
    parser.add_argument(
        '--num_points',
        type=int,
        default=180,
        help='Number of points to write (default: 180)')
    parser.add_argument(
        '--interval',
        type=int,
        default=1,
        help='Interval between writes in seconds (default: 10)')

    args = parser.parse_args()

    write_points_to_influxdb(
        token,
        args.url,
        args.org,
        args.bucket,
        args.num_points,
        args.interval)
