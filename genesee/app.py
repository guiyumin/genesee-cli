"""Genesee TUI Application."""

from collections.abc import Iterable
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Static, DirectoryTree, Header
from textual.binding import Binding

# Files and directories to ignore
IGNORED_PATTERNS = {
    "__pycache__",
    ".pyc",
    ".pyo",
    ".git",
    ".DS_Store",
    ".venv",
    "node_modules",
}


class FilteredDirectoryTree(DirectoryTree):
    """DirectoryTree that filters out ignored files."""

    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        """Filter out ignored paths."""
        return [
            p for p in paths
            if p.name not in IGNORED_PATTERNS
            and p.suffix not in IGNORED_PATTERNS
        ]


SPLASH_ASCII = """\
[bold cyan]   ██████╗ ███████╗███╗   ██╗███████╗███████╗███████╗███████╗[/]
[bold cyan]  ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝██╔════╝[/]
[bold cyan]  ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ███████╗█████╗  █████╗  [/]
[bold cyan]  ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║██╔══╝  ██╔══╝  [/]
[bold cyan]  ╚██████╔╝███████╗██║ ╚████║███████╗███████║███████╗███████╗[/]
[bold cyan]   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚══════╝[/]

[dim]Genesee — AI for Biomedical and Pharmaceutical Research[/]"""


class GeneseeApp(App[None]):
    """The main Genesee TUI application."""

    TITLE = "Genesee"
    CSS = """
    Screen {
        background: $surface;
    }

    #splash-container {
        width: 100%;
        height: 100%;
        align: center middle;
    }

    #splash {
        width: auto;
        height: auto;
        text-align: center;
    }

    #main-container {
        width: 100%;
        height: 100%;
    }

    #sidebar {
        width: 30;
        height: 100%;
        dock: left;
        border-right: solid $primary;
    }

    DirectoryTree {
        width: 100%;
        height: 100%;
        padding-left: 1;
    }

    #content {
        width: 100%;
        height: 100%;
        padding: 1 2;
    }

    #file-info {
        width: 100%;
        height: 100%;
        content-align: center middle;
    }

    .hidden {
        display: none;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("?", "help", "Help", show=True),
        Binding("f", "toggle_files", "Files", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        # Splash screen
        yield Vertical(
            Static(SPLASH_ASCII, id="splash"),
            id="splash-container",
        )

        # Main UI with file tree
        yield Horizontal(
            Vertical(
                FilteredDirectoryTree(Path.cwd(), id="tree"),
                id="sidebar",
            ),
            Vertical(
                Static("[dim]Select a file to view details[/]", id="file-info"),
                id="content",
            ),
            id="main-container",
            classes="hidden",
        )

        yield Footer()

    def on_mount(self) -> None:
        """Called when app is mounted - start splash timer."""
        self.set_timer(1.5, self._show_main_screen)

    def _show_main_screen(self) -> None:
        """Transition from splash to main screen."""
        self.query_one("#splash-container").add_class("hidden")
        self.query_one("#main-container").remove_class("hidden")
        self.query_one(FilteredDirectoryTree).focus()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        """Handle file selection in the tree."""
        path = event.path
        file_info = self.query_one("#file-info", Static)

        # Get file info
        stat = path.stat()
        size = stat.st_size

        # Format size
        if size < 1024:
            size_str = f"{size} B"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size / (1024 * 1024):.1f} MB"

        file_info.update(
            f"[bold cyan]{path.name}[/]\n\n"
            f"[dim]Path:[/] {path}\n"
            f"[dim]Size:[/] {size_str}\n"
            f"[dim]Type:[/] {path.suffix or 'No extension'}"
        )

    def action_toggle_files(self) -> None:
        """Toggle the file sidebar."""
        sidebar = self.query_one("#sidebar")
        sidebar.toggle_class("hidden")

    def action_help(self) -> None:
        """Show help."""
        self.notify(
            "q: Quit | f: Toggle files | ?: Help",
            title="Keyboard Shortcuts",
        )


def main() -> None:
    """Entry point for the Genesee TUI."""
    app = GeneseeApp()
    app.run()


if __name__ == "__main__":
    main()
