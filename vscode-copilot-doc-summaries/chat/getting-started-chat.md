# Getting Started with VS Code Copilot Chat

**Source:** [VS Code Copilot Chat Getting Started](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)

## Introduction

This tutorial walks you through using GitHub Copilot Chat in Visual Studio Code to build a Node.js web application. You'll learn how to use chat participants, context variables, and different chat modes to accelerate your development workflow.

## Prerequisites

Before starting this tutorial:

- Install the latest version of [Visual Studio Code](https://code.visualstudio.com/download)
- Have access to [GitHub Copilot](../setup.md) (Free plan includes monthly chat interactions)
- Basic familiarity with Node.js and web development concepts

## Setting Up Your Environment

### Step 1: Create Project Structure

1. **Create a new folder** for your project:
   ```bash
   mkdir copilot-chat-tutorial
   cd copilot-chat-tutorial
   ```

2. **Open in VS Code**:
   ```bash
   code .
   ```

3. **Open Chat View** using `Ctrl+Alt+I` or click the Copilot icon in the Activity Bar

### Step 2: Initialize Node.js Project

In the Chat view, ask Copilot to help set up your project:

```
@workspace /new create a new Node.js project with Express.js for a simple web application
```

**What happens:**
- `@workspace` tells Copilot to consider your project context
- `/new` indicates you're creating something new
- The request is specific about the technology stack

Copilot will suggest creating essential files like `package.json`, a basic Express server, and project structure.

## Building the Application

### Step 3: Create the Express Server

Ask Copilot to create a basic server:

```
Create a simple Express.js server that serves static files and has a basic route for the homepage
```

**Expected response:**
Copilot will generate code for:
- Express server setup
- Static file serving
- Basic route handling
- Port configuration

**Apply the code:**
1. Review the suggested code
2. Click **Apply in Editor** or copy to create `server.js`
3. Copilot may suggest additional files like `public/index.html`

### Step 4: Add Frontend Assets

Use context variables to reference your server file:

```
#file:server.js Based on this server setup, create a simple HTML page with CSS styling for the homepage
```

**What the `#file:` syntax does:**
- Includes the specified file as context
- Helps Copilot understand your existing code structure
- Provides better, more relevant suggestions

### Step 5: Implement Dynamic Routes

Ask for more complex functionality:

```
Add a /api/data route that returns JSON data about products. Include sample product data with name, price, and description.
```

**Copilot will suggest:**
- Route handler for `/api/data`
- Sample JSON data structure
- Proper Express middleware setup
- Error handling patterns

## Using Different Chat Modes

### Ask Mode - Understanding Code

Select some code in your `server.js` file and use **Inline Chat** (`Ctrl+I`):

```
/explain this middleware setup
```

**Benefits of Ask Mode:**
- Get explanations without modifying code
- Understand frameworks and patterns
- Learn best practices and alternatives

### Edit Mode - Making Changes

To modify existing code, switch to Edit mode in the Chat view:

```
/fix Add error handling to all routes and implement proper status codes
```

**Edit Mode capabilities:**
- Targeted code modifications
- Multiple file changes
- Preserve existing functionality
- Structured diff previews

### Agent Mode - Complex Tasks

For larger changes, use Agent mode:

```
Add user authentication with login/logout routes, session management, and protected routes for admin features
```

**Agent Mode advantages:**
- Autonomous decision making
- Multi-file coordination
- Tool integration (terminal, file system)
- Iterative problem solving

## Working with Context

### File Context

Reference multiple files for better suggestions:

```
#file:server.js #file:package.json Add database integration using MongoDB with proper error handling and connection management
```

### Selection Context

1. **Select code** in the editor (e.g., a specific function)
2. **Use Inline Chat** (`Ctrl+I`)
3. **Ask for modifications**:
   ```
   Refactor this function to use async/await instead of callbacks
   ```

### Workspace Context

Ask questions about your entire project:

```
@workspace What potential security issues should I address in this web application?
```

## Advanced Features

### Using Slash Commands

Experiment with different slash commands:

- **`/tests`** - Generate test cases:
  ```
  /tests Create unit tests for the API routes using Jest
  ```

- **`/doc`** - Generate documentation:
  ```
  /doc Create API documentation for all routes
  ```

- **`/refactor`** - Improve code structure:
  ```
  /refactor Organize the code into separate modules for routes, middleware, and database
  ```

### Chat Participants

Try different specialized participants:

- **`@terminal`** for command-line tasks:
  ```
  @terminal How do I deploy this Node.js app to Heroku?
  ```

- **`@vscode`** for editor help:
  ```
  @vscode How can I set up debugging for this Node.js application?
  ```

### Context Variables

Use various context types:

- **`#selection`** - Current editor selection
- **`#terminalLastCommand`** - Last terminal output
- **`#codebase`** - Project-wide context for large questions

## Testing Your Application

### Step 6: Add Testing

Ask Copilot to help with testing:

```
#file:server.js Create comprehensive tests for all routes using Jest and supertest. Include tests for both successful responses and error cases.
```

### Step 7: Run and Debug

Use the terminal integration:

1. **Open terminal** (`Ctrl+``)
2. **Install dependencies**: `npm install`
3. **Start the server**: `npm start`
4. **Test in browser**: Navigate to `http://localhost:3000`

If you encounter issues, use Inline Chat in the terminal:

```
@terminal The server won't start. How do I debug Node.js connection issues?
```

## Best Practices from This Tutorial

### Effective Prompting
1. **Be specific** - "Create Express server" vs "Create web application"
2. **Use context** - Reference files and selections for better results
3. **Iterate** - Build complexity gradually through follow-up questions

### Code Quality
1. **Review suggestions** - Always examine generated code before applying
2. **Test thoroughly** - Copilot provides starting points, not final solutions
3. **Follow conventions** - Ask for specific coding standards and patterns

### Workflow Integration
1. **Start broad, get specific** - Begin with architecture, then implement details
2. **Use appropriate modes** - Ask for learning, Edit for changes, Agent for complex tasks
3. **Leverage participants** - Use specialized knowledge when needed

## Common Patterns

### Project Initialization
```
@workspace /new Create a [technology] project with [specific requirements]
```

### Code Enhancement
```
#file:existing.js Add [functionality] with proper error handling and [specific pattern]
```

### Learning and Exploration
```
/explain [concept] in the context of this #file:example.js
```

### Testing and Documentation
```
/tests Generate tests for #selection with edge cases
/doc Create documentation for #file:api.js
```

## Next Steps

After completing this tutorial:

1. **Explore [Chat Context Management](./copilot-chat-context.md)** - Learn advanced context techniques
2. **Try [Different Chat Modes](./chat-modes.md)** - Master Ask, Edit, and Agent modes
3. **Read [Prompt Crafting Guide](../guides/prompt-crafting.md)** - Write more effective prompts
4. **Set up [Copilot Customization](../copilot-customization.md)** - Personalize your experience

## Troubleshooting

### Common Issues

**Copilot suggestions seem irrelevant:**
- Provide more specific context with `#file:` or `#selection`
- Break complex requests into smaller, focused questions
- Use appropriate chat participants for domain-specific help

**Code doesn't work as expected:**
- Review and test all generated code
- Ask for explanations: `/explain why this approach was chosen`
- Request alternatives: `suggest a different approach for this problem`

**Performance is slow:**
- Limit context size - avoid including large files unnecessarily
- Use specific file references instead of `@workspace` for targeted questions
- Consider breaking large conversations into focused sessions

### Getting Help

If you need assistance:

1. **Use `/help`** in chat for available commands
2. **Check the [Chat Overview](./copilot-chat.md)** for feature explanations
3. **Review [troubleshooting guides](../setup.md#troubleshooting)** for common issues

## Related Resources

- **[Copilot Chat Overview](./copilot-chat.md)** - Complete feature reference
- **[Chat Context Management](./copilot-chat-context.md)** - Advanced context techniques
- **[Chat Modes Comparison](./chat-modes.md)** - When to use each mode
- **[Agent Mode Guide](./chat-agent-mode.md)** - Autonomous coding workflows
- **[Prompt Crafting](../guides/prompt-crafting.md)** - Writing effective prompts

---

*This tutorial provides a foundation for using Copilot Chat effectively. Practice these techniques with your own projects to develop proficiency with AI-assisted development.*
