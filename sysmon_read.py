import win32evtlog
import xmltodict
#eventvwr.msc
def SearchEvents(LogName, EventId, count=1):
    EventLog = win32evtlog.EvtOpenLog(LogName, 1, None)

    #totalRecords = win32evtlog.EvtGetLogInfo(EventLog, win32evtlog.EvtLogNumberOfLogRecords)[0]
    ResultSet = win32evtlog.EvtQuery(LogName, win32evtlog.EvtQueryReverseDirection, "*[System[(EventID=%d)]]" % EventId, None)

    EventList = []
    for evt in win32evtlog.EvtNext(ResultSet, count):
        res = xmltodict.parse(win32evtlog.EvtRender(evt, 1))
        #took attention in events like 8. Take in mind CreateRemoteThread
        print(res["Event"]["System"]["EventID"])
        EventData = {}
        for e in res['Event']['EventData']['Data']:
            if '#text' in e:
                EventData[e['@Name']] = e['#text']

        EventList.append(EventData)

    return EventList

for i in range(0,500):
    try:
        Events = SearchEvents('Microsoft-Windows-Sysmon/Operational', i)
        #print(Events)
    except:
        pass
