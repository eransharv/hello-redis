#encoding=utf-8

import random
import socket
import re

INVALID_KEY = re.compile(r'[\x00-\x1F]|\s|\x7F', re.IGNORECASE)
TERMINAL = '\r\n'
BUFSIZE = 4096
MAX_KEY_LEN = 250

class MemClientError(Exception):
    pass

class MemServerError(Exception):
    pass

class MemClient(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.socket.connect((host, port))

    def _check_key(self, key):
        '''
        length <= 250
        no control character or whitespace
        '''
        if not isinstance(key, basestring):
            raise MemClientError('key must be str or unicode')
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if len(key) > MAX_KEY_LEN:
            raise MemClientError('key is too long (less than 250 characters)')
        res = INVALID_KEY.search(key)
        if res is not None:
            raise MemClientError('key contains control characters or whitespace')
        return key

    def _check_value(self, value, value_type=basestring):
        if not isinstance(value, value_type):
            raise MemClientError('value must be %s' % (value_type,))
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        return value

    # storage commands
    def _storage_command(self, command, key, value, expire, noreply, cas_unique=None):
        key = self._check_key(key)
        value = self._check_value(value)

        num_bytes = len(value)
        flags = random.randint(0, (1 << 16) - 1)

        meta = [command, key, str(flags), str(expire), str(num_bytes)]
        if cas_unique:
            meta.append(cas_unique)
        if noreply is True:
            meta.append('noreply')
        header = ' '.join(meta)
        padding = ''
        request = TERMINAL.join((header, value, padding))
        res = self.socket.sendall(request)
        if res is None and noreply is False:
            data = self.socket.recv(BUFSIZE)
        else:
            raise MemClientError('execute command %s failed' % command)

    def set(self, key, value, expire=0, noreply=True):
        return self._storage_command('set', key, value, expire, noreply)

    def add(self, key, value, expire=0, noreply=True):
        return self._storage_command('add', key, value, expire, noreply)

    def replace(self, key, value, expire=0, noreply=True):
        return self._storage_command('replace', key, value, expire, noreply)

    def append(self, key, value, noreply=True):
        return self._storage_command('append', key, value, 0, noreply)

    def prepend(self, key, value, noreply=True):
        return self._storage_command('prepend', key, value, 0, noreply)

    def cas(self, key, value, cas_unique, expire=0, noreply=True):
        raise NotImplemented

    # retrieval commands
    def _retrieval_command(self, command, keylist):
        keymap = {}
        for i in range(len(keylist)):
            keylist[i] = self._check_key(keylist[i])
            keymap[keylist[i]] = None

        keystr = ' '.join(keymap.keys())
        header = ' '.join((command, keystr))
        padding = ''
        request = TERMINAL.join((header, padding))
        res = self.socket.sendall(request)
        if res is None:
            data = self.socket.recv(BUFSIZE)
            while not data.endswith('END\r\n'):
                part = self.socket.recv(BUFSIZE)
                data = ''.join((data, part))
            blocks = data.split(TERMINAL)[:-2]
            for i in range(0, len(blocks), 2):
                header = blocks[i].split()
                raw = blocks[i + 1]
                if len(raw) != int(header[3]):
                    raise MemServerError('incomplete value for %s' % header[1])
                if len(header) == 5:
                    keymap[header[1]] = (raw, long(header[4]))
                else:
                    keymap[header[1]] = raw
            values = [keymap[key] for key in keylist]
            return values
        else:
            raise ClientError('execute command %s failed' % command)

    def get(self, key, *args):
        return self._retrieval_command('get', [key] + list(args))

    def gets(self, key, *args):
        return self._retrieval_command('gets', [key] + list(args))

    def _send_command(self, command, key, value=None, noreply=True):
        meta = [command, key]
        if value is not None:
            meta.append(value)
        if noreply  is True:
            meta.append('noreply')
        header = ' '.join(meta)
        padding = ''
        request = TERMINAL.join((header, padding))
        res = self.socket.sendall(request)
        if res is None and noreply is False:
            data = self.socket.recv(BUFSIZE)
        else:
            raise MemClientError('execute command %s failed' % command)

    # other commands
    def delete(self, key, noreply=True):
        key = self._check_key(key)
        self._send_command('delete', key, noreply=noreply)

    def incr(self, key, value, noreply=True):
        key = self._check_key(key)
        value = self._check_value(value, value_type=(int, long))
        self._send_command('incr', key, value, noreply)

    def decr(self, key, value, noreply=True):
        key = self._check_key(key)
        value = self._check_value(value, value_type=(int, long))
        self._send_command('decr', key, value, noreply)

    def touch(self, key, expire, noreply=True):
        key = self._check_key(key)
        self._send_command('touch', key, str(expire), noreply=noreply)

    def slabs_reassign(self, source, dest):
        raise NotImplemented

    def slabs_automove(self, indicator):
        raise NotImplemented

    def lru_crawler(self, enabled=True):
        raise NotImplemented

    def lru_crawler_sleep(self, ms):
        raise NotImplemented

    def lru_crawler_tocrawl(self, num):
        raise NotImplemented

    def lru_crawler_crawl(self, classid, *args, **kwargs):
        raise NotImplemented

    def stats(self):
        stat = {}
        header = 'stats'
        padding = ''
        request = TERMINAL.join((header, padding))
        res = self.socket.sendall(request)
        if res is None:
            data = self.socket.recv(BUFSIZE)
            while not data.endswith('END\r\n'):
                part = self.socket.recv(BUFSIZE)
                data = ''.join((data, part))
            blocks = data.split(TERMINAL)[:-2]
            for item in blocks:
                _, key, value = item.split(' ', 2)
                stat[key] = value
        else:
            raise MemClientError('execute command %s failed' % command)
        return stat

    def stats_settings(self):
        raise NotImplemented

    def stats_items(self):
        raise NotImplemented

    def stats_sizes(self):
        raise NotImplemented

    def stats_slabs(self):
        raise NotImplemented

    def stats_conns(self):
        raise NotImplemented

    def flush_all(self, delay=0, noreply=True):
        self._send_command('flush_all', str(delay), noreply=noreply)

    def version(self):
        header = 'version'
        padding = ''
        request = TERMINAL.join((header, padding))
        res = self.socket.sendall(request)
        if res is None:
            data = self.socket.recv(BUFSIZE)
            return data[8:-2]
        else:
            raise MemClientError('execute command %s failed' % command)

    def verbosity(self, log_level=3, noreply=True):
        self._send_command('verbosity', str(log_level), noreply=noreply)

    def quit(self):
        header = 'quit'
        padding = ''
        request = TERMINAL.join((header, padding))
        self.socket.sendall(request)
        self.socket.close()
        # self.socket.fileno() # socket.error: [Errno 9] Bad file descriptor