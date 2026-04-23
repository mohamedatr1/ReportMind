
import os
import sys
import datetime
import argparse
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.status import Status
import colorama
from colorama import Fore, Style
import click
import warnings
warnings.filterwarnings("ignore")

# Initialize colorama for cross-platform colors
colorama.init()

console = Console()

def print_banner():
    banner = r"""
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║   ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗       ║
  ║   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝       ║
  ║   ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║          ║
  ║   ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║          ║
  ║   ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║          ║
  ║   ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝          ║
  ║                                                              ║
  ║    ███╗   ███╗██╗███╗   ██╗██████╗                          ║
  ║    ████╗ ████║██║████╗  ██║██╔══██╗                         ║
  ║    ██╔████╔██║██║██╔██╗ ██║██║  ██║                         ║
  ║    ██║╚██╔╝██║██║██║╚██╗██║██║  ██║                         ║
  ║    ██║ ╚═╝ ██║██║██║ ╚████║██████╔╝                         ║
  ║    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝                          ║
  ║                                                              ║
  ║              AI-Powered Research Agent                      ║
  ║         Generate reports with a single query                ║
  ╚══════════════════════════════════════════════════════════════╝
    """
    
    console.print(Text(banner, style="bold blue"))
    console.print(Text("Welcome to ReportMind - AI Research Agent", justify="center", style="bold green"))
    console.print(Text("Real-time web search • Evidence-grounded answers • Auto-generated reports\n", justify="center", style="italic"))
def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(message, status_type="info"):
    """Print styled status messages."""
    styles = {
        "success": f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}",
        "warning": f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL}",
        "error": f"{Fore.RED}[ERROR]{Style.RESET_ALL}",
        "info": f"{Fore.CYAN}[INFO]{Style.RESET_ALL}",
        "thinking": f"{Fore.MAGENTA}[THINKING]{Style.RESET_ALL}"
    }
    
    style = styles.get(status_type, styles["info"])
    console.print(f"{style} {message}")

def display_search_results(results):
    """Display search results in a rich table."""
    if not results:
        return
    
    table = Table(title="Search Results", title_style="bold magenta")
    table.add_column("Source", style="cyan", width=20)
    table.add_column("Content", style="white")
    
    # Display first few results
    for i, result in enumerate(results[:3]):
        if isinstance(result, dict):
            content = result.get('content', str(result))
            url = result.get('url', 'N/A')
        else:
            content = str(result)
            url = 'N/A'
        
        table.add_row(url[:20] + "..." if len(url) > 20 else url, content[:70] + "..." if len(content) > 70 else content)
    
    console.print(table)

def main():
    parser = argparse.ArgumentParser(description='ReportMind - Enterprise Research Agent')
    parser.add_argument('query', nargs='*', help='Query to process (optional, will prompt if not provided)')
    parser.add_argument('--verbose', action='store_true', help='Show tool calls and reasoning steps')
    args = parser.parse_args()
    
    clear_screen()
    print_banner()
    
    # Load environment variables
    load_dotenv()
    
    # Initialize tools and agent
    try:
        tools = [TavilySearchResults(max_results=5)]
        llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile")
        agent = create_react_agent(llm, tools=tools)
    except Exception as e:
        print_status(f"Failed to initialize agent: {str(e)}", "error")
        sys.exit(1)
    
    # Get query either from command line or user input
    if args.query:
        query = " ".join(args.query)
        print_status(f"Processing query: {query}", "info")
    else:
        query = Prompt.ask("\n[bold cyan]Enter your research query[/bold cyan]")
    
    if not query.strip():
        print_status("Query cannot be empty", "error")
        return
    
    # Show progress during agent processing
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        task1 = progress.add_task(description="Initializing agent...", total=None)
        # Simulate a small delay for initialization visualization
        import time
        time.sleep(0.5)
        progress.update(task1, completed=True, description="[green]✓ Agent initialized[/green]")
        
        task2 = progress.add_task(description="Searching the web...", total=None)
        # Actual agent processing would happen here
        result = agent.invoke({"messages": [("user", query)]})
        progress.update(task2, completed=True, description="[green]✓ Search completed[/green]")
        
        task3 = progress.add_task(description="Analyzing results...", total=None)
        time.sleep(0.5)  # Simulate analysis time
        progress.update(task3, completed=True, description="[green]✓ Analysis completed[/green]")
        
        task4 = progress.add_task(description="Generating report...", total=None)
        content = result["messages"][-1].content
        progress.update(task4, completed=True, description="[green]✓ Report generated[/green]")
    
    # Create reports directory if it doesn't exist
    folder_name = "reports"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Save the report with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Report_{timestamp}.md"
    filepath = os.path.join(folder_name, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Display success message with clickable path
        console.print(Panel.fit(f"[bold green]✅ Report successfully generated![/bold green]\n\n[link=file://{os.path.abspath(filepath)}]{filepath}[/link]\n\n[bold]ReportMind[/bold] - Enterprise-grade Research Automation", 
                                title="Success", border_style="green"))
        
        # Play a completion sound (terminal bell)
        console.bell()
        
        # Optionally show verbose information if requested
        if args.verbose:
            console.print(Panel.fit(f"[bold yellow]Verbose Output:[/bold yellow]\n\n{str(result['messages'])[:500]}...", 
                                    title="Debug Info", border_style="yellow"))
        
    except Exception as e:
        print_status(f"Error saving report: {str(e)}", "error")

if __name__ == "__main__":
    main()