# Solution Link: https://leetcode.com/problems/implement-router/solutions/7209346/python-que-and-binary-search-solution-wi-blwi/

from collections import deque


class Router:
    def createPacketId(source: int, timestamp: int):
        return (timestamp << 20) + source

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packet_number = 0

        # packets[destination] = deque()
        self.packets = {}
        self.all_packets = deque()

        # packet_ids[destination] = set()
        self.packet_ids = {}

    def packetExist(self, source: int, destination: int, timestamp: int):
        packet_ids = self.packet_ids
        if destination in packet_ids:
            packet_id = Router.createPacketId(source, timestamp)
            return packet_id in packet_ids[destination]

        return False

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        limit = self.limit

        # 既に同じパケットがあるか
        if self.packetExist(source, destination, timestamp):
            return False

        # パケットが上限数に達しているので、FIFOに基づいて削除
        if self.packet_number == limit:
            self.forwardPacket()

        packets = self.packets
        all_packets = self.all_packets
        packet_ids = self.packet_ids

        if not (destination in packets):
            packets[destination] = deque()
        if not (destination in packet_ids):
            packet_ids[destination] = set()

        d_packets = packets[destination]
        d_packet = [source, timestamp]
        d_packets.append(d_packet)

        packet = [source, destination, timestamp]
        all_packets.append(packet)

        d_packet_ids = packet_ids[destination]
        packet_id = Router.createPacketId(source, timestamp)
        d_packet_ids.add(packet_id)

        self.packet_number += 1

        return True

    def forwardPacket(self) -> List[int]:
        if self.packet_number == 0:
            return []

        packets = self.packets
        all_packets = self.all_packets
        packet_ids = self.packet_ids

        rmv_packet = all_packets.popleft()
        rmv_src, rmv_dst, rmt_tsp = rmv_packet
        rmv_packet_id = Router.createPacketId(rmv_src, rmt_tsp)

        packets[rmv_dst].popleft()
        if len(packets[rmv_dst]) == 0:
            packets.pop(rmv_dst)

        packet_ids[rmv_dst].remove(rmv_packet_id)
        if len(packet_ids[rmv_dst]) == 0:
            packet_ids.pop(rmv_dst)

        self.packet_number -= 1

        return rmv_packet

    def startIndex(startTime: int, d_packets):
        if d_packets[-1][1] < startTime:
            return -1

        ok, ng = len(d_packets) - 1, -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if d_packets[mid][1] >= startTime:
                ok = mid
            else:
                ng = mid

        return ok

    def endIndex(endTime: int, d_packets):
        if endTime < d_packets[0][1]:
            return -1

        ok, ng = 0, len(d_packets)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if d_packets[mid][1] <= endTime:
                ok = mid
            else:
                ng = mid

        return ok

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.packets
        if not (destination in packets):
            return 0

        d_packets = packets[destination]
        s_idx = Router.startIndex(startTime, d_packets)
        if s_idx == -1:
            return 0

        e_idx = Router.endIndex(endTime, d_packets)
        if e_idx == -1:
            return 0

        return e_idx - s_idx + 1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
