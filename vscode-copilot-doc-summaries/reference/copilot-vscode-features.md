# GitHub Copilot VS Code Features Reference

## Overview

This comprehensive reference guide covers all GitHub Copilot features available in Visual Studio Code, from essential keyboard shortcuts to advanced AI-powered workflows. Use this as your complete feature reference and quick-access cheat sheet.

## Essential Keyboard Shortcuts

### Core Navigation
- **`Ctrl+Alt+I`** - Open the Chat view
- **`Ctrl+I`** - Enter voice chat prompt in Chat view / Start inline chat in editor or terminal
- **`Ctrl+N`** - Start a new chat session in Chat view
- **`Ctrl+Shift+I`** - Switch to agent mode
- **`Ctrl+I (hold)`** - Start inline voice chat
- **`Tab`** - Accept inline suggestion or navigate to next edit suggestion
- **`Escape`** - Dismiss inline suggestion

### Quick Access Features
- **`Ctrl+Shift+Alt+L`** - Open Quick Chat without interrupting workflow
- **`Ctrl+.`** - Toggle between different chat modes
- **`Ctrl+Alt+.`** - Show model picker for AI model selection
- **`F2`** - Get AI-powered symbol renaming suggestions

## Access AI in VS Code

### Chat Experiences
- **Chat view (`Ctrl+Alt+I`)**: Ongoing conversations in Secondary Side Bar
- **Inline chat (`Ctrl+I`)**: Ask questions while coding in flow
- **Quick Chat (`Ctrl+Shift+Alt+L`)**: Quick questions without context switching

### Editor AI Features
- **Code completions**: Real-time suggestions with `Tab` to accept
- **Edit context menu actions**: Right-click access to AI actions (explain, fix, test, review)
- **Code actions**: Lightbulb suggestions for fixing linting and compiler errors
- **Smart actions**: Task-specific AI assistance across VS Code

## Chat Experience Features

### Interactive Controls
| Feature | Shortcut/Action | Description |
|---------|-----------------|-------------|
| Add Context... | Button/Menu | Attach files, symbols, selections, and more |
| /-command | Type `/` | Slash commands for common tasks and reusable prompts |
| #-mention | Type `#` | Reference tools and chat variables for context |
| @-mention | Type `@` | Reference chat participants for domain-specific requests |
| Edit (✏️) | Button | Edit previous chat prompts and revert changes |
| History (📝) | Button | Access chat session history |
| Voice (🎤) | Button | Speech input with read-aloud responses |

### Tips for Effective Chat Usage
- Use `#`-mentions to add relevant context to prompts
- Use `/` commands and `@` participants for precise, relevant answers
- Be specific, keep prompts simple, and ask follow-up questions
- Choose appropriate chat modes: ask, edit, agent, or custom modes

## Context Management

### Adding Context to Prompts
- **Add Context Button**: Quick Pick for selecting relevant context types
- **Drag & Drop Files**: Drop files from Explorer or Search view onto Chat
- **Drag & Drop Folders**: Add entire folders and their contents as context
- **Drag & Drop Problems**: Include specific issues from Problems panel
- **`#<file|folder|symbol>`**: Type-ahead context addition
- **`#-mention`**: Chat variables for specific context types and tools

### Chat Variables (# syntax)
| Variable | Purpose |
|----------|---------|
| `#changes` | List of source control changes |
| `#codebase` | Workspace code search with automatic relevance |
| `#editFiles` | File creation and editing tool set |
| `#extensions` | VS Code extensions information and guidance |
| `#fetch` | Web page content retrieval |
| `#findTestFiles` | Test file discovery in workspace |
| `#<file\|folder\|symbol>` | Add specific workspace items as context |
| `#githubRepo` | GitHub repository code search |
| `#new` | New VS Code workspace scaffolding |
| `#openSimpleBrowser` | Built-in browser for local web app preview |
| `#problems` | Workspace issues from Problems panel |
| `#readCellOutput` | Notebook cell output reading |
| `#runCommands` | Terminal command execution and output |
| `#runNotebooks` | Notebook cell execution and results |
| `#runTasks` | Workspace task execution |
| `#runTests` | Test execution and results |
| `#search` | File search tool set |
| `#searchResults` | Search view results as context |
| `#selection` | Current editor selection |
| `#terminalSelection` | Current terminal selection |
| `#terminalLastCommand` | Last terminal command |
| `#testFailure` | Test failure information |
| `#usages` | Find All References + Implementation + Go to Definition |
| `#VSCodeAPI` | VS Code extension API reference |

## Slash Commands

### Essential Commands
| Command | Purpose |
|---------|---------|
| `/docs` | Generate code documentation comments (inline chat) |
| `/explain` | Explain code blocks, files, or programming concepts |
| `/fix` | Fix code blocks or resolve compiler/linting errors |
| `/help` | Get help about using chat in VS Code |
| `/tests` | Generate tests for selected methods and functions |
| `/setupTests` | Set up testing framework with recommendations |
| `/clear` | Start new chat session in Chat view |
| `/new` | Scaffold new VS Code workspace or file |
| `/newNotebook` | Create Jupyter notebook based on requirements |
| `/search` | Generate search query for Search view |
| `/startDebugging` | Generate launch.json and start debugging |
| `/<prompt file name>` | Run reusable prompt files |

## Chat Participants

### Built-in Participants
| Participant | Capabilities |
|-------------|--------------|
| `@github` | GitHub repositories, issues, PRs, and more |
| `@terminal` | Integrated terminal and shell command assistance |
| `@vscode` | VS Code features, settings, and extension APIs |
| `@workspace` | Current workspace questions and analysis |

### Example Usage
- `@github What are all of the open PRs assigned to me?`
- `@terminal list the 5 largest files in this workspace`
- `@vscode how to enable word wrapping?`
- `@workspace how is authentication implemented?`

## Agent Mode

### Core Features
- **`Ctrl+Shift+I`** - Switch to agent mode in Chat view
- **Tools (⚙️)** - Configure available tools (built-in, MCP servers, extensions)
- **Auto-approve tools** - Enable automatic tool approval (`chat.tools.autoApprove`)
- **Auto-approve terminal commands** - Automatic approval with allow/deny lists
- **MCP Integration** - Configure MCP servers for extended capabilities

### Agent Mode Tips
- Add extra tools to extend agent capabilities
- Configure custom chat modes for specific workflows
- Define custom instructions for code generation guidance
- Use for complex, multi-step development tasks

## Customization Features

### Custom Instructions
Define guidelines for:
- Code generation standards
- Code review practices
- Commit message formats
- Language-specific patterns

### Reusable Prompt Files
- Create standalone prompts for common tasks
- Store in `.github/prompts` directory
- Share across team members
- Version control integration

### Chat Modes
- Define operation boundaries and tool access
- Create specialized modes (read-only planning, etc.)
- Configure interaction patterns
- Customize AI behavior per mode

## Editor AI Features

### Code Completion Features
- **Real-time suggestions**: Context-aware code completions
- **Comment-driven prompts**: Write instructions in comments for code generation
- **Multi-language support**: Intelligent suggestions across programming languages

### Inline Chat (`Ctrl+I`)
- **Natural language requests**: Use conversational prompts in editor
- **Context awareness**: Leverages selected code and surrounding context
- **Chat variables support**: Reference files, symbols, and tools
- **Slash command integration**: Use shortcuts for common operations

### Context Menu Actions
Right-click in editor for quick access to:
- **Explain code**: Get detailed explanations of selected code
- **Generate tests**: Create test cases for functions and methods
- **Review code**: AI-powered code review and suggestions
- **Fix issues**: Automated bug fixing and improvement suggestions

### Smart Features
- **AI-powered rename**: Intelligent symbol renaming with `F2`
- **Code Actions**: Enhanced lightbulb suggestions for error fixing
- **Semantic analysis**: Deep code understanding for better suggestions

## Source Control Integration

### Git Workflow Features
- **`#changes`** - Add current source control changes as context
- **Commit context** - Include specific commits in chat prompts
- **Commit summaries** - Right-click commits for AI-generated summaries
- **Commit messages** - Auto-generate descriptive commit messages
- **PR descriptions** - Create pull request titles and descriptions

### GitHub Integration
- **`@github` participant** - Query issues, PRs, and repositories
- **Repository analysis** - Cross-repository code insights
- **Issue management** - AI assistance with GitHub issue workflows

## Code Review (Experimental)

### Review Features
- **Review and Comment**: Quick review pass for selected code blocks
- **Copilot Code Review**: Comprehensive review of uncommitted changes
- **Inline feedback**: Comments directly in editor with actionable suggestions
- **Context-aware analysis**: Leverages project patterns and best practices

## Search and Settings

### Enhanced Search
- **Semantic search** (`search.searchView.semanticSearchBehavior`): AI-powered search results
- **Settings search** (`workbench.settings.showAISearchToggle`): Intelligent settings discovery
- **Query generation**: Natural language to search query translation

## Testing Features

### Test Generation
- **`/tests`** - Generate comprehensive test suites
- **`/setupTests`** - Framework setup and configuration guidance
- **`/fixTestFailure`** - Intelligent test failure resolution
- **Test coverage** - Generate tests for uncovered functions (experimental)

### Testing Tips
- Specify preferred testing frameworks in prompts
- Request specific test types (unit, integration, end-to-end)
- Include testing library preferences for better suggestions

## Debugging Features

### Debug Assistance
- **`/fix`** - Code problem resolution and optimization suggestions
- **`/fixTestFailure`** - Test-specific debugging assistance
- **`/startDebugging`** - Debug configuration generation and session startup
- **`copilot-debug` command** - Terminal command for streamlined debugging

### Debug Tips
- Provide context about specific fix requirements
- Watch for Copilot Code Actions indicating available fixes
- Use detailed error descriptions for better solutions

## Project Scaffolding

### Creation Tools
- **Agent mode** - Natural language project creation
- **`/new`** - Structured project and file scaffolding
- **`/newNotebook`** - Jupyter notebook generation with requirements

### Examples
- `Create a svelte web application to track my tasks`
- `/new Express app using typescript and svelte`
- `/newNotebook get census data and preview key insights with Seaborn`

## Terminal Integration

### Terminal AI Features
- **`Ctrl+I`** - Terminal inline chat for shell command assistance
- **`@terminal`** - Terminal-focused chat participant
- **`@terminal /explain`** - Command explanation and documentation

### Examples
- `how many cores on this machine?`
- `@terminal list the 5 largest files in this workspace`
- `@terminal /explain top shell command`

## Python and Notebook Support

### Jupyter Integration
- **Generate (`Ctrl+I`)** - Create code or Markdown blocks in notebooks
- **`#` variables** - Attach kernel variables for context-aware responses
- **Native REPL** - Inline chat in Python REPL with command execution
- **Edit/Agent modes** - Comprehensive notebook editing capabilities

### Python-Specific Features
- **Variable context**: Leverage Jupyter kernel state
- **Data science workflows**: Specialized assistance for data analysis
- **Library integration**: Enhanced support for pandas, numpy, matplotlib

## Related Documentation
- [Copilot Setup](../setup.md)
- [Copilot Chat](../chat/copilot-chat.md)
- [Agent Mode](../chat/agent-mode.md)
- [Tips and Tricks](../tips-and-tricks.md)
- [Copilot Settings](copilot-settings.md)
- [Workspace Context](workspace-context.md)

## External Resources
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/)
- [Getting Started Tutorial](https://code.visualstudio.com/docs/copilot/getting-started)

This comprehensive feature reference serves as your complete guide to leveraging GitHub Copilot's full potential in Visual Studio Code, from basic completions to advanced AI-powered development workflows.
