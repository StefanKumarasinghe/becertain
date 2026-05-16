"""
Custom exceptions for data source connectors and queries.

Copyright (c) 2026 Stefan Kumarasinghe.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. See http://www.apache.org/licenses/LICENSE-2.0 for details.
"""


class DataSourceError(Exception):
    pass


class DataSourceUnavailableError(DataSourceError):
    pass


class QueryTimeoutError(DataSourceError):
    pass


class InvalidQueryError(DataSourceError):
    pass


class BackendStartupTimeoutError(DataSourceError):
    pass
