import win32evtlog
import xmltodict
#eventvwr.msc
def SearchEvents(LogName, EventId, count=20):
    EventLog = win32evtlog.EvtOpenLog(LogName, 1, None)

    #totalRecords = win32evtlog.EvtGetLogInfo(EventLog, win32evtlog.EvtLogNumberOfLogRecords)[0]
    ResultSet = win32evtlog.EvtQuery(LogName, win32evtlog.EvtQueryReverseDirection, "*[System[(EventID=%d)]]" % EventId, None)

    EventList = []
    for evt in win32evtlog.EvtNext(ResultSet, count):
        res = xmltodict.parse(win32evtlog.EvtRender(evt, 1))
        #took attention in events like 8. Take in mind CreateRemoteThread
        # 11 are related to files created, here we're looking for Ryuk ransom note
        eventid = int(res["Event"]["System"]["EventID"])
        if eventid in [8,11]:
            EventData = {}
            for e in res['Event']['EventData']['Data']:
                if '#text' in e:
                    EventData[e['@Name']] = e['#text']

        EventList.append(EventData)

    return EventList

for i in [8,11]:
    try:
        Events = SearchEvents('Microsoft-Windows-Sysmon/Operational', i)
        print(Events)
        print()
    except:
        pass
