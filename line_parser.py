def parse_line(line):
    """parse a given string into tokens

    Args:
        line: str

    Description:
        this function splits a given string by space characters or '"'. Characters withing 2 '"' are considered single tokens

    Returns: list of strings
    """
    if line and isinstance(line, str):
        line = line.strip()
        token = '';
        result = []
        i = 0;
        while i < len(line):
            if line[i] == ' ':
                i += 1
                continue
            if line[i] in '"':
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
    else:
        return []
