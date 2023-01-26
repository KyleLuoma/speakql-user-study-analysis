
#Static class for providing keywords for keywords that can divide up a query during structure determination phase
class SpeakQlKeywords:

    def __init__(self):

        lexer_kws = ['RETRIEVE', 'SHOW-ME', 'DISPLAY', 'PRESENT', 'FIND', 'IN-TABLE', 'FROM-TABLE', 'FROM-TABLES', 'JOIN-TABLE', 
        'BY-JOINING', 'BY-JOINING-TABLE', 'JOIN-WITH', 'JOIN-WITH-TABLE', 'JOINED-WITH', 'JOINED-WITH-TABLE', 'DOT', 'AND-THEN', 
        'SUBQUERY', 'ADD', 'ALL', 'ALTER', 'ALWAYS', 'ANALYZE', 'AND', 'ARRAY', 'AS', 'ASC', 'BEFORE', 'BETWEEN', 'BOTH', 'BUCKETS', 
        'BY', 'CALL', 'CASCADE', 'CASE', 'CAST', 'CHANGE', 'CHARACTER', 'CHECK', 'COLLATE', 'COLUMN', 'CONDITION', 'CONSTRAINT', 
        'CONTINUE', 'CONVERT', 'CREATE', 'CROSS', 'CURRENT', 'CURRENT-USER', 'CURSOR', 'DATABASE', 'DATABASES', 'DECLARE', 'DEFAULT', 
        'DELAYED', 'DELETE', 'DESC', 'DESCRIBE', 'DETERMINISTIC', 'DIAGNOSTICS', 'DISTINCT', 'DISTINCTROW', 'DROP', 'EACH', 'ELSE', 
        'ELSEIF', 'EMPTY', 'ENCLOSED', 'ESCAPED', 'EXCEPT', 'EXISTS', 'EXIT', 'EXPLAIN', 'FALSE', 'FETCH', 'FOR', 'FORCE', 'FOREIGN', 
        'FROM', 'FULLTEXT', 'GENERATED', 'GET', 'GRANT', 'GROUP', 'HAVING', 'HIGH-PRIORITY', 'HISTOGRAM', 'IF', 'IGNORE', 'IN', 'INDEX', 
        'INFILE', 'INNER', 'INOUT', 'INSERT', 'INTERVAL', 'INTO', 'IS', 'ITERATE', 'JOIN', 'KEY', 'KEYS', 'KILL', 'LEADING', 'LEAVE', 
        'LEFT', 'LIKE', 'LIMIT', 'LINEAR', 'LINES', 'LOAD', 'LOCK', 'LOOP', 'LOW-PRIORITY', 'MASTER-BIND', 'MASTER-SSL-VERIFY-SERVER-CERT', 
        'MATCH', 'MAXVALUE', 'MODIFIES', 'NATURAL', 'NOT', 'NO-WRITE-TO-BINLOG', 'NULL', 'NUMBER', 'ON', 'OPTIMIZE', 'OPTION', 'OPTIONALLY', 
        'OR', 'ORDER', 'OUT', 'OVER', 'OUTER', 'OUTFILE', 'PARTITION', 'PRIMARY', 'PROCEDURE', 'PURGE', 'RANGE', 'READ', 'READS', 
        'REFERENCES', 'REGEXP', 'RELEASE', 'RENAME', 'REPEAT', 'REPLACE', 'REQUIRE', 'RESIGNAL', 'RESTRICT', 'RETAIN', 'RETURN', 'REVOKE', 
        'RIGHT', 'RLIKE', 'SCHEMA', 'SCHEMAS', 'SELECT', 'SET', 'SEPARATOR', 'SHOW', 'SIGNAL', 'SPATIAL', 'SQL', 'SQLEXCEPTION', 'SQLSTATE', 
        'SQLWARNING', 'SQL-BIG-RESULT', 'SQL-CALC-FOUND-ROWS', 'SQL-SMALL-RESULT', 'SSL', 'STACKED', 'STARTING', 'STRAIGHT-JOIN', 'TABLE', 
        'TERMINATED', 'THEN', 'TO', 'TRAILING', 'TRIGGER', 'TRUE', 'UNDO', 'UNION', 'UNIQUE', 'UNLOCK', 'UNSIGNED', 'UPDATE', 'USAGE', 'USE', 
        'USING', 'VALUES', 'WHEN', 'WHERE', 'WHILE', 'WITH', 'WRITE', 'XOR', 'ZEROFILL', '', '', '', '', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 
        'MIDDLEINT', 'INT', 'INT1', 'INT2', 'INT3', 'INT4', 'INT8', 'INTEGER', 'BIGINT', 'REAL', 'DOUBLE', 'PRECISION', 'FLOAT', 'FLOAT4', 
        'FLOAT8', 'DECIMAL', 'DEC', 'NUMERIC', 'DATE', 'TIME', 'TIMESTAMP', 'DATETIME', 'YEAR', 'CHAR', 'VARCHAR', 'NVARCHAR', 'NATIONAL', 
        'BINARY', 'VARBINARY', 'TINYBLOB', 'BLOB', 'MEDIUMBLOB', 'LONG', 'LONGBLOB', 'TINYTEXT', 'TEXT', 'MEDIUMTEXT', 'LONGTEXT', 'ENUM', 
        'VARYING', 'SERIAL', 'YEAR-MONTH', 'DAY-HOUR', 'DAY-MINUTE', 'DAY-SECOND', 'HOUR-MINUTE', 'HOUR-SECOND', 'MINUTE-SECOND', 
        'SECOND-MICROSECOND', 'MINUTE-MICROSECOND', 'HOUR-MICROSECOND', 'DAY-MICROSECOND', 'AVG', 'BIT-AND', 'BIT-OR', 'BIT-XOR', 'COUNT', 
        'CUME-DIST', 'DENSE-RANK', 'FIRST-VALUE', 'GROUP-CONCAT', 'LAG', 'LAST-VALUE', 'LEAD', 'MAX', 'MIN', 'NTILE', 'NTH-VALUE', 
        'PERCENT-RANK', 'RANK', 'ROW-NUMBER', 'STD', 'STDDEV', 'STDDEV-POP', 'STDDEV-SAMP', 'SUM', 'VAR-POP', 'VAR-SAMP', 'VARIANCE', 
        'CURRENT-DATE', 'CURRENT-TIME', 'CURRENT-TIMESTAMP', 'LOCALTIME', 'CURDATE', 'CURTIME', 'DATE-ADD', 'DATE-SUB', 'EXTRACT', 
        'LOCALTIMESTAMP', 'NOW', 'POSITION', 'SUBSTR', 'SUBSTRING', 'SYSDATE', 'TRIM', 'UTC-DATE', 'UTC-TIME', 'UTC-TIMESTAMP', 'ACCOUNT', 
        'ACTION', 'AFTER', 'AGGREGATE', 'ALGORITHM', 'ANY', 'AT', 'AUTHORS', 'AUTOCOMMIT', 'AUTOEXTEND-SIZE', 'AUTO-INCREMENT', 
        'AVG-ROW-LENGTH', 'BEGIN', 'BINLOG', 'BIT', 'BLOCK', 'BOOL', 'BOOLEAN', 'BTREE', 'CACHE', 'CASCADED', 'CHAIN', 'CHANGED', 
        'CHANNEL', 'CHECKSUM', 'PAGE-CHECKSUM', 'CIPHER', 'CLASS-ORIGIN', 'CLIENT', 'CLOSE', 'COALESCE', 'CODE', 'COLUMNS', 'COLUMN-FORMAT', 
        'COLUMN-NAME', 'COMMENT', 'COMMIT', 'COMPACT', 'COMPLETION', 'COMPRESSED', 'COMPRESSION', 'CONCURRENT', 'CONNECT', 'CONNECTION', 
        'CONSISTENT', 'CONSTRAINT-CATALOG', 'CONSTRAINT-SCHEMA', 'CONSTRAINT-NAME', 'CONTAINS', 'CONTEXT', 'CONTRIBUTORS', 'COPY', 'CPU', 
        'CURSOR-NAME', 'DATA', 'DATAFILE', 'DEALLOCATE', 'DEFAULT-AUTH', 'DEFINER', 'DELAY-KEY-WRITE', 'DES-KEY-FILE', 'DIRECTORY', 'DISABLE', 
        'DISCARD', 'DISK', 'DO', 'DUMPFILE', 'DUPLICATE', 'DYNAMIC', 'ENABLE', 'ENCRYPTION', 'END', 'ENDS', 'ENGINE', 'ENGINES', 'ERROR', 
        'ERRORS', 'ESCAPE', 'EVEN', 'EVENT', 'EVENTS', 'EVERY', 'EXCHANGE', 'EXCLUSIVE', 'EXPIRE', 'EXPORT', 'EXTENDED', 'EXTENT-SIZE', 
        'FAST', 'FAULTS', 'FIELDS', 'FILE-BLOCK-SIZE', 'FILTER', 'FIRST', 'FIXED', 'FLUSH', 'FOLLOWING', 'FOLLOWS', 'FOUND', 'FULL', 'FUNCTION', 
        'GENERAL', 'GLOBAL', 'GRANTS', 'GROUP-REPLICATION', 'HANDLER', 'HASH', 'HELP', 'HOST', 'HOSTS', 'IDENTIFIED', 'IGNORE-SERVER-IDS', 
        'IMPORT', 'INDEXES', 'INITIAL-SIZE', 'INPLACE', 'INSERT-METHOD', 'INSTALL', 'INSTANCE', 'INVISIBLE', 'INVOKER', 'IO', 'IO-THREAD', 
        'IPC', 'ISOLATION', 'ISSUER', 'JSON', 'KEY-BLOCK-SIZE', 'LANGUAGE', 'LAST', 'LEAVES', 'LESS', 'LEVEL', 'LIST', 'LOCAL', 'LOGFILE', 
        'LOGS', 'MASTER', 'MASTER-AUTO-POSITION', 'MASTER-CONNECT-RETRY', 'MASTER-DELAY', 'MASTER-HEARTBEAT-PERIOD', 'MASTER-HOST', 
        'MASTER-LOG-FILE', 'MASTER-LOG-POS', 'MASTER-PASSWORD', 'MASTER-PORT', 'MASTER-RETRY-COUNT', 'MASTER-SSL', 'MASTER-SSL-CA', 
        'MASTER-SSL-CAPATH', 'MASTER-SSL-CERT', 'MASTER-SSL-CIPHER', 'MASTER-SSL-CRL', 'MASTER-SSL-CRLPATH', 'MASTER-SSL-KEY', 
        'MASTER-TLS-VERSION', 'MASTER-USER', 'MAX-CONNECTIONS-PER-HOUR', 'MAX-QUERIES-PER-HOUR', 'MAX-ROWS', 'MAX-SIZE', 'MAX-UPDATES-PER-HOUR', 
        'MAX-USER-CONNECTIONS', 'MEDIUM', 'MEMBER', 'MERGE', 'MESSAGE-TEXT', 'MID', 'MIGRATE', 'MIN-ROWS', 'MODE', 'MODIFY', 'MUTEX', 'MYSQL', 
        'MYSQL-ERRNO', 'NAME', 'NAMES', 'NCHAR', 'NEVER', 'NEXT', 'NO', 'NODEGROUP', 'NONE', 'ODBC', 'OFFLINE', 'OFFSET', 'OF', 'OJ', 
        'OLD-PASSWORD', 'ONE', 'ONLINE', 'ONLY', 'OPEN', 'OPTIMIZER-COSTS', 'OPTIONS', 'OWNER', 'PACK-KEYS', 'PAGE', 'PARSER', 'PARTIAL', 
        'PARTITIONING', 'PARTITIONS', 'PASSWORD', 'PHASE', 'PLUGIN', 'PLUGIN-DIR', 'PLUGINS', 'PORT', 'PRECEDES', 'PRECEDING', 'PREPARE', 
        'PRESERVE', 'PREV', 'PROCESSLIST', 'PROFILE', 'PROFILES', 'PROXY', 'QUERY', 'QUICK', 'REBUILD', 'RECOVER', 'REDO-BUFFER-SIZE', 
        'REDUNDANT', 'RELAY', 'RELAY-LOG-FILE', 'RELAY-LOG-POS', 'RELAYLOG', 'REMOVE', 'REORGANIZE', 'REPAIR', 'REPLICATE-DO-DB', 
        'REPLICATE-DO-TABLE', 'REPLICATE-IGNORE-DB', 'REPLICATE-IGNORE-TABLE', 'REPLICATE-REWRITE-DB', 'REPLICATE-WILD-DO-TABLE', 
        'REPLICATE-WILD-IGNORE-TABLE', 'REPLICATION', 'RESET', 'RESUME', 'RETURNED-SQLSTATE', 'RETURNING', 'RETURNS', 'ROLE', 'ROLLBACK', 
        'ROLLUP', 'ROTATE', 'ROW', 'ROWS', 'ROW-FORMAT', 'SAVEPOINT', 'SCHEDULE', 'SECURITY', 'SERVER', 'SESSION', 'SHARE', 'SHARED', 
        'SIGNED', 'SIMPLE', 'SLAVE', 'SLOW', 'SNAPSHOT', 'SOCKET', 'SOME', 'SONAME', 'SOUNDS', 'SOURCE', 'SQL-AFTER-GTIDS', 'SQL-AFTER-MTS-GAPS', 
        'SQL-BEFORE-GTIDS', 'SQL-BUFFER-RESULT', 'SQL-CACHE', 'SQL-NO-CACHE', 'SQL-THREAD', 'START', 'STARTS', 'STATS-AUTO-RECALC', 
        'STATS-PERSISTENT', 'STATS-SAM', 'BENCHMARK', 'BIN', 'BIT-COUNT', 'BIT-LENGTH', 'BUFFER', 'CATALOG-NAME', 'CEIL', 'CEILING', 'CENTROID', 
        'CHARACTER-LENGTH', 'CHARSET', 'CHAR-LENGTH', 'COERCIBILITY', 'COLLATION', 'COMPRESS', 'CONCAT', 'CONCAT-WS', 'CONNECTION-ID', 'CONV', 
        'CONVERT-TZ', 'COS', 'COT', 'CRC32', 'CREATE-ASYMMETRIC-PRIV-KEY', 'CREATE-ASYMMETRIC-PUB-KEY', 'CREATE-DH-PARAMETERS', 'CREATE-DIGEST', 
        'CROSSES', 'DATEDIFF', 'DATE-FORMAT', 'DAYNAME', 'DAYOFMONTH', 'DAYOFWEEK', 'DAYOFYEAR', 'DECODE', 'DEGREES', 'DES-DECRYPT', 'DES-ENCRYPT', 
        'DIMENSION', 'DISJOINT', 'ELT', 'ENCODE', 'ENCRYPT', 'ENDPOINT', 'ENVELOPE', 'EQUALS', 'EXP', 'EXPORT-SET', 'EXTERIORRING', 'EXTRACTVALUE', 
        'FIELD', 'FIND-IN-SET', 'FLOOR', 'FORMAT', 'FOUND-ROWS', 'FROM-BASE64', 'FROM-DAYS', 'FROM-UNIXTIME', 'GEOMCOLLFROMTEXT', 'GEOMCOLLFROMWKB', 
        'GEOMETRYCOLLECTIONFROMTEXT', 'GEOMETRYCOLLECTIONFROMWKB', 'GEOMETRYFROMTEXT', 'GEOMETRYFROMWKB', 'GEOMETRYN', 'GEOMETRYTYPE', 'GEOMFROMTEXT', 
        'GEOMFROMWKB', 'GET-FORMAT', 'GET-LOCK', 'GLENGTH', 'GREATEST', 'GTID-SUBSET', 'GTID-SUBTRACT', 'HEX', 'IFNULL', 'INET6-ATON', 'INET6-NTOA', 
        'INET-ATON', 'INET-NTOA', 'INSTR', 'INTERIORRINGN', 'INTERSECTS', 'ISCLOSED', 'ISEMPTY', 'ISNULL', 'ISSIMPLE', 'IS-FREE-LOCK', 'IS-IPV4', 
        'IS-IPV4-COMPAT', 'IS-IPV4-MAPPED', 'IS-IPV6', 'IS-USED-LOCK', 'LAST-INSERT-ID', 'LCASE', 'LEAST', 'LENGTH', 'LINEFROMTEXT', 'LINEFROMWKB', 
        'LINESTRINGFROMTEXT', 'LINESTRINGFROMWKB', 'LN', 'LOAD-FILE', 'LOCATE', 'LOG', 'LOG10', 'LOG2', 'LOWER', 'LPAD', 'LTRIM', 'MAKEDATE', 
        'MAKETIME', 'MAKE-SET', 'MASTER-POS-WAIT', 'MBRCONTAINS', 'MBRDISJOINT', 'MBREQUAL', 'MBRINTERSECTS', 'MBROVERLAPS', 'MBRTOUCHES', 'MBRWITHIN', 
        'MD5', 'MLINEFROMTEXT', 'MLINEFROMWKB', 'MONTHNAME', 'MPOINTFROMTEXT', 'MPOINTFROMWKB', 'MPOLYFROMTEXT', 'MPOLYFROMWKB', 'MULTILINESTRINGFROMTEXT',
        'MULTILINESTRINGFROMWKB', 'MULTIPOINTFROMTEXT', 'MULTIPOINTFROMWKB', 'MULTIPOLYGONFROMTEXT', 'MULTIPOLYGONFROMWKB', 'NAME-CONST', 'NULLIF', 
        'NUMGEOMETRIES', 'NUMINTERIORRINGS', 'NUMPOINTS', 'OCT', 'OCTET-LENGTH', 'ORD', 'OVERLAPS', 'PERIOD-ADD', 'PERIOD-DIFF', 'PI', 'POINTFROMTEXT', 
        'POINTFROMWKB', 'POINTN', 'POLYFROMTEXT', 'POLYFROMWKB', 'POLYGONFROMTEXT', 'POLYGONFROMWKB', 'POW', 'POWER', 'QUOTE', 'RADIANS', 'RAND', 
        'RANDOM-BYTES', 'RELEASE-LOCK', 'REVERSE', 'ROUND', 'ROW-COUNT', 'RPAD', 'RTRIM', 'SEC-TO-TIME', 'SESSION-USER', 'SHA', 'SHA1', 'SHA2', 'SCHEMA-NAME', 
        'SIGN', 'SIN', 'SLEEP', 'SOUNDEX', 'SQL-THREAD-WAIT-AFTER-GTIDS', 'SQRT', 'SRID', 'STARTPOINT', 'STRCMP', 'STR-TO-DATE', 'ST-AREA', 'ST-ASBINARY', 
        'ST-ASTEXT', 'ST-ASWKB', 'ST-ASWKT', 'ST-BUFFER', 'ST-CENTROID', 'ST-CONTAINS', 'ST-CROSSES', 'ST-DIFFERENCE', 'ST-DIMENSION', 'ST-DISJOINT', 
        'ST-DISTANCE', 'ST-ENDPOINT', 'ST-ENVELOPE', 'ST-EQUALS', 'ST-EXTERIORRING', 'ST-GEOMCOLLFROMTEXT', 'ST-GEOMCOLLFROMTXT', 'ST-GEOMCOLLFROMWKB', 
        'ST-GEOMETRYCOLLECTIONFROMTEXT', 'ST-GEOMETRYCOLLECTIONFROMWKB', 'ST-GEOMETRYFROMTEXT', 'ST-GEOMETRYFROMWKB', 'ST-GEOMETRYN', 'ST-GEOMETRYTYPE', 
        'ST-GEOMFROMTEXT', 'ST-GEOMFROMWKB', 'ST-INTERIORRINGN', 'ST-INTERSECTION', 'ST-INTERSECTS', 'ST-ISCLOSED', 'ST-ISEMPTY', 'ST-ISSIMPLE', 
        'ST-LINEFROMTEXT', 'ST-LINEFROMWKB', 'ST-LINESTRINGFROMTEXT', 'ST-LINESTRINGFROMWKB', 'ST-NUMGEOMETRIES', 'ST-NUMINTERIORRING', 'ST-NUMINTERIORRINGS', 
        'ST-NUMPOINTS', 'ST-OVERLAPS', 'ST-POINTFROMTEXT', 'ST-POINTFROMWKB', 'ST-POINTN', 'ST-POLYFROMTEXT', 'ST-POLYFROMWKB', 'ST-POLYGONFROMTEXT', 
        'ST-POLYGONFROMWKB', 'ST-SRID', 'ST-STARTPOINT', 'ST-SYMDIFFERENCE', 'ST-TOUCHES', 'ST-UNION', 'ST-WITHIN', 'ST-X', 'ST-Y', 'SUBDATE', 
        'SUBSTRING-INDEX', 'SUBTIME', 'SYSTEM-USER', 'TAN', 'TIMEDIFF', 'TIMESTAMPADD', 'TIMESTAMPDIFF', 'TIME-FORMAT', 'TIME-TO-SEC', 'TOUCHES', 
        'TO-BASE64', 'TO-DAYS', 'TO-SECONDS', 'UCASE', 'UNCOMPRESS', 'UNCOMPRESSED-LENGTH', 'UNHEX', 'UNIX-TIMESTAMP', 'UPDATEXML', 'UPPER', 'UUID', 
        'UUID-SHORT', 'VALIDATE-PASSWORD-STRENGTH', 'VERSION', 'WAIT-UNTIL-SQL-THREAD-AFTER-GTIDS', 'WEEKDAY', 'WEEKOFYEAR', 'WEIGHT-STRING', 'WITHIN', 
        'YEARWEEK']

        self.exp_delim_kw = [
            "AND THEN",
            #"THEN"
        ]

        self.select_kw = [
            "SELECT",
            "RETRIEVE",
            "SHOW ME",
            "DISPLAY",
            "PRESENT",
            "FIND",
            "GET",
            "WHAT IS",
            "WHAT ARE",
            "WHAT IS THE",
            "WHAT ARE THE"
        ]

        self.from_kw = [
            "FROM",
            "FROM TABLE",
            "FROM TABLES",
            "IN",
            "IN TABLE",
            "IN TABLES"
        ]

        self.join_kw = [
            "JOIN",
            "JOIN TABLE",
            "BY JOINING",
            "BY JOINING TABLE",
            "JOINED WITH",
            "JOIN WITH",
            "JOINED WITH TABLE",
            "JOIN WITH TABLE",
            "BY JOINING WITH TABLE",
            "BY JOINING WITH",
            "LEFT JOIN",
            "OUTER JOIN",
            "INNER JOIN",
            "CROSS JOIN",
            "RIGHT JOIN",
            "NATURAL JOIN"
        ]

        self.with_kw = [
            "WITH",
            "WITH TABLE"
        ]

        self.group_kw = [
            "GROUP",
            "GROUP BY"
        ]

        self.order_kw = [
            "ORDER BY"
        ]

        self.having_kw = [
            "HAVING"
        ]

        self.limit_kw = [
            "LIMIT"
        ]

        #Lookup SQL keyword by its SpeakQL synonyms
        self.synonym_to_keyword_dict = {}

        for kw in self.select_kw:
            self.synonym_to_keyword_dict[kw] = "SELECT"
        for kw in self.from_kw:
            self.synonym_to_keyword_dict[kw] = "FROM"
        for kw in self.join_kw:
            self.synonym_to_keyword_dict[kw] = "JOIN"
        for kw in self.group_kw:
            self.synonym_to_keyword_dict[kw] = "GROUP BY"
        for kw in self.order_kw:
            self.synonym_to_keyword_dict[kw] = "ORDER BY"
        for kw in self.having_kw:
            self.synonym_to_keyword_dict[kw] = "HAVING"
        for kw in self.limit_kw:
            self.synonym_to_keyword_dict[kw] = "LIMIT"
        for kw in self.with_kw:
            self.synonym_to_keyword_dict[kw] = "WITH"

        #Each entry in this set represents the minimum kws that must be present
        #in an unbundled query for the query to be considered valid.
        self.min_kws_for_unbundled = [
            [self.select_kw, self.from_kw],
            [self.join_kw, self.with_kw],
            [self.group_kw],
            [self.order_kw],
            [self.having_kw],
            [self.limit_kw]
        ]

        self.literal_kw = [
            "uid",
            "constant",
            "tableName",
            "tableAlias"
        ]

        self.symbols_dict = {
            "plus" : "+",
            "minus" : "-",
            "is less than or equal to" : "<=",
            "less than or equal to" : "<=",
            "is less than" : "<",
            "less than" : "<",
            "is greater than or equal to" : ">=",
            "greater than or equal to" : ">=",
            "is greater than" : ">",
            "greater than" : ">",
            "not equal to" : "<>",
            "equals" : "=",
            "equal to" : "=",
            "equal" : "=",
            "times" : "*",
            " X " : " * ",
            "divided by" : "/",
            "open parenthesis" : "(",
            "close parenthesis" : ")",
            "end quote" : "'",
            "quote" : "'",
            "star" : "*",
            "asterisk" : "*",
            "everything" : "*"
        }

        self.symbols_to_word_list_dict = {
            "+" : ["plus"],
            "-" : ["minus"],
            "<=" : ["less than or equal to", "is less than or equal to"],
            "<" : ["less than", "is less than"],
            ">=" : ["greater than or equal to", "is greater than or equal to"],
            ">" : ["greater than", "is greater than"],
            "<>" : [
                "not equal to", "is not equal to",  
                "does not equal", "not equal"
                ],
            "=" : ["equals", "equal", "equal to", "is equal to"],
            "*" : ["times"],
            "/" : ["divided by"],
            "(" : ["open parenthesis", "opened parenthesis", "left parenthesis"],
            ")" : ["close parenthesis", "closed parenthesis", "right parenthesis"],
            "'" : ["quote", "quotation mark"],
            "." : ["dot"],
            "_" : ["underscore"],
            "," : ["comma"],
            "avg" : ["average"],
            "desc" : ["descending"],
            "asc" : ["ascending"],
            "*" : ["star", "everything", "asterisk"]
        }


    def lookup_kw_synonym(self, kw):
        try:
            return self.synonym_to_keyword_dict[kw]
        except:
            return "NONE"

    def get_min_kws_for_unbundled(self):
        return self.min_kws_for_unbundled

    def get_symbols_dict(self):
        return self.symbols_dict

    def get_symbol_text_list(self):
        key_list = []
        for key in self.symbols_dict.keys():
            key_list.append(key)
        return key_list

    def get_limit_kws(self):
        return self.limit_kw

    def get_having_kws(self):
        return self.having_kw

    def get_group_kws(self):
        return self.group_kw

    def get_order_kws(self):
        return self.order_kw
    
    def get_exp_delim_kws(self):
        return self.exp_delim_kw

    def get_select_kws(self):
        return self.select_kw

    def get_from_kws(self):
        return self.from_kw

    def get_join_kws(self):
        return self.join_kw

    def get_with_kws(self):
        return self.with_kw

    def get_start_kws(self):
        return (
            self.select_kw 
            + ["WHAT", "SHOW"]
            + self.from_kw 
            + self.join_kw 
            + ["BY", "JOINED"]
            + self.order_kw 
            + ["ORDER"]
            + self.group_kw 
            + self.having_kw
            + self.limit_kw
        )

    def get_literal_kws(self):
        return self.literal_kw