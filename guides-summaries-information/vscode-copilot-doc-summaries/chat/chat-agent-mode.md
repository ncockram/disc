# VS Code Copilot Agent Mode

**Source:** [VS Code Copilot Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)

## Introduction

Agent mode represents the most advanced and autonomous form of AI assistance in VS Code. It enables Copilot to independently plan, execute, and iterate on complex coding tasks that span multiple files, tools, and systems. Agent mode combines code editing with tool invocation to accomplish high-level objectives.

## Why Use Agent Mode?

### Complex Task Automation
Agent mode excels at tasks that require:
- **Multi-file coordination** - Changes across multiple related files
- **Tool integration** - Terminal commands, file operations, external APIs
- **Iterative problem solving** - Self-correction and adaptation
- **Planning and execution** - Breaking down complex requirements into steps

### Ideal Use Cases
- **Feature implementation** - "Add OAuth authentication to the app"
- **Codebase refactoring** - "Migrate from React class components to hooks"
- **Project setup** - "Create a TypeScript React app with testing and linting"
- **Integration tasks** - "Add Redis caching to the API layer"
- **Migration projects** - "Convert from JavaScript to TypeScript"

## Prerequisites

- **VS Code 1.99 or later** - Agent mode requires recent VS Code version
- **GitHub Copilot subscription** - Agent mode uses advanced AI capabilities
- **Enabled setting** - `chat.agent.enabled` must be set to `true`

## Enabling Agent Mode

### Basic Setup

1. **Open Settings** (`Ctrl+,`)
2. **Search for** `chat.agent.enabled`
3. **Enable the setting** - Check the box or set to `true`

### Enterprise Configuration

For organizations using device management:

```json
{
  "chat.agent.enabled": true,
  "chat.extensionTools.enabled": true,
  "chat.tools.autoApprove": false
}
```

### Quick Access

**Direct links to agent mode:**
- **Stable**: `vscode://GitHub.Copilot-Chat/chat?mode=agent`
- **Insiders**: `vscode-insiders://GitHub.Copilot-Chat/chat?mode=agent`

## Getting Started

### Opening Agent Mode

1. **Chat View** (`Ctrl+Alt+I`)
2. **Select "Agent"** from the mode dropdown
3. **Enter your high-level request**
4. **Monitor and approve** tool executions

### First Agent Request

Start with a simple but complete task:

```
Create a simple Node.js REST API with user authentication, including signup, login, and protected routes
```

**What Agent mode will do:**
1. **Plan the implementation** - Break down the task into steps
2. **Create project structure** - Set up directories and files
3. **Install dependencies** - Use npm/yarn to add required packages
4. **Implement functionality** - Write code across multiple files
5. **Test the implementation** - Run commands to verify functionality
6. **Iterate on issues** - Fix problems that arise

## How Agent Mode Works

### Autonomous Decision Making

Agent mode operates independently by:

**Planning:**
- Analyzing requirements and breaking them down
- Determining file structure and dependencies
- Sequencing implementation steps
- Identifying potential challenges

**Execution:**
- Creating and modifying files as needed
- Running terminal commands for setup and testing
- Installing packages and configuring tools
- Making iterative improvements

**Adaptation:**
- Monitoring outcomes of actions
- Adjusting approach based on results
- Fixing errors and resolving issues
- Learning from feedback and continuing

### Tool Integration

Agent mode can use various tools:

**Built-in Tools:**
- **File operations** - Create, read, update, delete files
- **Terminal commands** - Run shell commands and scripts
- **Code analysis** - Understand existing code structure
- **Error detection** - Identify and fix issues

**Extension Tools:**
- **Language servers** - Type checking, linting, formatting
- **Testing frameworks** - Run tests and analyze results
- **Build systems** - Compile and package applications
- **Version control** - Git operations and workflows

**MCP (Model Context Protocol) Tools:**
- **External APIs** - Integration with third-party services
- **Databases** - Database operations and queries
- **Cloud services** - Deployment and infrastructure management
- **Custom tools** - Organization-specific integrations

## Working with Agent Mode

### Crafting Effective Requests

**High-level objectives work best:**
```
// Effective agent requests
Add social media sharing functionality to this blog application

Implement real-time chat using WebSockets with message persistence

Set up CI/CD pipeline for automatic testing and deployment

Migrate the authentication system from sessions to JWT tokens
```

**Avoid overly specific instructions:**
```
// Less effective for agent mode  
Create a file called auth.js with a function named validateUser that takes email and password parameters

// Better for agent mode
Implement user authentication with email/password validation and session management
```

### Providing Context

**Project context:**
```
@workspace This is a React e-commerce application. Add a shopping cart feature with persistent storage.
```

**Constraint specification:**
```
Add user authentication using Firebase Auth, ensuring compatibility with the existing React Router setup.
```

**Technology preferences:**
```
Implement a blog system using Next.js, TypeScript, and Tailwind CSS with MDX support for content.
```

### Monitoring Progress

Agent mode provides visibility into its process:

**Step-by-step updates:**
- See what the agent is planning to do
- Monitor file creation and modification
- Track tool executions and results
- Observe problem-solving iterations

**Approval workflows:**
- **Tool confirmations** - Approve terminal commands before execution
- **File operations** - Review major file changes
- **External integrations** - Approve API calls and external tool usage

### Tool Approval Management

**Manual approval (default):**
- Agent requests permission before using tools
- Review each action before it executes
- Can approve individual tools for the session
- Maintains control over all operations

**Semi-automatic approval:**
- Pre-approve specific tools for the workspace
- Automatically approve read-only operations
- Require approval for destructive changes
- Configure allow/deny lists for commands

**Automatic approval (experimental):**
- Set `chat.tools.autoApprove` to `true`
- Agent can use tools without interruption
- **Use with caution** - only in safe environments
- Consider for remote development environments

## Advanced Agent Capabilities

### Multi-Step Problem Solving

Agent mode can handle complex workflows:

```
// Single request that involves multiple steps
Refactor this monolithic application into microservices with Docker containers and API gateway
```

**Agent's approach:**
1. **Analysis** - Understand current architecture
2. **Planning** - Design microservice breakdown
3. **Implementation** - Create service containers
4. **Configuration** - Set up API gateway and routing
5. **Testing** - Verify inter-service communication
6. **Documentation** - Update README and deployment guides

### Error Detection and Resolution

Agent mode monitors its own work:

**Automatic error detection:**
- Syntax errors in generated code
- Failed test executions
- Build failures and compilation errors
- Runtime errors during testing

**Self-correction mechanisms:**
- Analyze error messages and logs
- Identify root causes of failures
- Implement fixes and retry operations
- Learn from failures to avoid repetition

### Iterative Improvement

Agent mode can refine its work:

```
// Initial request
Create a React form component with validation

// Agent iterates automatically
1. Creates basic form structure
2. Adds input validation
3. Implements error handling
4. Adds accessibility features
5. Creates unit tests
6. Optimizes performance
```

## Tool Sets and Configuration

### Defining Tool Sets

Group related tools for specific workflows:

```json
{
  "webDevelopment": {
    "tools": [
      "npm",
      "webpack", 
      "eslint",
      "prettier",
      "jest",
      "lighthouse"
    ],
    "description": "Web development and testing tools",
    "icon": "globe"
  },
  "database": {
    "tools": [
      "prisma",
      "mongodb",
      "postgresql",
      "redis"
    ],
    "description": "Database management and operations",
    "icon": "database"
  }
}
```

### Custom Tool Configuration

**Terminal command allow/deny lists:**
```json
{
  "github.copilot.chat.agent.terminal.allowList": [
    "npm",
    "yarn", 
    "git",
    "/^docker.*/",
    "/^kubectl.*/"
  ],
  "github.copilot.chat.agent.terminal.denyList": [
    "rm -rf",
    "sudo",
    "chmod 777"
  ]
}
```

**Workspace-specific settings:**
```json
{
  "chat.agent.maxRequests": 15,
  "github.copilot.chat.agent.runTasks": true,
  "github.copilot.chat.agent.autoFix": true
}
```

## Real-World Agent Workflows

### Full-Stack Application Setup

```
Create a full-stack TypeScript application with:
- Next.js frontend with Tailwind CSS
- Express.js API backend
- PostgreSQL database with Prisma ORM
- Authentication using NextAuth.js
- Deployment configuration for Vercel
```

**Agent execution steps:**
1. Initialize Next.js project with TypeScript
2. Set up Tailwind CSS configuration
3. Create Express.js API server
4. Configure PostgreSQL and Prisma
5. Implement authentication system
6. Set up deployment configurations
7. Create environment setup documentation
8. Run tests to verify functionality

### Legacy System Migration

```
Migrate this jQuery-based application to modern React with TypeScript, maintaining all existing functionality
```

**Agent approach:**
1. **Analysis** - Understand current jQuery implementation
2. **Planning** - Map jQuery features to React patterns
3. **Setup** - Create React project structure
4. **Migration** - Convert components incrementally
5. **Testing** - Ensure feature parity
6. **Optimization** - Improve performance and code quality
7. **Documentation** - Create migration notes

### API Integration Project

```
Integrate this application with the Stripe payment API, including webhook handling and subscription management
```

**Agent workflow:**
1. **Research** - Review Stripe API documentation
2. **Setup** - Install Stripe SDK and configure keys
3. **Implementation** - Create payment endpoints
4. **Webhooks** - Set up webhook handlers
5. **Frontend** - Add payment UI components
6. **Testing** - Use Stripe test mode for validation
7. **Security** - Implement proper error handling and validation

## Best Practices

### Request Formulation

**Be goal-oriented:**
```
// Focus on outcomes
Add e-commerce functionality to support product catalogs and order processing

// Rather than implementation details
Create a products table with id, name, price columns and add CRUD operations
```

**Provide business context:**
```
Build a content management system for a marketing team that needs to publish blog posts and manage media assets
```

**Specify constraints:**
```
Implement user authentication using existing Active Directory integration, maintaining current security policies
```

### Guidance and Feedback

**Monitor progress actively:**
- Review each major step
- Provide feedback on direction
- Approve or reject tool usage
- Guide decision-making when needed

**Provide domain expertise:**
```
// After agent creates initial API structure
This API needs to handle high traffic. Implement rate limiting and caching strategies appropriate for a social media platform.
```

**Iterate and refine:**
```
// Follow-up to improve implementation
The authentication system works well. Now add role-based access control for admin, moderator, and user roles.
```

### Code Quality and Security

**Review generated code:**
- Check for security vulnerabilities
- Verify error handling
- Assess performance implications
- Ensure code quality standards

**Test thoroughly:**
- Run automated tests
- Perform manual testing
- Verify edge cases
- Check integration points

**Follow team standards:**
- Ensure coding conventions are followed
- Verify documentation requirements
- Check commit message standards
- Validate deployment procedures

## Troubleshooting

### Common Issues

**Agent requests fail or timeout:**
- Reduce scope of initial request
- Check network connectivity
- Verify tool availability
- Review error messages in output

**Generated code has errors:**
- Review agent's error detection
- Provide feedback on specific issues
- Ask for fixes to particular problems
- Consider breaking into smaller tasks

**Tool approval interruptions:**
- Configure appropriate approval settings
- Use tool sets for common workflows
- Pre-approve safe operations
- Review security implications

### Performance Optimization

**Large project considerations:**
- Use specific file/directory context
- Break complex tasks into phases
- Monitor token usage and limits
- Consider workspace organization

**Network and resource usage:**
- Be mindful of API rate limits
- Consider local vs. cloud tool usage
- Monitor system resource consumption
- Plan for long-running operations

## Settings Reference

### Core Agent Settings

```json
{
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  "github.copilot.chat.agent.runTasks": true,
  "github.copilot.chat.agent.autoFix": true,
  "chat.tools.autoApprove": false
}
```

### Terminal Integration

```json
{
  "github.copilot.chat.agent.terminal.allowList": ["npm", "yarn", "git"],
  "github.copilot.chat.agent.terminal.denyList": ["rm -rf", "sudo"]
}
```

### MCP and External Tools

```json
{
  "chat.mcp.discovery.enabled": true,
  "chat.extensionTools.enabled": true
}
```

## Related Resources

- **[MCP Servers Setup](./mcp-servers.md)** - Adding external tools to agent mode
- **[Chat Modes Overview](./chat-modes.md)** - When to use agent vs. other modes
- **[Edit Mode Guide](./copilot-edits.md)** - For more controlled editing workflows
- **[Copilot Customization](../copilot-customization.md)** - Personalizing agent behavior
- **[Getting Started Guide](./getting-started-chat.md)** - Basic tutorial including agent mode

---

*Agent mode represents the cutting edge of AI-assisted development, enabling autonomous coding workflows that can handle complex, multi-step tasks. Use it for substantial implementations where you want AI to take initiative while maintaining oversight and control.*
