"""Main entry point for the Todo List application."""

from todo.cli.console import run_cli


def main():
    """Main application entry point."""
    print("🚀 Todo List Application Started!")
    print("📊 Database: PostgreSQL with SQLAlchemy")

    try:
        # start CLI
        run_cli()
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"💥 Application error: {e}")
    finally:
        print("✅ Application shutdown complete")


if __name__ == "__main__":
    main()