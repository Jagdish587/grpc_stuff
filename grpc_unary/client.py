import grpc
import employee_pb2
import employee_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = employee_pb2_grpc.EmployeeServiceStub(channel)

        request = employee_pb2.EmployeeRequest(name="Alice", division="Engineering")
        try:
            response = stub.GetEmployeeInfo(request)
            print(f"Name: {response.name}")
            print(f"Division: {response.division}")
            print(f"Designation: {response.designation}")
            print(f"Floor: {response.floor}")
        except grpc.RpcError as e:
            print(f"Error: {e.code().name}, {e.details()}")

if __name__ == '__main__':
    run()

