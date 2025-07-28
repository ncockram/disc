# VS Code Copilot MCP Servers

**Source:** [VS Code Copilot MCP Servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## Introduction

Model Context Protocol (MCP) servers extend GitHub Copilot's capabilities in VS Code by providing access to external tools, databases, APIs, and specialized services. MCP enables AI models to interact with external systems through a standardized interface, significantly expanding what Copilot can accomplish.

## What is MCP?

### Core Concept

Model Context Protocol (MCP) is an open standard that:
- **Standardizes AI-tool interaction** - Unified interface for external services
- **Enables tool discovery** - AI can find and use available tools
- **Provides secure integration** - Controlled access to external resources
- **Supports diverse capabilities** - Databases, APIs, file systems, cloud services

### How MCP Works

**Architecture:**
```
VS Code ↔ Copilot ↔ MCP Server ↔ External Service
```

**Process:**
1. **Tool Discovery** - Copilot finds available MCP tools
2. **Context Gathering** - MCP servers provide relevant data
3. **Tool Invocation** - Copilot requests tool execution
4. **Result Integration** - Tool output enhances AI responses

### Supported Capabilities

**Tools:** Functions that perform actions
- Database queries and operations
- API calls and integrations
- File system operations
- Cloud service management

**Resources:** Data sources for context
- Documentation and knowledge bases
- Configuration files and settings
- Real-time data feeds
- External system state

**Prompts:** Pre-configured task templates
- Common workflows and procedures
- Domain-specific operations
- Best practice implementations

## Prerequisites

- **VS Code 1.102 or later** - MCP support is generally available
- **GitHub Copilot subscription** - Required for chat functionality
- **Agent mode enabled** - MCP tools work best with agent mode

## Adding MCP Servers

### Installation Options

**Direct installation from curated list:**
1. Visit [VS Code MCP Servers](https://code.visualstudio.com/mcp)
2. Click "Install" on any MCP server
3. Server automatically configures in VS Code

**Workspace configuration:**
- Create `.vscode/mcp.json` in your project
- Share configuration with team members
- Project-specific tool access

**User configuration:**
- Global MCP server setup
- Available across all workspaces
- Synchronized with Settings Sync

**Auto-discovery:**
- Reuse MCP servers from other tools (Claude Desktop)
- Enable with `chat.mcp.discovery.enabled`

### Workspace MCP Configuration

Create `.vscode/mcp.json` for project-specific servers:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "api-key",
      "description": "API Key for External Service",
      "password": true
    }
  ],
  "servers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "database": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost:5432/mydb"
      }
    },
    "perplexity": {
      "type": "stdio", 
      "command": "npx",
      "args": ["-y", "server-perplexity-ask"],
      "env": {
        "PERPLEXITY_API_KEY": "${input:api-key}"
      }
    }
  }
}
```

### User MCP Configuration

Global configuration for all workspaces:

1. **Open user configuration:** `MCP: Open User Configuration`
2. **Add servers** to your profile
3. **Configure per VS Code profile** for different contexts

Example user configuration:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "MCP_ROOT_PATH": "/home/user/projects"
      }
    },
    "weather": {
      "type": "sse",
      "url": "https://weather-mcp-server.example.com/sse"
    }
  }
}
```

## Configuration Format

### Server Configuration

**For `stdio` servers (local processes):**
```json
{
  "type": "stdio",
  "command": "node",
  "args": ["server.js"],
  "env": {
    "API_KEY": "${input:my-api-key}"
  }
}
```

**For `sse`/`http` servers (remote endpoints):**
```json
{
  "type": "sse",
  "url": "https://my-mcp-server.com/sse",
  "headers": {
    "Authorization": "Bearer ${input:auth-token}"
  }
}
```

### Input Variables

Avoid hardcoding sensitive information:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "database-password",
      "description": "Database Password",
      "password": true
    },
    {
      "type": "promptString", 
      "id": "api-endpoint",
      "description": "API Endpoint URL"
    }
  ]
}
```

### Dev Container Support

Configure MCP servers in containerized environments:

```json
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node:latest",
  "customizations": {
    "vscode": {
      "mcp": {
        "servers": {
          "playwright": {
            "command": "npx",
            "args": ["-y", "@microsoft/mcp-server-playwright"]
          }
        }
      }
    }
  }
}
```

## Using MCP Tools

### In Agent Mode

MCP tools are most powerful in agent mode:

1. **Open Agent Mode** (`Ctrl+Alt+I` → Select "Agent")
2. **View available tools** - Click the Tools button
3. **Select tools** - Enable/disable specific MCP tools
4. **Make requests** - Tools are automatically invoked as needed

```
// Example agent request using MCP tools
Analyze the user engagement data from our PostgreSQL database and create a comprehensive report with visualizations
```

**Tool invocation process:**
1. **Request analysis** - Agent determines needed tools
2. **Tool confirmation** - User approves tool usage
3. **Tool execution** - MCP server performs operations
4. **Result integration** - Output enhances response

### Tool Selection

**Tools picker interface:**
- Search available tools by name
- Enable/disable tools for current session
- Maximum 128 tools per request
- Group related tools using tool sets

**Direct tool reference:**
```
Use #perplexity-search to find the latest information about React 18 features

Query the #database-tool to get user statistics for the last month
```

### Tool Confirmation Workflow

**Default behavior:** Manual approval required
- Review tool parameters before execution
- Approve/deny each tool invocation
- Edit tool parameters if needed
- Auto-approve for session/workspace/all future use

**Advanced approval settings:**
```json
{
  "chat.tools.autoApprove": false,
  "github.copilot.chat.agent.terminal.allowList": ["npm", "git"],
  "github.copilot.chat.agent.terminal.denyList": ["rm", "sudo"]
}
```

## Working with MCP Resources

### Adding Resources as Context

MCP servers provide resources for context:

1. **Chat view** → **Add Context** → **MCP Resources**
2. **Select resource type** from available options
3. **Provide parameters** if required
4. **Resource content** included in chat context

Examples:
```
// Database schema as context
Add the user table schema from our PostgreSQL MCP server

// External documentation
Include the API documentation from our internal MCP server

// Real-time data
Get current system metrics from the monitoring MCP server
```

### Resource Types

**Static resources:**
- Configuration files
- Documentation
- Schema definitions
- Reference data

**Dynamic resources:**
- Database query results
- API responses
- System status information
- Real-time metrics

**Computed resources:**
- Analysis results
- Aggregated data
- Processed information
- Generated reports

## MCP Prompts

### Using Pre-configured Prompts

MCP servers can provide ready-made prompts:

```
/mcp.servername.promptname
```

Examples:
```
/mcp.database.analyze-performance
/mcp.github.review-pr
/mcp.testing.generate-test-suite
```

### Prompt with Parameters

Some prompts require additional input:

```
/mcp.weather.get-forecast
// Prompt asks for: Location, Duration
```

### Custom Prompt Integration

Create workflows combining multiple MCP prompts:

```
// Multi-step workflow using MCP prompts
1. /mcp.database.backup-data
2. /mcp.deployment.staging-deploy  
3. /mcp.testing.run-integration-tests
4. /mcp.monitoring.setup-alerts
```

## Tool Sets for MCP

### Creating Tool Sets

Group related MCP tools for easier management:

```json
{
  "dataAnalysis": {
    "tools": [
      "postgres-query",
      "redis-stats", 
      "analytics-api",
      "chart-generator"
    ],
    "description": "Data analysis and visualization tools",
    "icon": "graph"
  },
  "deployment": {
    "tools": [
      "docker-build",
      "kubernetes-deploy",
      "aws-cli",
      "terraform"
    ],
    "description": "Deployment and infrastructure tools", 
    "icon": "rocket"
  }
}
```

### Using Tool Sets

Reference tool sets in prompts:

```
Use the #dataAnalysis tool set to create a comprehensive user engagement report

Apply the #deployment tool set to deploy this application to production
```

## Managing MCP Servers

### Server Management UI

**Extensions view** (`Ctrl+Shift+X`) → **MCP SERVERS - INSTALLED**:
- **Start/Stop/Restart** servers
- **View server logs** for debugging
- **Configure model access** and sampling
- **Browse resources** provided by servers
- **Show configuration** details
- **Uninstall servers** when no longer needed

### Command Palette Operations

**MCP: List Servers** - View all configured servers
**MCP: Add Server** - Install new MCP server
**MCP: Open User Configuration** - Edit global settings
**MCP: Browse Resources** - Explore available resources

### Server Status Monitoring

**Health indicators:**
- Green: Server running and responsive
- Yellow: Server starting or experiencing issues
- Red: Server failed or disconnected

**Log access:**
- Right-click server → "Show Output"
- View startup logs and error messages
- Debug connectivity and configuration issues

## Development and Debugging

### Development Mode

Enable development features for MCP servers:

```json
{
  "servers": {
    "my-server": {
      "command": "node",
      "args": ["build/index.js"],
      "dev": {
        "watch": "build/**/*.js",
        "debug": { "type": "node" }
      }
    }
  }
}
```

**Development features:**
- **File watching** - Auto-restart on changes
- **Debugger integration** - Step through server code
- **Enhanced logging** - Detailed execution information

### Debugging MCP Issues

**Common troubleshooting steps:**

1. **Check server logs:**
   ```
   MCP: List Servers → Select Server → Show Output
   ```

2. **Verify configuration:**
   - Check JSON syntax in `mcp.json`
   - Validate environment variables
   - Confirm file permissions

3. **Test connectivity:**
   - Ensure server starts without errors
   - Verify network connectivity for remote servers
   - Check authentication credentials

4. **Review tool limits:**
   - Maximum 128 tools per request
   - Reduce active tools if hitting limits
   - Use tool sets for better organization

### Error Resolution

**Server won't start:**
- Check command and arguments
- Verify dependencies are installed
- Review environment variable values
- Check file paths and permissions

**Tools not appearing:**
- Restart VS Code to refresh tool list
- Check server status in Extensions view
- Verify MCP configuration syntax
- Review server logs for errors

**Slow tool execution:**
- Check network connectivity
- Review server resource usage
- Consider local vs. remote server options
- Optimize tool parameters

## Popular MCP Servers

### Database Integration

**PostgreSQL MCP Server:**
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "mcp-server-postgres"],
    "env": {
      "DATABASE_URL": "postgresql://user:pass@localhost:5432/db"
    }
  }
}
```

**MongoDB MCP Server:**
```json
{
  "mongodb": {
    "command": "npx", 
    "args": ["-y", "mcp-server-mongodb"],
    "env": {
      "MONGODB_URI": "mongodb://localhost:27017/mydb"
    }
  }
}
```

### API Integration

**REST API MCP Server:**
```json
{
  "api-client": {
    "command": "npx",
    "args": ["-y", "mcp-server-fetch"],
    "env": {
      "API_BASE_URL": "https://api.example.com"
    }
  }
}
```

**GitHub MCP Server:**
```json
{
  "github": {
    "url": "https://api.githubcopilot.com/mcp/"
  }
}
```

### Development Tools

**Playwright MCP Server:**
```json
{
  "playwright": {
    "command": "npx",
    "args": ["-y", "@microsoft/mcp-server-playwright"]
  }
}
```

**File System MCP Server:**
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem"],
    "env": {
      "MCP_ROOT_PATH": "/path/to/project"
    }
  }
}
```

## Security Considerations

### Access Control

**Principle of least privilege:**
- Grant minimal necessary permissions
- Use environment variables for secrets
- Avoid hardcoding credentials
- Review server source code

**Input validation:**
- MCP servers should validate all inputs
- Use parameterized queries for databases
- Sanitize user-provided data
- Implement rate limiting

### Network Security

**Remote server connections:**
- Use HTTPS/WSS for encrypted communication
- Validate SSL certificates
- Implement authentication headers
- Monitor for suspicious activity

**Local server isolation:**
- Run servers with limited user permissions
- Use containerization when possible
- Isolate server processes
- Monitor system resource usage

### Data Privacy

**Sensitive information handling:**
- Avoid including secrets in MCP configurations
- Use input prompts for runtime secrets
- Implement data masking where appropriate
- Follow organizational privacy policies

## Advanced Use Cases

### Custom MCP Server Development

Create specialized servers for your organization:

```javascript
// Example: Custom analytics MCP server
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server({
  name: 'analytics-server',
  version: '1.0.0'
});

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'user-analytics':
      return await getUserAnalytics(args);
    case 'performance-metrics':
      return await getPerformanceMetrics(args);
  }
});
```

### Enterprise Integration

**Single sign-on integration:**
```json
{
  "enterprise-api": {
    "type": "sse",
    "url": "https://internal-mcp-server.company.com/sse",
    "headers": {
      "Authorization": "Bearer ${input:sso-token}"
    }
  }
}
```

**Multi-environment configuration:**
```json
{
  "production-db": {
    "command": "npx",
    "args": ["-y", "mcp-server-postgres"],
    "env": {
      "DATABASE_URL": "${input:prod-db-url}"
    }
  },
  "staging-db": {
    "command": "npx", 
    "args": ["-y", "mcp-server-postgres"],
    "env": {
      "DATABASE_URL": "${input:staging-db-url}"
    }
  }
}
```

## Best Practices

### Configuration Management

**Security:**
- Use input variables for sensitive data
- Avoid committing secrets to version control
- Implement proper access controls
- Regularly rotate credentials

**Organization:**
- Group related servers logically
- Use descriptive server names
- Document server purposes and usage
- Maintain configuration consistency

**Performance:**
- Monitor server resource usage
- Implement caching where appropriate
- Use appropriate timeout values
- Consider server locality

### Workflow Integration

**Development workflow:**
1. **Local development** - Use development mode MCP servers
2. **Testing** - Integrate MCP tools with testing workflows
3. **Staging** - Use staging environment MCP servers
4. **Production** - Carefully managed production server access

**Team collaboration:**
- Share MCP configurations via version control
- Document available tools and their usage
- Establish approval processes for new servers
- Train team members on MCP capabilities

## Related Resources

- **[VS Code MCP Servers List](https://code.visualstudio.com/mcp)** - Curated server directory
- **[Model Context Protocol Documentation](https://modelcontextprotocol.io/)** - Official MCP specification
- **[Agent Mode Guide](./chat-agent-mode.md)** - Using MCP tools with agent mode
- **[Chat Context Management](./copilot-chat-context.md)** - Integrating MCP resources as context
- **[Copilot Customization](../copilot-customization.md)** - Personalizing MCP tool usage

---

*MCP servers transform Copilot from a code-focused assistant into a comprehensive development platform capable of integrating with your entire technology stack. Start with simple servers and gradually build more sophisticated integrations as your team becomes comfortable with the technology.*
