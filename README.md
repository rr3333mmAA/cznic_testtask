# Solved Test Task

# Python

## Requirements

- Python 3.7 to 3.10
- Linux OS support
- gRPC and REST APIs

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-client-cli.git
cd file-client-cli
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Compile the gRPC protocol buffer file:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_file.proto
```

## Usage 
```bash
file-client [options] stat UUID
file-client [options] read UUID
file-client --help
```


# SQL

All the SQL queries are in the `sql` directory in separate files :)
