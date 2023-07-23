import win32evtlog
import xmltodict
import json

#eventvwr.msc
RANSOM_NOTE = "RyukReadMe.txt"
PROCESS_CREATE = 1
NETWORK_CONNECT = 3
PROCESS_TERMINATED = 5
CREATE_REMOTE_THREAD = 8
FILE_CREATED = 11
REGISTRY_SET = 13
DNS_QUERY = 22
SYSMON_OPERATIONAL = 'Microsoft-Windows-Sysmon/Operational'

class MonitorSysmon:
    def __init__(self) -> None:
        pass

    def __searchEvents(self,LogName, EventId, count=20)->list:
        EventLog = win32evtlog.EvtOpenLog(LogName, 1, None)

        # Adjust the count parameter based on the total number of records
        total_records = win32evtlog.EvtGetLogInfo(EventLog, win32evtlog.EvtLogNumberOfLogRecords)[0]
        count = min(count, total_records)

        # Fetch events in descending order (most recent first)
        ResultSet = win32evtlog.EvtQuery(LogName, win32evtlog.EvtQueryReverseDirection, "*[System[(EventID=%d)]]" % EventId, None)

        EventList = []
        while len(EventList) < count:
            events = list(win32evtlog.EvtNext(ResultSet, count - len(EventList)))
            if not events:
                break

            for evt in events:
                res = xmltodict.parse(win32evtlog.EvtRender(evt, 1))
                #eventid = int(res["Event"]["System"]["EventID"])
                EventData = {}
                for e in res['Event']['EventData']['Data']:
                    if '#text' in e:
                        EventData[e['@Name']] = e['#text']

                EventList.append(EventData)
        return EventList

    def monitor_files_created(self,count=20)->list:
        pids = []
        Events = self.__searchEvents(SYSMON_OPERATIONAL, FILE_CREATED,count)
        for event in Events:
            if event["TargetFilename"].split(r"\\")[-1] == RANSOM_NOTE:
                process_name = event['Image'].split(r'\\')[-1]
                print(fr"Ryuk Process identified: {process_name}")
                pids.append(int(event["ProcessId"]))
        return pids

    def monitor_create_remote_thread(self)->list:
        pairs = []
        Events = self.__searchEvents(SYSMON_OPERATIONAL, CREATE_REMOTE_THREAD)
        for event in Events:
            pair_map = {}
            if event["StartFunction"] != 'CtrlRoutine':
                process_name = event['TargetImage'].split(r'\\')[-1]
                print(fr"Ryuk Process identified: {process_name}")
                pair_map["SourcePID"] = int(event['SourceProcessId'])
                pair_map["TargetPID"] = int(event['TargetProcessId'])
                pairs.append(pair_map)
        return pairs

    
