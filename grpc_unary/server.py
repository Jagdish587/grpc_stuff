from concurrent import futures
import grpc
import employee_pb2
import employee_pb2_grpc

# Sample database
EMPLOYEE_DB = {
    ("Alice", "Engineering"): {"designation": "Software Engineer", "floor": "5"},
    ("Bob", "HR"): {"designation": "HR Manager", "floor": "2"},
    ("Charlie", "Finance"): {"designation": "Accountant", "floor": "3"},
}

class EmployeeService(employee_pb2_grpc.EmployeeServiceServicer):
    def GetEmployeeInfo(self, request, context):
        key = (request.name, request.division)
        record = EMPLOYEE_DB.get(key)
        if record:
            return employee_pb2.EmployeeResponse(
                name=request.name,
                division=request.division,
                designation=record["designation"],
                floor=record["floor"]
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Employee not found')
            return employee_pb2.EmployeeResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    employee_pb2_grpc.add_EmployeeServiceServicer_to_server(EmployeeService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

