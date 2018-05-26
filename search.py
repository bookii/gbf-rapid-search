# -*- coding: utf-8 -*-

import json
import re
import subprocess
import sys
import time
from requests_oauthlib import OAuth1Session

# 取得したConsumer Key等と置き換えてください
CK = 'consumer_key'
CS = 'consumer_secret'
AT = 'access_token'
AS = 'access_token_secret'

FILTER_URL = 'https://stream.twitter.com/1.1/statuses/filter.json'

# params depend on OS
CMD_NAME = ''
IF_USES_SHELL = ''

def set_os_params():
    os_name = sys.platform
    global CMD_NAME, IF_USES_SHELL

    if os_name == 'win32':     # Windows
        CMD_NAME = 'clip'
        IF_USES_SHELL = True
    elif os_name == 'darwin':    # Mac
        CMD_NAME = 'pbcopy'
        IF_USES_SHELL = False
    else:
        print("Don't understand this operating system.")
        print("Try on Windows or Mac.")
        sys.exit()

# 文字列から参戦IDを抽出
def parse(string):
    pattern = r'[0-9A-F]{8}\s:参戦ID'
    matchOB = re.findall(pattern, string)   # 一致する文字列を全て取得
    if matchOB:
        return matchOB[-1][0:8]     # 一致する文字列のうち最後のものをreturnすることによってダミーのIDを回避
    else:
        return None

# テキストをクリップボードにコピー
def set_clipboard(string):
    process = subprocess.Popen(CMD_NAME, stdin = subprocess.PIPE, shell=IF_USES_SHELL)
    process.communicate(string.encode("utf-8")) # str型をbyte型に変換

def usage():
    print('Usage: python %s level name' % sys.argv[0])
    print('Example: python %s 75 シュヴァリエ・マグナ' % sys.argv[0])

def main():
    try:
        args = sys.argv
        if len(args) != 3:
            usage()
            sys.exit()
        
        set_os_params()

        # OAuth
        oauth_session = OAuth1Session(CK, CS, AT, AS)
        params = {'track': 'Lv%s %s' % (args[1], args[2])}
        req = oauth_session.post(FILTER_URL, params=params, stream=True)
        for line in req.iter_lines():
            line_decode = line.decode('utf-8')
            if line_decode != '':   # if not empty
                tweet = json.loads(line_decode)
                if tweet.get('source') == '<a href="http://granbluefantasy.jp/" rel="nofollow">グランブルー ファンタジー</a>':
                    tm = time.localtime()
                    name = tweet.get('user').get('name')
                    screen_name = tweet.get('user').get('screen_name')

                    print("[%02d:%02d:%02d] %s @%s" % (tm.tm_hour, tm.tm_min, tm.tm_sec, name, screen_name))
                    print(tweet.get('text') + '\n')

                    raid_id = parse(tweet.get('text'))
                    if raid_id:
                        set_clipboard(raid_id)

    except KeyboardInterrupt:
        print()
        sys.exit()

if __name__ == "__main__":
    main()
