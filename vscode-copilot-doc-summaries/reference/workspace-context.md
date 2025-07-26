# Making Chat an Expert in Your Workspace

## Overview

GitHub Copilot's workspace context features transform AI assistance from generic code help into intelligent, project-aware guidance. This comprehensive guide covers how Copilot understands your workspace, optimizes context retrieval, and provides accurate, codebase-specific assistance.

## Understanding @workspace vs #codebase

### @workspace Participant
**Dedicated chat participant for codebase questions**
- **Focused approach**: Takes control of user prompts for codebase-specific answers
- **Streamlined workflow**: Optimized for asking questions about your code
- **Mode restriction**: Only available in ask mode
- **Direct interaction**: "Ask and answer" pattern for workspace queries

**Example Usage:**
```
@workspace how can I validate a date?
@workspace where is database connection string configured?
@workspace how is authentication implemented?
```

### #codebase Tool
**Flexible tool for adding codebase context**
- **Context enhancement**: Performs codebase search and adds relevant code as context
- **LLM control**: Language model remains in control, can combine with other tools
- **Mode flexibility**: Works in ask, edit, and agent modes
- **Editing scenarios**: Ideal for code modification and improvement tasks

**Example Usage:**
```
add a tooltip to this button, consistent with other button #codebase
add unit tests and run them #codebase
How do I build this #codebase?
```

### Recommendation
**Use `#codebase` for maximum flexibility** - it provides broader applicability across different chat modes and can be combined with other tools for complex workflows.

### Enhanced Effectiveness
Enable `github.copilot.chat.codesearch.enabled` setting to make `#codebase` more effective at finding relevant code snippets. This setting is enabled by default and significantly improves context retrieval quality.

## Effective Prompt Examples

### Finding Existing Code
**Configuration and Setup Queries:**
- `@workspace where is database connecting string configured?` - Locates database configuration files and connection setup
- `@workspace where are tests defined?` - Identifies test suites, cases, and related configurations
- `@workspace how can I validate a date?` - Finds existing date validation helpers and utilities

### Planning Complex Edits
**Architecture and Implementation Guidance:**
- `@workspace how can I add a rich tooltip to a button?` - Provides implementation plan using existing tooltip components
- `@workspace add a new API route for the forgot password form` - Outlines route addition and integration approach
- `@workspace how can I implement user authentication?` - Comprehensive authentication strategy based on existing patterns

### Understanding System Architecture
**High-Level Concept Exploration:**
- `@workspace how is authentication implemented?` - Authentication flow overview with code references
- `@workspace which API routes depend on this service?` - Service dependency analysis and route mapping
- `How do I build this #codebase?` - Build process steps from documentation and scripts

## Context Sources and Data

### Comprehensive Context Retrieval
Copilot searches through the same sources developers use for codebase navigation:

**File System Analysis:**
- All [indexable files](workspace-context.md#what-content-is-included-in-the-workspace-index) in workspace (excluding `.gitignore` entries)
- Complete directory structure with nested folder and file names
- Symbol definitions and declarations across the workspace

**Enhanced Context Sources:**
- **GitHub Code Search Index**: For GitHub repositories with remote indexing enabled
- **Editor Context**: Currently selected text and visible content in active editor
- **IntelliSense Integration**: Symbol information, function signatures, and type definitions

**Important Note:** `.gitignore` filtering is bypassed when files are explicitly opened or text is selected within ignored files.

## Context Retrieval Process

### Intelligent Context Selection
Your workspace may be too large to pass entirely to GitHub Copilot, so `@workspace` uses sophisticated algorithms to extract the most relevant information:

**Phase 1: Question Analysis**
- Analyzes user question and conversation history
- Considers workspace structure and currently selected code
- Determines information types needed for accurate response

**Phase 2: Context Collection**
- **Local Search**: Finds relevant code snippets using workspace indexing
- **Remote Search**: Leverages [GitHub's code search](https://github.blog/2023-02-06-the-technology-behind-githubs-new-code-search) for indexed repositories
- **IntelliSense Integration**: Adds function signatures, parameters, and type information
- **Symbol Resolution**: Includes related definitions and implementations

**Phase 3: Response Generation**
- Uses collected context for accurate, project-specific answers
- Prioritizes most relevant context if size limits are reached
- Includes references to files, ranges, and symbols in responses
- Provides direct links from responses to corresponding code locations

### Reference Integration
Responses include comprehensive references:
- **File Links**: Direct navigation to referenced files
- **Line Ranges**: Specific code sections used for context
- **Symbol References**: Functions, classes, and variables mentioned
- **Code Snippets**: Exact code examples provided to Copilot

## Managing Workspace Indexes

### Index Types and Selection

Copilot maintains workspace indexes to enable fast, accurate codebase search. View your current index type and status in the Copilot status dashboard in the Status Bar.

### Remote Index (Recommended)
**GitHub-Hosted Indexing for Optimal Performance**

**Setup Process:**
1. **Sign in**: Authenticate with GitHub account in VS Code
2. **Build Index**: Run `Build Remote Workspace Index` command from Command Palette (`Ctrl+Shift+P`)
3. **Monitor Progress**: Check status in Copilot status dashboard

**Benefits:**
- Fast search even for large codebases
- Automatic updates when code is pushed to GitHub
- Superior search quality and relevance
- No local storage requirements

**Requirements:**
- Git repository with GitHub remote
- Code pushed to GitHub (kept relatively up-to-date)
- GitHub account authentication in VS Code

### Local Index
**Machine-Stored Indexing for Private or Offline Work**

**Automatic Setup** (< 750 indexable files):
- Copilot automatically builds advanced local index
- No manual intervention required
- Continuous updates as files change

**Manual Setup** (750-2500 indexable files):
- Run `Build local workspace index` command from Command Palette
- One-time setup process
- Monitor progress in Copilot status dashboard

**Limitations:**
- Limited to 2500 indexable files maximum
- Local storage requirements
- Rebuild time when switching branches or making extensive changes

### Basic Index
**Fallback for Large Projects**

**Automatic Activation:**
- Projects with > 2500 indexable files
- No remote index available
- Simpler search algorithms optimized for large codebases

**Performance Characteristics:**
- Works adequately for many workspace questions
- Reduced search sophistication compared to advanced indexes
- May struggle with complex or nuanced queries

**Improvement Path:**
- Upgrade to remote index for better performance
- Consider repository restructuring for better indexing

### Indexed Content Types

**Included Content:**
- All relevant text files in project scope
- Source code across multiple programming languages
- Configuration files, documentation, and scripts
- Files not excluded by `files.exclude` setting or `.gitignore`

**Excluded Content:**
- Binary files (images, PDFs, executables)
- Temporary files (`.tmp`, `.out`, build artifacts)
- Files matching `.gitignore` patterns
- Files excluded by VS Code `files.exclude` setting

## Optimization Tips for Workspace Context

### Effective Prompting Strategies

**Specificity and Clarity:**
- **Be explicit**: Avoid vague terms like "this" that could refer to multiple contexts
- **Use domain terminology**: Include terms likely to appear in your codebase or documentation
- **Provide implementation details**: Specify technologies, frameworks, and patterns when relevant

**Context Enhancement:**
- **Review references**: Check response references to ensure file relevance
- **Iterate on questions**: Refine prompts if initial results aren't comprehensive
- **Explicit context**: Select relevant code or mention specific files (`#editor`, `#selection`, `#<filename>`)

**Multi-Reference Queries:**
- **Comprehensive searches**: "find exceptions without a catch block"
- **Usage patterns**: "provide examples of how handleError is called"
- **Avoid broad analysis**: Don't expect exhaustive code analysis ("how many times is this function invoked?")

### Question Optimization Techniques

**Effective Patterns:**
```
✅ "@workspace where is the JWT token validation implemented?"
✅ "@workspace how do I add logging to the payment processing module?"
✅ "@workspace what testing framework is used for the API layer?"
```

**Patterns to Avoid:**
```
❌ "@workspace what does this do?" (ambiguous reference)
❌ "@workspace find all bugs" (too broad)
❌ "@workspace who wrote this code?" (beyond code scope)
```

### Context Scope Management

**Appropriate Expectations:**
- **Code location and structure**: Finding where functionality is implemented
- **Implementation patterns**: Understanding how features are built
- **Integration guidance**: Learning how to extend existing functionality
- **Configuration discovery**: Locating setup and configuration files

**Limitations:**
- **Comprehensive analysis**: Avoid expecting complete codebase audits
- **External information**: Don't assume knowledge beyond the code itself
- **Quantitative analysis**: Limited ability to count occurrences across large codebases
- **Historical information**: No access to commit history or authorship details

## Advanced Workspace Features

### Integration with Development Workflow

**Code Navigation Enhancement:**
- **Symbol following**: Use workspace context to understand symbol relationships
- **Dependency analysis**: Identify how components interact across the codebase
- **Architecture understanding**: Gain insights into system design and patterns

**Refactoring Support:**
- **Impact analysis**: Understand what code might be affected by changes
- **Pattern identification**: Find similar implementations for consistency
- **Integration points**: Identify where new code should connect to existing systems

### Team Collaboration Benefits

**Onboarding Acceleration:**
- **Codebase familiarization**: Help new team members understand project structure
- **Pattern learning**: Teach existing coding patterns and conventions
- **Knowledge transfer**: Capture institutional knowledge in AI-accessible format

**Knowledge Sharing:**
- **Documentation generation**: Create documentation based on actual implementation
- **Best practice identification**: Learn from successful patterns in the codebase
- **Consistency maintenance**: Ensure new code follows established patterns

## Related Documentation
- [Copilot Chat Context](../chat/copilot-chat-context.md)
- [Copilot Chat Tutorial](../chat/getting-started-chat.md)
- [Copilot Chat Overview](../chat/copilot-chat.md)
- [VS Code Copilot Features](copilot-vscode-features.md)
- [Tips and Tricks](../tips-and-tricks.md)

## External Resources
- [GitHub Code Search Documentation](https://docs.github.com/en/search-github/github-code-search/about-github-code-search)
- [VS Code Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)
- [GitHub Copilot Chat in GitHub.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/github-copilot-enterprise/copilot-chat-in-github/using-github-copilot-chat-in-githubcom)

Workspace context transforms GitHub Copilot from a general programming assistant into an expert collaborator who understands your specific codebase, enabling more accurate suggestions, better architectural guidance, and seamless integration with your existing development patterns.
