import time
import grpc
from concurrent import futures
import streaming_pb2
import streaming_pb2_grpc

class LogService(streaming_pb2_grpc.LogServiceServicer):
    def StreamLogs(self, request, context):
        print(f"Streaming logs for process: {request.process_name}")
        for i in range(1, 11):  # Simulate 10 log entries
            log = streaming_pb2.LogEntry(
                message=f"{request.process_name} log entry #{i}",
                line_number=i
            )
            yield log
            time.sleep(0.5)  # simulate delay

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_LogServiceServicer_to_server(LogService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server started on port 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

