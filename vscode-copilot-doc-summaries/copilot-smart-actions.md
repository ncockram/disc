# Copilot Smart Actions in Visual Studio Code

**Source:** https://code.visualstudio.com/docs/copilot/copilot-smart-actions

## Summary

Copilot smart actions provide AI assistance for common development scenarios without requiring manual prompt writing. These actions are integrated throughout the VS Code UI and offer quick access to AI-powered solutions for tasks like generating commit messages, documentation, tests, fixing errors, and performing code reviews.

## Overview

Smart actions enable developers to:
- Generate commit messages and PR information automatically
- Rename symbols with AI suggestions
- Create documentation and tests
- Fix coding and testing errors
- Explain and review code
- Generate alt text for Markdown images
- Search semantically and find settings with AI

## Core Smart Actions

### Generate a Commit Message and PR Information

#### Commit Message Generation
- **Access**: Use sparkle icon in Source Control view
- **Functionality**: Generates commit messages based on code changes
- **Integration**: Works directly in the Source Control input box

#### Pull Request Information
- **Requirements**: GitHub PR extension
- **Capabilities**: Generates PR titles and descriptions
- **Context**: Analyzes changes across the entire pull request

### Rename Symbols

#### AI-Powered Renaming
- **Context Awareness**: Suggests names based on symbol context and codebase
- **Integration**: Works with VS Code's rename functionality
- **Language Support**: Available across multiple programming languages

#### Process
1. Initiate symbol rename operation
2. Copilot analyzes context and usage patterns
3. Suggests appropriate new names
4. Apply suggestions with confirmation

### Generate Alt Text for Images in Markdown

#### Accessibility Enhancement
- **Purpose**: Improves accessibility of Markdown documents
- **Integration**: Code Action (lightbulb) menu

#### Usage Steps
1. Open Markdown file
2. Position cursor on image link
3. Select Code Action icon
4. Choose "Generate alt text" option
5. For existing alt text, use "Refine alt text"

### Generate Documentation

#### Automated Documentation Creation
- **Access**: Right-click context menu → Copilot → Generate Docs
- **Scope**: Works with or without code selection
- **Language Support**: Multiple programming languages

#### Features
- Generates code comments and documentation
- Understands function signatures and class structures
- Creates appropriate documentation formats for different languages
- Supports JSDoc, Python docstrings, and other standards

### Generate Tests

#### Test Generation Capabilities
- **Access**: Right-click context menu → Copilot → Generate Tests
- **File Management**: Creates new test files or updates existing ones
- **Context Awareness**: Analyzes code structure for appropriate tests

#### Process
1. Select code to test (optional)
2. Use context menu to generate tests
3. Copilot creates comprehensive test coverage
4. Refine tests with additional prompts if needed

### Explain Code

#### Code Understanding Assistance
- **Purpose**: Provides detailed explanations of code functionality
- **Access**: Select code → Right-click → Copilot → Explain
- **Output**: Clear, natural language explanations

#### Benefits
- Helps understand complex algorithms
- Explains unfamiliar code patterns
- Assists in code review processes
- Educational tool for learning new concepts

### Fix Coding Errors

#### Error Resolution Features
- **Integration**: Works with compile and lint errors
- **Access Methods**:
  - Right-click → Copilot → Fix
  - Sparkle icon on error squiggles
  - Code Actions menu

#### Process
1. Identify error (red squiggle)
2. Click sparkle icon or use context menu
3. Select "Fix using Copilot"
4. Review and apply suggested solutions

### Fix Testing Errors

#### Test Failure Resolution
- **Integration**: Test Explorer integration
- **Features**: 
  - Fix Test Failure button (sparkle icon)
  - `/fixTestFailure` command in chat
  - Agent mode automatic fixing

#### Agent Mode Integration
- Monitors test output automatically
- Attempts fixes for failing tests
- Reruns tests after applying fixes
- Provides iterative improvement

### Fix Terminal Errors

#### Command Failure Assistance
- **Trigger**: Automatic sparkle appears after failed commands
- **Functionality**: Explains what went wrong and suggests solutions
- **Integration**: Terminal gutter indicators

#### Benefits
- Reduces time spent debugging command failures
- Provides learning opportunities
- Suggests alternative approaches

### Review Code

#### Code Review Capabilities
- **Editor Integration**: Select code → Right-click → Copilot → Review and Comment
- **Pull Request Integration**: Requires GitHub Pull Requests extension
- **Output**: Creates review comments in Comments panel and inline

#### Features
- **Block Review**: Review selected code sections
- **PR Review**: Comprehensive pull request analysis
- **Comment Generation**: Creates structured review feedback
- **Inline Display**: Shows comments directly in editor

## Advanced Features

### Semantic Search Results (Preview)

#### Enhanced Search Capabilities
- **Purpose**: Find semantically relevant results beyond exact text matches
- **Use Cases**: 
  - Concept-based searches
  - Unknown terminology exploration
  - Related code discovery

#### Configuration
- **Setting**: `search.searchView.semanticSearchBehavior`
- **Options**: Automatic or manual activation
- **Integration**: Search view enhancement

#### Keyword Suggestions
- **Setting**: `search.searchView.keywordSuggestions`
- **Functionality**: AI-generated alternative search terms
- **Chat Integration**: Reference results with `#searchResults`

### Search Settings with AI (Experimental)

#### Natural Language Settings Discovery
- **Purpose**: Find settings using descriptive queries
- **Example**: "increase text size" → font size settings
- **Setting**: `workbench.settings.showAISearchToggle`

#### Usage
1. Enable AI search toggle in Settings editor
2. Use natural language to describe desired setting
3. View AI-generated setting suggestions
4. Toggle feature on/off as needed

## Integration Points

### Source Control Integration
- Commit message generation
- PR title and description creation
- Code change analysis

### Test Explorer Integration
- Automatic test failure detection
- Fix suggestions for failing tests
- Iterative test improvement

### GitHub Integration
- Pull request review capabilities
- Repository context awareness
- Extension ecosystem compatibility

### Editor Integration
- Context menu actions
- Sparkle icon indicators
- Code Actions integration
- Inline chat activation

## Configuration and Settings

### Enabling Features
- Most smart actions are enabled by default
- Specific features may require additional settings
- Preview features need explicit enablement

### Customization Options
- Configure semantic search behavior
- Enable/disable specific smart actions
- Adjust AI search toggle visibility

## Best Practices

### Effective Usage
- **Context Selection**: Select relevant code for better suggestions
- **Iterative Refinement**: Use additional prompts to improve results
- **Review Before Applying**: Always review AI-generated content
- **Learning Opportunity**: Use explanations to understand new concepts

### Workflow Integration
- **Commit Messages**: Use for consistent, descriptive commit messages
- **Documentation**: Generate initial docs, then customize as needed
- **Testing**: Create comprehensive test suites with AI assistance
- **Code Review**: Supplement human review with AI insights

## Troubleshooting

### Common Issues
- **No Sparkle Icon**: Check Copilot authentication and subscription
- **Irrelevant Suggestions**: Provide more context or refine selection
- **Missing Actions**: Ensure extensions are installed and enabled

### Performance Optimization
- **Context Size**: Limit selections to relevant code sections
- **Specific Queries**: Use precise language for better results
- **Iterative Approach**: Break complex tasks into smaller steps

## Next Steps

### Learning Resources
- [Copilot Quickstart](https://code.visualstudio.com/docs/copilot/getting-started)
- [Agent Mode Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [GitHub Pull Requests Extension](https://marketplace.visualstudio.com/items/?itemName=GitHub.vscode-pull-request-github)

### Advanced Features
- Explore chat modes for complex tasks
- Configure custom instructions for consistent results
- Integrate with team workflows and standards

## Related Documentation

- [Copilot Chat Features](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [Code Completions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions)
- [Testing with Copilot](https://code.visualstudio.com/docs/copilot/guides/test-with-copilot)
- [Debugging with Copilot](https://code.visualstudio.com/docs/copilot/guides/debug-with-copilot)
- [Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
