#!/usr/bin/env python
"""Script for managing migrations

Commands:
    generate:
        - generate a sample migration file

    up:
        - apply migration
        - options:
            - n, step: number of up migration to apply
            - v, to: migrate up to a specific version

    down:
        - rollback migration
        - options:
            - n, step: number of migrations to rollback
            - v, to: rollback to a specific version

    view:
        - view actual migration db
        - options:
            n, number: number of lines to display
"""
import click

import incirrina_api.lib.tools.migration as migration_lib


@click.group()
def migration():
    """Database migration manager."""
    pass


@click.command()
@click.argument('name')
def generate(name):
    """Generate a migration file."""
    if not name:
        raise click.BadParameter("<name> cannot be empty.")
    filename = migration_lib.generate_migration_file(name)
    click.echo("Created migration file: {}".format(filename))


@click.command()
@click.option("-n", "--step", type=int, help="Migrate <n> number of times.")
@click.option("-v", "--to", type=int, help="Migrate up to specific version.")
def up(step, to):
    """Apply migrations to database.
    If no options is passed, apply all (non-applied) migrations."""
    click.echo("Applying UP migrations")
    try:
        nb_migrations = migration_lib.migrate_up(step, to)
        if nb_migrations:
            msg = "{} ups applied successfully.".format(nb_migrations)
        else:
            msg = "No ups to apply."
        click.echo(msg)
    except Exception as e:
        click.secho("Could not perform operation: {}".format(e.message),
                    fg="red")
        raise click.Abort


@click.command()
@click.option("-n", "--step", type=int, help="Migrate <n> number of times.")
@click.option("-v", "--to", type=int, help="Migrate up to specific version.")
def down(step, to):
    click.echo("Applying DOWN migrations")
    """Rollback migrations."""
    if not step and not to:
        raise click.BadParameter("<step> or <to> must be defined.")
    click.echo("Downgrading for: {}".format(step))
    try:
        nb_migrations = migration_lib.migrate_down(step, to)
        if nb_migrations:
            msg = "{} rollbacks applied successfully.".format(nb_migrations)
        else:
            msg = "No rollbacks to apply."
        click.echo(msg)
    except Exception as e:
        click.secho("Could not perform operation: {}".format(e.message),
                    fg="red")
        raise click.Abort


@click.command()
@click.option("-n", "--max-count", type=int,
              help="Maximum number of migrations to display")
def view(max_count):
    """View migrations list"""
    migration_lib.view(max_count)


migration.add_command(generate)
migration.add_command(up)
migration.add_command(down)
migration.add_command(view)

if __name__ == '__main__':
    migration()
