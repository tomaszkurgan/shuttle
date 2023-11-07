import click

from .registry import Registry


@click.group("shuttle")
def shuttle_cli():
    ...


@shuttle_cli.command("list")
def list_cmd():
    registry = Registry.load(r"C:\dev\projects\shuttle\temp\shuttle_registry.json")
    for conn in registry:
        print(conn)


@shuttle_cli.command("conn")
@click.argument("name")
def connect_cmd(name):
    registry = Registry.load(r"C:\dev\projects\shuttle\temp\shuttle_registry.json")
    conn = registry[name]
    conn.connect()
