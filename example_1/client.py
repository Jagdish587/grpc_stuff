import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        name_input = input("Enter your full name: ")
        request = helloworld_pb2.HelloRequest(user_full_name=name_input)
        response = stub.SayHello(request)
        print("Server response:", response.greeting_text)

if __name__ == '__main__':
    run()
