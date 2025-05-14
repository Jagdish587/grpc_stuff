import time
import grpc
import streaming_pb2
import streaming_pb2_grpc

def run():
    while True:
        try:
            with grpc.insecure_channel('localhost:50052') as channel:
                stub = streaming_pb2_grpc.LogServiceStub(channel)
                request = streaming_pb2.LogRequest(process_name="sampleDaemon")

                print("Connected. Waiting for logs...")
                for log_entry in stub.StreamLogs(request):
                    print(f"[{log_entry.line_number}] {log_entry.message}")

        except grpc.RpcError as e:
            print(f"Stream error: {e.code().name} - {e.details()}")
            print("Reconnecting in 3 seconds...")
            time.sleep(3)

if __name__ == "__main__":
    run()

