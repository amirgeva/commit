import utils

def scan(root,data):
    patterns={
      'Changes to be committed:':'Staged',
      'Changes not staged for commit:':'Modified',
      'Untracked files:':'Untracked'          
    }
    (out,err)=utils.call(root,'git','status','-u')
    #open('dump.txt','w').write(out)
    lines=out.split('\n')
    n=len(lines)
    i=0
    status='UNKNOWN'
    scanStage=-1
    rows=[]
    while i<n:
        line=lines[i]
        for pat in patterns:
            if line.startswith(pat):
                status=patterns.get(pat)
                scanStage=0
        if len(line.strip())==0:
            if scanStage>=0:
                scanStage=scanStage+1
        elif scanStage==1:
            modifiers=[]
            filename=line.strip()
            if filename.startswith('new file:'):
                modifiers.append("New")
                filename=(filename[9:]).strip()
            if filename.startswith('modified:'):
                filename=(filename[9:]).strip()
            fileStatus=status
            if len(modifiers)>0:
                fileStatus=status+" ("+','.join(modifiers)+")"

            print "Adding {} [{}]".format(filename,fileStatus)
            comment=''
            if filename in data:
                comment=(data.get(filename))[2]
            rows.append([filename,fileStatus,comment])
        i=i+1
    return rows

                
    