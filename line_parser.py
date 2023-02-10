def parse(line):
    if line and isinstance(line, str):
        token = '';
        result = []
        i = 0;
        while i < len(line):
            if line[i] == ' ':
                i += 1
                continue
            if line[i] == '"':
                i += 1
                while i < len(line) and line[i] != '"':
                    token += line[i]
                    i += 1
                result.append(token)
                token = ''
                i += 1
            elif i < len(line):
                while i < len(line) and line[i] != ' ':
                    token += line[i]
                    i += 1
                result.append(token)
                i += 1
                token = ''
        return result
