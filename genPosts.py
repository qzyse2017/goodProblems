import subprocess
import time
import datetime
import os
import re

startMode = 'powershell'
month2Num = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

def convertStr2Time(StrTime):
    #e.g. Sat Jul 7 12:36:48 2018 +0800
    rawDescription = StrTime.split(' ')
    datetimeDescription = []
    for x in rawDescription:
        t = x.strip()
        if t != '':
            datetimeDescription.append(t)
    monthNum = month2Num[datetimeDescription[2]]
    dayNum = int(datetimeDescription[3])
    timeDescription = datetimeDescription[4].split(':')
    yearNum = int(datetimeDescription[5])

    return datetime.datetime(yearNum,monthNum,dayNum,\
        int(timeDescription[0]),int(timeDescription[1]),int(timeDescription[2]))

def getLastUpdateTime():
    f = open('newPosts.md','r')
    line = (f.readlines())[2]
    #e.g. last_update: Jul 5 11:56:40 2018 +0800
    line = line.strip(' ')
    return convertStr2Time(line)

def getTimeFromLog(logStr):
    #e.g. Date:   Sat Jul 7 12:36:48 2018 +0800
    startPoint = logStr.find('\t')
    return convertStr2Time(logStr[startPoint + 1:])

def getMsgFromLog(logStr):
    #e.g. insert `How to write good git commit messages`
    startPoint = logStr.find('`')
    endPoint = logStr.find('`',startPoint + 1)
    insertStart = logStr.find('`',endPoint + 1)
    insertEnd = logStr.find('`',insertStart + 1)
    return logStr[startPoint + 1 : endPoint],logStr[insertStart + 1: insertEnd]
    
def genNewPosts():
    commands = 'git log'
    process = subprocess.run([startMode,commands],\
                            stderr = subprocess.PIPE,stdout = subprocess.PIPE)

    lastUpdateTime =  getLastUpdateTime()
    outStream = process.stdout.decode('utf-8')

    contentList = []

    newUpdateTime  = ''
    updateTimeFlag = False
    for line in outStream.splitlines():
        if line.startswith('Date'):
            commitTime = getTimeFromLog(line)
            dateLine = line
        if line.lower().find('insert') != -1:
            msg,insertLoc = getMsgFromLog(line)  
            if commitTime > lastUpdateTime:
                if updateTimeFlag == False:
                    rawDatePiece = dateLine.split(' ')
                    datePiece = []
                    for x in rawDatePiece:
                        x = x.strip()
                        if x!= '':
                            datePiece.append(x)

                    newUpdateTime = 'last_update: ' + (' ').join(datePiece[1:]) + '\n'
                    updateTimeFlag = True

                newPosts = ' %s\t' % commitTime.strftime('%Y-%m-%d-%H-%M')  + '[' + msg + '](' + insertLoc + '.md)' + '\r\n'
                contentList.append(newPosts)

    if updateTimeFlag != False: 
        with open('newPosts.md','r') as f:
            data = f.readlines()
            data[2] = newUpdateTime
        f.close()

        with open('newPosts.md', 'w') as f:
            f.writelines(data)
        f.close()

   
    with open('newPosts.md','a') as f:
        for newLine in reversed(contentList):
            f.write(newLine)
    f.close()
                       
if __name__ == "__main__":
    genNewPosts()