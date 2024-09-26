import argparse
import sys
import grpc
import requests
from service_file_pb2 import StatRequest, ReadRequest, Uuid
import service_file_pb2_grpc


def grpc_stat(grpc_server, uuid):
    with grpc.insecure_channel(grpc_server) as channel:
        client = service_file_pb2_grpc.FileStub(channel)
        request = StatRequest(uuid=Uuid(value=uuid))
        response = client.stat(request)
        return response.data


def grpc_read(grpc_server, uuid):
    with grpc.insecure_channel(grpc_server) as channel:
        client = service_file_pb2_grpc.FileStub(channel)
        request = ReadRequest(uuid=Uuid(value=uuid), size=0)
        file_content = b""
        for response in client.read(request):
            file_content += response.data.data
        return file_content


def rest_stat(base_url, uuid):
    url = f"{base_url}/file/{uuid}/stat/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def rest_read(base_url, uuid):
    url = f"{base_url}/file/{uuid}/read/"
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def main():
    parser = argparse.ArgumentParser(description="File Client CLI")
    parser.add_argument("command", choices=["stat", "read"], help="Command to execute")
    parser.add_argument("uuid", help="File UUID")
    parser.add_argument("--backend", choices=["grpc", "rest"], default="grpc", help="Backend to use")
    parser.add_argument("--grpc-server", default="localhost:50051", help="gRPC server address")
    parser.add_argument("--base-url", default="http://localhost/", help="Base URL for REST server")
    parser.add_argument("--output", default="-", help="Output file")

    args = parser.parse_args()

    if args.command == "stat":
        if args.backend == "grpc":
            result = grpc_stat(args.grpc_server, args.uuid)
        else:
            result = rest_stat(args.base_url, args.uuid)
        print(result)

    elif args.command == "read":
        if args.backend == "grpc":
            result = grpc_read(args.grpc_server, args.uuid)
        else:
            result = rest_read(args.base_url, args.uuid)

        if args.output == "-":
            sys.stdout.buffer.write(result)
        else:
            with open(args.output, "wb") as f:
                f.write(result)


if __name__ == "__main__":
    main()
