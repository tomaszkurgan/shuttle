import json
import subprocess
from pathlib import Path

from pydantic import BaseModel


class ConnectionDefinition(BaseModel):
    name: str
    host: str
    user: str

    @property
    def url(self):
        return f"{self.user}@{self.host}"

    def connect(self):
        subprocess.call(["ssh", self.url])

    def __str__(self):
        return f"{self.name}: {self.url}"


class Registry(BaseModel):
    connection_definitions: list[ConnectionDefinition] = []

    @classmethod
    def load(cls, registry_file_path: Path):
        with open(registry_file_path, "r") as f:
            registry = json.load(f)

        conns = [ConnectionDefinition.model_validate({
            "name": conn_name,
            **conn_def,
        }) for conn_name, conn_def in registry["connections"].items()]

        return cls(connection_definitions=conns)

    def __getitem__(self, conn_name):
        for conn in self.connection_definitions:
            if conn.name == conn_name:
                return conn
        raise KeyError

    def __iter__(self):
        return iter(self.connection_definitions)
