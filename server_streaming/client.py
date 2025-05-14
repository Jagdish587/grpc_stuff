import grpc
import streaming_pb2
import streaming_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = streaming_pb2_grpc.LogServiceStub(channel)
        request = streaming_pb2.LogRequest(process_name="SensorReader")

        responses = stub.StreamLogs(request)
        for log_entry in responses:
            print(f"[{log_entry.line_number}] {log_entry.message}")

if __name__ == '__main__':
    run()
