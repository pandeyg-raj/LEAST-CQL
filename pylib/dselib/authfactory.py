# Copyright DataStax, Inc.
#
# Please see the included license file for details.
#
from six.moves import configparser
import importlib
import sys

from cassandra.auth import DSEPlainTextAuthProvider, DSEGSSAPIAuthProvider

from datastax_db_auth.auth import AdvancedAuthProvider

VALID_AUTH_SECTIONS = ['oidc', 'kerberos']


def get_auth_provider(config_file, env, hostname, username=None, password=None, auth=None, debug=None):
    if username:
        _print_debug("Using DSEPlainTextAuthProvider\n", debug)
        return DSEPlainTextAuthProvider(username=username, password=password)

    configs = configparser.SafeConfigParser() if sys.version_info < (3, 2) else configparser.ConfigParser()
    configs.read(config_file)

    if auth is None:
        # Default to the first auth section defined in the config file. This mechanism
        # has the dual purpose of disambiguating the auth provider when multiple are
        # defined in the config file, and also to ensure that the OIDC auth provider
        # is correctly detected (given that its configuration is mandatory).
        defined_auth = list(filter(lambda x: x in VALID_AUTH_SECTIONS, configs.sections()))
        auth = defined_auth[0] if defined_auth else None

    if auth == 'oidc':
        oidc_options = configs['oidc'].keys() if 'oidc' in configs.sections() else []
        oidc_args = dict([(k, configs['oidc'][k]) for k in oidc_options])
        _print_debug("Using AdvancedAuthProvider\n", debug)
        return _get_advanced_auth_provider(**oidc_args)

    # Default to kerberos which can be configured based on environment variables only,
    # preserving the legacy behavior of cqlsh.
    return _get_kerberos_auth_provider(configs, env, hostname, debug)


def _get_kerberos_auth_provider(configs, env, hostname, debug=False):

    def get_option(section, option, env_variable, default=None):
        value = env.get(env_variable)
        if value is None:
            try:
                value = configs.get(section, option)
            except configparser.Error:
                value = default
        return value

    """
    Kerberos auth provider can be configured in the cqlshrc file [kerberos] section
    or with environment variables:

    Config option      Environment Variable      Description
    -------------      --------------------      -----------
    service            KRB_SERVICE               Service to authenticate with
    qops               QOPS                      Comma separated list of QOP values (default: auth)
    """

    krb_service = get_option('kerberos', 'service', 'KRB_SERVICE', 'dse')
    krb_qop_value = get_option('kerberos', 'qops', 'QOPS', 'auth')

    try:
        provider_name = get_option('kerberos', 'dsecqlsh_auth_provider', 'DSECQLSH_AUTH_PROVIDER', 'DSEGSSAPIAuthProvider')
        try:
            # pluggable auth_providers must be placed in a `dselib/<name>.py` file
            cls = getattr(importlib.import_module('dselib.' + provider_name), provider_name)
        except:
            cls = globals()[provider_name] if provider_name in globals() else DSEGSSAPIAuthProvider
        provider = cls(service=krb_service, qops=krb_qop_value.split(','), hostname=hostname)
        _print_debug("Using %s(service=%s, qops=%s, hostname=%s)\n" % (provider_name, krb_service, krb_qop_value, hostname), debug)
        _print_debug("    This will only be used if the server requests kerberos authentication\n", debug)
        return provider
    except ImportError as e:
        _print_debug("Attempted to use %s(service=%s, qops=%s, hostname=%s)\n" % (provider_name, krb_service, krb_qop_value, hostname), debug)
        _print_debug("    Attempt failed because: %s\n" % str(e), debug)
        return None


def _get_advanced_auth_provider(**kwargs):
    """
    Use Advanced Auth provider for OIDC authentication configured in the cqlshrc file [oidc] section

    Config option      Description
    -------------      -----------
    issuer_url         OpenID Connect issuer URL
    client_id          OpenID Connect Client Id
    client_secret      OpenID Connect Client Secret
    auth_flow          OpenID Connect Authentication Flow. Options are "code" (default) for Authorization
                       Code Flow, or "client" for Client Credentials Flow.
    truststore         OpenID Connect Truststore use to connect to the issuer
    ssl_verify         OpenID Connect SSL connection verify (default true)
    interactive        OpenID Connect interactive Authorization Code Flow (default true)
    callback_url       OpenId Connect Authorization Code Flow callback endpoint (default to /oauth/callback)
    callback_port      OpenId Connect Authorization Code Flow callback port (default to 0, ephemeral port)
    browser_auto_open  Automatically open the browser when using Authorization Code Flow (default true)
    """
    return AdvancedAuthProvider(**kwargs)


def _print_debug(message, debug=False):
    if debug:
        sys.stderr.write(message)
