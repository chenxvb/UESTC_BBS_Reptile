import json

def json_read(file):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            content = json.load(f)
        return content
    except:
        return -1

def json_write(file, content):
    try:
        with open(file, 'w+', encoding="utf-8") as f: 
            f.write(json.dumps(content, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
        return 0
    except:
        return -1