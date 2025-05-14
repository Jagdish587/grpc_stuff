📁 Directory Structure


├── proto/
│   └── streaming.proto         # gRPC service definition
├── generated/
│   ├── streaming_pb2.py
│   └── streaming_pb2_grpc.py   # Generated gRPC Python code
├── server/
│   └── server.py               # Server implementation
└── client/
    └── client.py               # Client implementation

🔌 Requirements
Install dependencies on both machines:

pip3 install grpcio grpcio-tools



🖥️ Server Setup (Machine A)
✅ Required Files:
streaming.proto

streaming_pb2.py

streaming_pb2_grpc.py

server.py

🚀 Run Instructions:

(Optional) Generate gRPC code:

python -m grpc_tools.protoc -I=./proto --python_out=./generated --grpc_python_out=./generated ./proto/streaming.proto

Run the server:

python server.py

Ensure the gRPC port (default: 50052) is open for inbound traffic.

🧑‍💻 Client Setup (Machine B)

streaming_pb2.py ← copy from server or regenerate

streaming_pb2_grpc.py ← copy from server or regenerate

python client.py



🔁 Summary Table
File	Contains	Used By	Purpose

streaming_pb2.py	Message classes (message)	Client & Server	Define structure of request/response

streaming_pb2_grpc.py	RPC service stubs (service)	Client & Server	Define service interface and stub calls