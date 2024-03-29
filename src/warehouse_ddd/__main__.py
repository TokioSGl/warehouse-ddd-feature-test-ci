"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Warehouse Ddd."""
    from warehouse_ddd.flask_app import app

    app.run(debug=True)


if __name__ == "__main__":
    main(prog_name="warehouse-ddd")  # pragma: no cover
