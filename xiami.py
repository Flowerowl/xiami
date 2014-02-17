#encoding:utf-8
import urllib


def caesar(location):
    num = int(location[0])
    avg_len, remainder = int(len(location[1:]) / num), int(len(location[1:]) % num)
    result = [location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1] for i in range(remainder)]
    result.extend([location[(avg_len + 1) * remainder:][i * avg_len + 1: (i + 1) * avg_len + 1] for i in range(num-remainder)])
    url = urllib.unquote(''.join([''.join([result[j][i] for j in range(num)]) for i in range(avg_len)]) + \
                        ''.join([result[r][-1] for r in range(remainder)])).replace('^','0')
    return url
