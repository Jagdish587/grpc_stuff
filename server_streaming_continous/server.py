import time
import random
import grpc
from concurrent import futures
import streaming_pb2
import streaming_pb2_grpc

def is_daemon_alive():
    # Simulate daemon randomly dying (10% chance)
    return random.random() > 0.1

class LogService(streaming_pb2_grpc.LogServiceServicer):
    def StreamLogs(self, request, context):
        print(f"Client subscribed for: {request.process_name}")
        line = 1
        while True:
            if not is_daemon_alive():
                print("Daemon stopped. Ending stream.")
                context.set_code(grpc.StatusCode.UNAVAILABLE)
                context.set_details("Daemon not running.")
                return
            yield streaming_pb2.LogEntry(
                message=f"{request.process_name} log entry #{line}",
                line_number=line
            )
            line += 1
            time.sleep(0.5)  # Simulate delay/log arrival

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_LogServiceServicer_to_server(LogService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server started at port 50052.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

