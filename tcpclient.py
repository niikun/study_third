import socket

class TCPClient:
    """
    TCP通信を行うクライアントを表すクラス
    """

    def request(self):
        """
        サーバーへリクエストを送信する
        """

        print("=== クライアントを起動します ===")

        try:
            # socket を生成
            client_socket = socket.socket()
            client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

            # サーバーに接続
            print("=== サーバーに接続します ===")
            client_socket.connect(("127.0.0.1", 80))
            print("=== サーバーに接続しました ===")

            with open("client_send.txt","rb") as f:
                request = f.read()
            
            # サーバーにデータを送信
            client_socket.send(request)

            response = client_socket.recv(4096)

            with open("client_recv.txt","wb") as f:
                f.write(response)

            client_socket.close()

        finally:
            print("=== クライアントを停止します ===")

if __name__=="__main__":
    client = TCPClient()
    client.request()

            