import os.path as Path
import sqlite3


SQL_SELECT_ALL = """
	SELECT
		id, original_url, short_url, created
	FROM
		shortener
"""


_SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"


_SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + " WHERE original_url=?"


_SQL_URL_BY_SHORT = SQL_SELECT_ALL + " WHERE short_url=?"


_SQL_INSERT_URL = """
	INSERT INTO shortener (original_url) VALUES (?)
"""


_SQL_UPDATE_SHORT_URL = """
	UPDATE shortener SET short_url=? WHERE id=?
"""


def dict_factory(cursor, row):
	d = {}

	print('==> Row', row)
	print('==>', cursor.description)

	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]

	return d


def connect(db_name=None):
	if db_name is None:
		db_name - ':memory:'
	conn = sqlite3.connect(db_name)
	conn.row_factory = dict_factory

	return conn


def initialize(conn, creation_schema):
	with conn, open(creation_schema) as f:
		conn.executescript(f.read())


def add_url(conn, url, domain=''):
	"""Save URL in base"""
	url = url.rstrip('/')

	if not url:
		#ошибка должна быть
		raise RuntimeError('URL can not be empty!')

	with conn:
		found = find_url_by_origin(conn, url)

		if found:
			return found.get('short_url')

		cursor = conn.execute(_SQL_INSERT_URL, (url,))

		pk = cursor.lastrowid	#последний сгенерированный PK
		short_url = '{}/{}'.format(domain.strip('/'), pk)


		conn.execute(_SQL_UPDATE_SHORT_URL, (short_url, pk))

		return short_url


def find_all(conn):
	"""back all URL from base"""


def find_url_by_pk(conn, pk):
	""" back URL with pk"""


def find_url_by_short(conn, short_url):
	""" Back short URL"""
	short_url = short_url.rsplit('/', 1).pop()
	pk = inverse(short_url)
	return find_url_by_pk(conn, pk)


def find_url_by_origin(conn, origin_url):
	"""back original URL"""
	url = origin_url.strip('/')

	with conn:
		cursor = conn.execute(_SQL_SELECT_URL_BY_ORIGINAL, (url,))
		return cursor.fetchone()
