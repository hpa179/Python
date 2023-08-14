Name: Harita Agarwal
V Number: V01002060

Steps:
You need to run the PINGServer.py program before you run the PINGClient.py

How to compile the PINGServer
Login into the terminal using ssh -l <eID> 172.18.233.74
Once you are inside the terminal successfully and see the machine "egr-v-cmsc440-1"
Open another terminal and type ssh 10.0.0.3
Enter your password
When you see sftp> type "python3 PINGServer.py <IP> <Port>"
For example: python3 PINGServer.py 10501 30

How to compile the PINGClient
Open a another terminal that will run parallel to the PINGServer
Login into the terminal using ssh -l <eID> 172.18.233.74
Once you are inside the terminal successfully and see the machine "egr-v-cmsc440-1"
Open another terminal and type ssh 10.0.0.2
Enter your password
When you see sftp> "python3 PINGClient.py <IP> <Port> <ClientID> <No. of Packets> <Wait Time>"
For example: python3 PINGCLient.py 172.18.233.74 10501 3333 100 2

**Make sure the IP Address is the same as the one server generated and the port number is also same as the server**