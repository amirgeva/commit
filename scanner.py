import utils


def scan(root, data):
    """
    Scan the git status printout to find modified and untracked files
    Returns a list of such files
    """
    patterns = {
        'Changes to be committed:': 'Staged',
        'Changes not staged for commit:': 'Modified',
        'Untracked files:': 'Untracked'
    }
    (out, err) = utils.call(root, 'git', 'status', '-u')
    out = out.decode('utf-8')
    lines = out.split('\n')
    n = len(lines)
    i = 0
    status = 'UNKNOWN'
    scanStage = -1
    rows = []
    for line in lines:
        for pat in patterns:
            if line.startswith(pat):
                status = patterns.get(pat)
                scanStage = 0
        if scanStage < 0:
            continue
        line = line.strip()
        if len(line) == 0:
            scanStage = -1
            continue
        if line.startswith("("):
            if scanStage == 0:
                scanStage = 1
            continue
        if scanStage == 1:
            modifiers = []
            filename = line.strip()
            if filename.startswith('new file:'):
                modifiers.append("New")
                filename = (filename[9:]).strip()
            if filename.startswith('modified:'):
                filename = (filename[9:]).strip()
            if filename.startswith('deleted:'):
                filename = (filename[8:]).strip()
                modifiers.append("Deleted")
            fileStatus = status
            if len(modifiers) > 0:
                fileStatus = status + " (" + ','.join(modifiers) + ")"
            comment = ''
            if filename in data:
                comment = (data.get(filename))[2]
            rows.append([filename, fileStatus, comment])
        i = i + 1
    return rows
