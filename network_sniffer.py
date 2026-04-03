from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        # Determine the protocol name
        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        print(f"[{protocol_name}] {src_ip} -> {dst_ip}")

        # If there is a payload, display a snippet of it
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet.payload)
            if payload:
                print(f"   Payload Snippet: {payload[:50].hex()}...")

def main():
    print("Starting Network Sniffer... Press Ctrl+C to stop.")
    # sniff() captures packets. 'prn' refers to the function to call for each packet.
    # 'store=0' prevents memory buildup by not saving every packet in RAM.
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()