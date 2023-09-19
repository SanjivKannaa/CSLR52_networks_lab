import os
import matplotlib.pyplot as plt


PACKETSIZE = 1024
N = [5, 10, 15, 20, 25]
duration =100
for topology in ["bus", "mesh", "hybrid"]:
    packet_loss_list = []
    throughput_list = []
    for i in N:
        packet_received = 0
        packet_sent = 0
        os.system(f"ns {topology}.tcl {i} {PACKETSIZE}")
        with open(f"{topology}.nam", "r") as trace_file:
            for line in trace_file:
                if line[0] == "r":
                    packet_received += 1
                elif line[0] == "-":
            packet_sent += 1
            packet_loss = packet_sent - packet_received
            thr = packet_received / duration
            packet_loss_list.append(packet_loss)
            throughput_list.append(thr)
print(packet_loss_list)
print(throughput_list)
plt.figure(figsize=(8, 8))
plt.tight_layout()
plt.suptitle('Packet Loss and Throughput for ' + topology, fontsize=16)
# plt.title('Packet Loss and Throughput for ' + topology)
plt.subplot(211)
plt.plot(N, packet_loss_list, label=topology + " Packet Loss")
plt.ylabel("Packet Loss")
plt.subplot(212)
plt.plot(N, throughput_list, label=topology + " Throughput")
plt.xlabel("Number of Nodes")
plt.ylabel("Throughput")
plt.savefig(f"{topology}.jpg")