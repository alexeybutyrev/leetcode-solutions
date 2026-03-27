# Problem: Design Log Storage System
# Language: python3
# Runtime: 175 ms
# Memory: 20.2 MB

from datetime import datetime, timedelta
from sortedcontainers import SortedList

def parse_with_granularity(ts_string, granularity):
    # Map granularity to the number of segments to keep
    # 2017 : 01 : 01 : 23 : 59 : 59
    # (1)  : (2): (3): (4): (5): (6)
    levels = {
        "year": 1,
        "month": 2,
        "day": 3,
        "hour": 4,
        "minute": 5,
        "second": 6
    }
    
    # Full format parts
    format_parts = ["%Y", "%m", "%d", "%H", "%M", "%S"]
    
    count = levels.get(granularity.lower(), 6)
    
    # Slice both the input string and the format string to match
    str_limited = ":".join(ts_string.split(":")[:count])
    fmt_limited = ":".join(format_parts[:count])
    
    return datetime.strptime(str_limited, fmt_limited)

class LogSystem:

    def __init__(self):
        self.A = SortedList()
        self.mp = {}

    def put(self, id: int, timestamp: str) -> None:
        ts = datetime.strptime(timestamp, "%Y:%m:%d:%H:%M:%S")
        self.mp[ts] =  timestamp
        self.A.add((ts, id))
    
    def convert(self, ts, granularity, lower = True):
        if lower:
            if granularity == "Year":
                # Round to Year
                ts = ts.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            elif granularity == "Month":
                # Round to Day
                ts = ts.replace(hour=0, minute=0, second=0, microsecond=0)
            elif granularity == "Month":
                # Round to Minute
                ts = ts.replace(second=0, microsecond=0)
        else:
            # Round UP to Minute
            # Truncate seconds, then add 1 minute
            ts = ts.replace(second=0, microsecond=0) + timedelta(minutes=1)

            # Round UP to Hour
            ts = ts.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)

            # Round UP to Day
            ts = ts.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        return ts
    
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start_ts = parse_with_granularity(start, granularity)
        end_ts = parse_with_granularity(end, granularity)
        ans = []
        for ts, id in self.A:
            ts =  parse_with_granularity(self.mp[ts], granularity)
            if start_ts <= ts <= end_ts:
                ans.append(id)
        return ans

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)