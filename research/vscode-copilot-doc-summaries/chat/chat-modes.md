# VS Code Copilot Chat Modes Overview

**Source:** [VS Code Copilot Chat Modes](https://code.visualstudio.com/docs/copilot/chat/chat-modes)

## Introduction

GitHub Copilot Chat in VS Code offers three distinct modes, each optimized for different types of interactions and tasks. Understanding when and how to use each mode will significantly improve your AI-assisted development workflow.

## Mode Overview

| Mode | Purpose | Best For | Context Scope |
|------|---------|----------|---------------|
| **Ask** | Information and guidance | Learning, explanations, advice | Current conversation |
| **Edit** | Targeted code modifications | Specific changes, refactoring | Selected files/code |
| **Agent** | Autonomous coding workflows | Complex tasks, multi-file changes | Entire workspace |

## Ask Mode

### Purpose and Use Cases

Ask mode is designed for **information gathering** and **learning**:
- Getting explanations of code or concepts
- Understanding best practices and patterns
- Asking questions about frameworks and libraries
- Exploring different approaches to problems
- Learning about new technologies

### Key Features

**Non-destructive interaction:**
- No direct code modifications
- Safe exploration of ideas
- Multiple solution alternatives
- Educational explanations

**Conversational flow:**
- Natural question-and-answer format
- Follow-up questions encouraged
- Context builds throughout conversation
- Learning-focused responses

### Example Interactions

```
// Learning about patterns
What are the benefits of using the Repository pattern in this codebase?

// Understanding frameworks  
How does React Context work and when should I use it?

// Exploring alternatives
What are different ways to handle authentication in Node.js applications?

// Code explanation
/explain this middleware function and how it processes requests
```

### When to Use Ask Mode

- **Learning new concepts** or technologies
- **Understanding existing code** without changing it
- **Exploring options** before implementation
- **Getting advice** on architecture decisions
- **Debugging understanding** of complex systems

[Detailed Ask Mode Guide →](./chat-ask-mode.md)

## Edit Mode

### Purpose and Use Cases

Edit mode is optimized for **targeted code modifications**:
- Making specific changes to existing code
- Refactoring functions or components
- Adding features to current files
- Fixing bugs and issues
- Implementing requested modifications

### Key Features

**Precise code modifications:**
- Direct file editing capabilities
- Diff-based change previews
- Selective accept/reject options
- Multi-file coordination

**Change management:**
- Clear before/after comparisons
- Granular control over edits
- Undo/redo functionality
- Version control integration

### Example Interactions

```
// Targeted refactoring
Refactor this function to use async/await instead of callbacks

// Feature addition
Add input validation to this form component

// Bug fixes
Fix the memory leak in this event listener setup

// Code improvement
Optimize this database query for better performance
```

### When to Use Edit Mode

- **Specific code changes** with clear requirements
- **Refactoring existing code** while preserving functionality
- **Adding features** to current components
- **Bug fixes** with targeted scope
- **Code improvements** and optimizations

[Detailed Edit Mode Guide →](./copilot-edits.md)

## Agent Mode

### Purpose and Use Cases

Agent mode provides **autonomous coding capabilities**:
- Complex multi-file implementations
- Feature development from high-level requirements
- Project scaffolding and setup
- Cross-cutting concerns and integrations
- End-to-end workflow automation

### Key Features

**Autonomous decision making:**
- Multi-step planning and execution
- Tool integration (terminal, file system)
- Iterative problem solving
- Self-correction and adaptation

**Workspace-level operations:**
- Multi-file coordination
- Project structure understanding
- Dependency management
- Build system integration

### Example Interactions

```
// High-level feature requests
Add user authentication with OAuth, including login/logout UI and protected routes

// Project setup
Create a React TypeScript project with ESLint, Prettier, and Jest testing setup

// Complex integrations
Integrate this application with a PostgreSQL database using Prisma ORM

// Architecture changes
Refactor the application to use a microservices architecture with Docker
```

### When to Use Agent Mode

- **Complex features** requiring multiple files
- **Project initialization** and scaffolding
- **Architecture changes** affecting many components
- **Integration tasks** involving external tools
- **End-to-end implementations** from requirements

[Detailed Agent Mode Guide →](./chat-agent-mode.md)

## Mode Selection Guidelines

### Decision Framework

**Choose Ask Mode when:**
- You need to understand something
- You're exploring options or alternatives
- You want explanations without changes
- You're learning new concepts
- You need advice or guidance

**Choose Edit Mode when:**
- You have specific code to modify
- You know exactly what needs to change
- You want to refactor existing functionality
- You need targeted bug fixes
- You want precise control over changes

**Choose Agent Mode when:**
- You have high-level requirements
- Multiple files need coordination
- You need complex integrations
- You want automated workflows
- The task involves tools and external systems

### Task Complexity Mapping

**Simple Tasks (Ask Mode):**
- "How does this function work?"
- "What's the best practice for error handling?"
- "Explain the difference between these approaches"

**Medium Tasks (Edit Mode):**
- "Add error handling to this function"
- "Refactor this component to use hooks"
- "Fix the performance issue in this query"

**Complex Tasks (Agent Mode):**
- "Add a complete user management system"
- "Set up CI/CD pipeline for this project"
- "Migrate from REST API to GraphQL"

## Mode Switching

### Within Conversations

You can switch modes during a conversation:

```
// Start with Ask mode
How should I implement caching in this API?

// Switch to Edit mode after understanding
Now add Redis caching to the user endpoints

// Switch to Agent mode for broader implementation  
Implement caching across the entire application with configuration management
```

### Mode-Specific Commands

Use slash commands to clarify intent:

```
// Ask mode patterns
/explain this authentication flow
/help with React performance optimization

// Edit mode patterns  
/fix the validation errors in this form
/refactor this class to use composition

// Agent mode patterns
/new feature: real-time chat functionality
/setup testing framework for the project
```

## Advanced Mode Features

### Custom Chat Modes

Create custom modes for specific workflows:

**Example: Code Review Mode**
```json
{
  "name": "Code Review",
  "description": "Focused on code quality and best practices",
  "defaultContext": ["#selection", "#relatedFiles"],
  "suggestedPrompts": [
    "Review this code for potential issues",
    "Check for security vulnerabilities",
    "Suggest performance improvements"
  ]
}
```

**Example: Documentation Mode**
```json
{
  "name": "Documentation",  
  "description": "Generate and improve documentation",
  "defaultContext": ["#file", "#symbols"],
  "suggestedPrompts": [
    "Generate API documentation",
    "Create usage examples",
    "Write README sections"
  ]
}
```

### Mode Configuration

Customize mode behavior through settings:

```json
{
  "copilot.chat.askMode.includeContext": "auto",
  "copilot.chat.editMode.previewChanges": true,
  "copilot.chat.agentMode.maxIterations": 5,
  "copilot.chat.agentMode.autoApproveTools": false
}
```

## Best Practices by Mode

### Ask Mode Best Practices

1. **Be curious and exploratory**
   - Ask follow-up questions
   - Request examples and alternatives
   - Seek understanding of underlying concepts

2. **Provide good context**
   - Include relevant code snippets
   - Reference specific files or functions
   - Explain your current understanding

3. **Learn progressively**
   - Start with broad concepts
   - Drill down into specifics
   - Connect new knowledge to existing code

### Edit Mode Best Practices

1. **Be specific about changes**
   - Clearly describe desired modifications
   - Provide current state context
   - Specify constraints and requirements

2. **Review changes carefully**
   - Examine diffs before accepting
   - Test modifications thoroughly
   - Consider impact on related code

3. **Iterate on improvements**
   - Refine changes through follow-up edits
   - Ask for alternative implementations
   - Optimize for readability and performance

### Agent Mode Best Practices

1. **Provide clear high-level goals**
   - Describe desired outcomes
   - Specify technical constraints
   - Include business requirements

2. **Monitor and guide the process**
   - Review intermediate steps
   - Approve tool executions
   - Provide feedback on direction

3. **Verify comprehensive results**
   - Test end-to-end functionality
   - Review all generated files
   - Validate against requirements

## Common Workflows

### Learning to Implementation

1. **Ask Mode**: Understand the problem and explore solutions
2. **Ask Mode**: Learn about relevant patterns and best practices  
3. **Edit Mode**: Implement specific changes based on learning
4. **Agent Mode**: Scale implementation across the project

### Bug Investigation and Resolution

1. **Ask Mode**: Understand the problem and potential causes
2. **Edit Mode**: Make targeted fixes to specific issues
3. **Agent Mode**: Implement comprehensive testing and prevention

### Feature Development

1. **Ask Mode**: Explore requirements and design approaches
2. **Agent Mode**: Implement the complete feature across files
3. **Edit Mode**: Refine specific implementations and fix issues
4. **Ask Mode**: Learn about testing and deployment strategies

## Mode-Specific Shortcuts

### Keyboard Shortcuts

- **Quick Chat** (`Ctrl+Shift+I`): Opens in Ask mode by default
- **Inline Chat** (`Ctrl+I`): Context-aware, typically Edit mode
- **Chat View** (`Ctrl+Alt+I`): Full mode selection available

### Voice and Natural Language

Each mode responds to natural language cues:

**Ask Mode Triggers:**
- "How do I...", "What is...", "Why does...", "Explain..."

**Edit Mode Triggers:**  
- "Change this to...", "Fix...", "Refactor...", "Add..."

**Agent Mode Triggers:**
- "Create a complete...", "Set up...", "Build...", "Implement..."

## Related Resources

- **[Ask Mode Detailed Guide](./chat-ask-mode.md)** - In-depth Ask mode features
- **[Edit Mode Detailed Guide](./copilot-edits.md)** - Comprehensive Edit mode workflow
- **[Agent Mode Detailed Guide](./chat-agent-mode.md)** - Advanced Agent mode capabilities
- **[Chat Context Management](./copilot-chat-context.md)** - Optimizing context for each mode
- **[Getting Started Guide](./getting-started-chat.md)** - Hands-on tutorial using all modes

---

*Each chat mode serves a distinct purpose in the development workflow. Mastering when and how to use each mode will significantly enhance your productivity with GitHub Copilot Chat.*
