#encoding:utf-8
from __future__ import unicode_literals

import urllib


def caesar(location):
    num = int(location[0])
    avg_len, remainder = int(len(location[1:]) / num), int(len(location[1:]) % num)
    result = [location[i * (avg_len + 1) + 1: (i + 1) * (avg_len + 1) + 1] for i in range(remainder)]
    result.extend([location[(avg_len + 1) * remainder:][i * avg_len + 1: (i + 1) * avg_len + 1] for i in range(num-remainder)])
    url = urllib.unquote(''.join([''.join([result[j][i] for j in range(num)]) for i in range(avg_len)]) + \
                        ''.join([result[r][-1] for r in range(remainder)])).replace('^','0')
    print url

caesar('6hAFlm%%%875_%h3%c986-55%lt%mei222%8El3_D52e141EE5lt25..FFF235.FkeEd2f137%EpF.xc994F_6mae88f9d1965-%%fio336527puy8525ea28En32iam7786%13t%e2ed34%%-u')

