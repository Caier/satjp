<?PHP
define('SPOOLDIR', '/var/spool/voipmonitor/');
define('DISABLE_CHECK_SPOOLDIR', false);
define('MYSQL_HOST', 'mariadb-voipmon');
define('MYSQL_DB', 'voipmonitor');
define('MYSQL_USER', 'root');
define('MYSQL_PASS', '');
define('MYSQL_KEY', '');
define('MYSQL_CERT', '');
define('MYSQL_CACERT', '');
define('MYSQL_CAPATH', '');
define('MYSQL_CIPHERS', '');
define('VPMANAGERHOST', 'freeswitch');
define('VPMANAGERPORT', 5029);
define('ENABLE_IP_REVERSE_LOOKUP', true);
define('DEFAULT_CDR_INTERVAL', 0);
define('SNIFFER_NAME', 'voipmonitor');
define('TIMEZONE', 'system default');
define('DATE_FORMAT', 'Y-m-d');
define('TIME_FORMAT', 'G:i:s');
define('ENABLE_GROUPS_CDR', true);
define('ENABLE_FILTER_CDR_BY_IP_GROUPS', true);
define('ENABLE_GROUP_CDR_BY_IP_GROUPS', true);
define('ENABLE_SQL_IP_REVERSE_LOOKUP', true);
define('ENABLE_DIG_REVERSE_RESOLVE', false);
define('ENABLE_SQL_CUSTOMER_PREFIX_LOOKUP', false);
// this is for rare cases when wav cannot be decoded
define('NORTPFIRSTLEG', true);
define('ENABLE_TEST_SIP_USERS', false);
// If true  https://voipmonitor/php/2909.wav will not require user to be logged. If true, user is not checked against valid session when downloading WAV. Suitable for downloading WAV outside VoIPmonitor GUI. If you need to secure it, you can set WAV_API_KEY below.
define('DISABLE_WAV_SECURITY', false);
        // If you set DISABLE_WAV_SECURITY and set WAV_API_KEY, you have to pass &key=puthereSomeKey to WAV /php/wav.php?id=226587&key=puthereSomeKey. If you do not set WAV_API_KEY you do not need to pass that key (but still have to set true to DISABLE_WAV_SECURITY.
#define('WAV_API_KEY', 'puthereSomeKey');
        // disable showing domains in CDR
define('DISABLE_SHOW_DOMAIN', false);
        // disable play in live view globally
define('DISABLE_LIVEPLAY', false);
        // disable play in CDR globally
define('DISABLE_CDRPLAY', false);
        // define configuration file used for uploading files
define('UPLOADPCAP_SNIFFERCONF', '/etc/voipmonitor.conf');
        define('EULA_AGREE', true);
?>