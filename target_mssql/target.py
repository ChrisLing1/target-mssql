"""mssql target class."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.target_base import SQLTarget

from target_mssql.sinks import mssqlSink


class Targetmssql(SQLTarget):
    """Singer target for mssql."""

    name = "target-mssql"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "sqlalchemy_url",
            th.StringType,
            description="SQLAlchemy connection string",
        ),
        th.Property(
            "username",
            th.StringType,
            description="SQL Server username",
        ),
        th.Property(
            "password",
            th.StringType,
            description="SQL Server password",
        ),
        th.Property(
            "host",
            th.StringType,
            description="SQL Server host",
        ),
        th.Property(
            "port",
            th.StringType,
            default="1433",
            description="SQL Server port",
        ),
        th.Property(
            "database",
            th.StringType,
            description="SQL Server database",
        ),
        th.Property(
            "default_target_schema",
            th.StringType,
            description="Default target schema to write to",
        ),
        th.Property(
            "table_name", th.StringType, description="Target table name"
        ),
        th.Property(
            "prefer_float_over_numeric",
            th.BooleanType,
            description="Use float data type for numbers (otherwise number type is used)",
            default=False,
        ),
    ).to_dict()

    default_sink_class = mssqlSink

    def _handle_max_record_age(self) -> None:
        # remove default batch time limit
        pass

    def _process_endofpipe(self) -> None:
        """Called after all input lines have been read."""
        self.drain_all(is_endofpipe=True)


if __name__ == "__main__":
    Targetmssql.cli()
