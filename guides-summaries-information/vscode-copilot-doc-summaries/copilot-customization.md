# Customize AI responses in VS Code

**Source:** https://code.visualstudio.com/docs/copilot/copilot-customization

## Summary

This comprehensive guide explains how to customize AI responses in VS Code through custom instructions, prompt files, and custom chat modes. These features enable you to tailor Copilot's behavior to match your coding practices, project requirements, and workflow preferences without repeatedly providing context in every chat prompt.

## Overview

VS Code offers three primary customization approaches:

1. **Custom Instructions**: Define common guidelines for tasks like code generation, reviews, and commit messages
2. **Prompt Files**: Create reusable prompts for specific tasks and workflows  
3. **Custom Chat Modes**: Configure how chat operates, available tools, and interaction patterns

## Custom Instructions

### Purpose and Benefits
- Automatically incorporate coding practices and project requirements
- Eliminate repetitive context in chat queries
- Ensure consistent AI responses across team members
- Define project-specific conventions and standards

> **Note**: Custom instructions apply only to chat interactions, not code completions.

### Types of Custom Instructions

#### .github/copilot-instructions.md File
- **Scope**: Workspace-specific instructions
- **Location**: Repository root in `.github/` directory
- **Compatibility**: Works across VS Code, Visual Studio, and GitHub.com
- **Use Case**: General coding practices and project requirements

#### .instructions.md Files
- **Scope**: Workspace or user profile instructions
- **Flexibility**: Task-specific instructions with glob pattern targeting
- **Control**: Automatic or manual inclusion in chat prompts
- **Organization**: Multiple files for different purposes

#### VS Code Settings
- **Scope**: User or workspace settings
- **Coverage**: Code generation, test generation, commit messages, code review, PR descriptions
- **Format**: JSON configuration with text or file references

### Creating Custom Instructions

#### .github/copilot-instructions.md Setup

1. **Enable Feature**
   ```json
   "github.copilot.chat.codeGeneration.useInstructionFiles": true
   ```

2. **Create File Structure**
   ```
   workspace-root/
   ├── .github/
   │   └── copilot-instructions.md
   ```

3. **Write Instructions**
   ```markdown
   # Project Coding Standards
   
   - Use TypeScript for all new files
   - Follow functional programming patterns
   - Include comprehensive JSDoc comments
   - Use descriptive variable names
   - Prefer const over let
   ```

#### .instructions.md File Structure

**Header with Metadata (Front Matter)**:
```yaml
---
description: "TypeScript React component guidelines"
applyTo: "**/*.ts,**/*.tsx"
---
```

**Body with Instructions**:
```markdown
# React Component Guidelines

## Naming Conventions
- Use PascalCase for component names
- Use camelCase for props and state

## Code Style
- Use arrow functions for components
- Include TypeScript types for all props
- Use destructuring for props
```

#### Creating Instructions Files

1. **Via Chat View**
   - Select Configure Chat → Instructions → New instruction file
   - Choose workspace or user profile location

2. **Via Command Palette**
   - Run `Chat: New Instructions File`
   - Select scope and provide name

3. **Manual Creation**
   - Create `.instructions.md` files in appropriate directories
   - Add front matter and instruction content

### Instructions File Management

#### Automatic Application
- Use `applyTo` property with glob patterns
- Examples:
  - `"**"`: Apply to all files
  - `"**/*.ts,**/*.tsx"`: TypeScript files only
  - `"src/components/**"`: Components directory

#### Manual Attachment
- **Chat View**: Add Context → Instructions
- **Command Palette**: `Chat: Attach Instructions`
- **Reference**: Use `#filename` in chat prompts

#### File Organization
- **Workspace**: `.github/instructions/` (default)
- **User Profile**: Synced across devices with Settings Sync
- **Custom Locations**: Configure with `chat.instructionsFilesLocations`

### Settings-Based Instructions

#### Configuration Example
```json
{
  "github.copilot.chat.reviewSelection.instructions": [
    { "text": "Focus on security and performance issues" },
    { "file": "guidelines/code-review-checklist.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Use conventional commit format" }
  ]
}
```

#### Available Settings
- `github.copilot.chat.reviewSelection.instructions`
- `github.copilot.chat.commitMessageGeneration.instructions`
- `github.copilot.chat.pullRequestDescriptionGeneration.instructions`

### Auto-Generated Instructions

#### Workspace Analysis
VS Code can analyze your workspace and generate matching instructions:

1. Configure Chat → Instructions
2. Select "Generate instructions"
3. Review and customize generated content
4. Save as `.github/copilot-instructions.md`

## Prompt Files (Experimental)

### Purpose and Structure
Prompt files are reusable prompts for specific tasks like code generation or reviews. They combine task descriptions with optional guidelines and can reference instruction files.

### File Structure

#### Header (Front Matter)
```yaml
---
mode: "agent"           # ask, edit, or agent
model: "gpt-4"         # specific AI model
tools: ["filesystem"]   # available tools
description: "Generate React form components"
---
```

#### Body Content
```markdown
# Generate React Form Component

Create a TypeScript React component with the following requirements:

## Component Structure
- Use functional component with hooks
- Include form validation
- Support controlled inputs

## Input Variables
- Component name: ${input:componentName}
- Form fields: ${input:fields:Enter comma-separated field names}

## References
- [Style Guide](../docs/style-guide.md)
- [Form utilities](../utils/form-helpers.ts)
```

#### Variable Support
- **Workspace**: `${workspaceFolder}`, `${workspaceFolderBasename}`
- **Selection**: `${selection}`, `${selectedText}`
- **File Context**: `${file}`, `${fileBasename}`, `${fileDirname}`
- **Input**: `${input:variableName}`, `${input:variableName:placeholder}`

### Creating Prompt Files

#### Via Chat Interface
1. Configure Chat → Prompt Files → New prompt file
2. Choose workspace or user profile location
3. Enter prompt file name
4. Author content with Markdown formatting

#### File Organization
- **Workspace**: `.github/prompts/` (default)
- **User Profile**: Synced with Settings Sync
- **Custom Locations**: Configure with `chat.promptFilesLocations`

### Using Prompt Files

#### Execution Methods
1. **Command Palette**: `Chat: Run Prompt` → select file
2. **Chat Input**: Type `/prompt-filename` with optional parameters
3. **Editor**: Open prompt file and click play button

#### Parameter Passing
```
/create-react-form: componentName=LoginForm
/generate-tests: testType=unit, coverage=90%
```

#### Cross-References
- Link to other prompt files: `[Base Setup](./base-setup.prompt.md)`
- Reference instructions: `[Guidelines](../instructions/react.instructions.md)`
- Include workspace files: `[Utils](../src/utils/helpers.ts)`

## Advanced Customization

### Custom Chat Modes
Define how chat operates with specific tool access and interaction patterns:

```markdown
---
description: "Security-focused code review mode"
tools: ["security-scanner", "vulnerability-checker"]
---

# Security Review Mode

This mode focuses on identifying security vulnerabilities and best practices.

## Review Criteria
- Authentication and authorization
- Input validation and sanitization
- Data encryption and storage
- Error handling and information disclosure
```

### Integration with Instructions
Prompt files can reference instruction files for consistency:

```markdown
# API Development Prompt

Follow the [API Guidelines](../instructions/api-standards.instructions.md) 
when generating REST endpoints.

Create a new API endpoint for ${input:resource} with CRUD operations.
```

### Team Collaboration

#### Version Control
- Store instruction and prompt files in repository
- Track changes and updates over time
- Ensure team-wide consistency

#### Sharing Strategies
- **Repository Level**: `.github/copilot-instructions.md` for project standards
- **Team Templates**: Shared user profile instructions
- **Role-Specific**: Different instruction files for frontend/backend developers

## Configuration and Management

### Central Management
Enable/disable features organization-wide:
```json
"chat.promptFiles": true
```

### Settings Overview

#### Custom Instructions Settings
- `github.copilot.chat.codeGeneration.useInstructionFiles`
- `chat.instructionsFilesLocations`
- Various task-specific instruction settings

#### Prompt Files Settings
- `chat.promptFiles`
- `chat.promptFilesLocations`
- `chat.instructionFilesLocations`

### Enterprise Configuration
Use device management policies to control feature availability across the organization.

## Best Practices

### Writing Effective Instructions
- **Concise and Specific**: Each instruction should be a single, clear statement
- **Self-Contained**: Avoid external references within instructions
- **Organized**: Use multiple files for different topics or tasks
- **Testable**: Instructions should lead to consistent, measurable outcomes

### File Organization
- **Logical Grouping**: Separate instructions by language, framework, or team role
- **Clear Naming**: Use descriptive filenames for easy identification
- **Documentation**: Include descriptions in front matter

### Team Adoption
- **Gradual Implementation**: Start with high-impact, commonly used instructions
- **Training**: Educate team members on available instructions and prompt files
- **Feedback Loop**: Regularly review and update based on team experience
- **Standards**: Establish guidelines for creating and maintaining custom content

### Maintenance
- **Regular Review**: Update instructions as project requirements evolve
- **Testing**: Verify instructions produce expected results
- **Cleanup**: Remove outdated or conflicting instructions
- **Monitoring**: Track usage and effectiveness of different instruction sets

## Troubleshooting

### Common Issues
- **Conflicting Instructions**: Ensure no contradictory guidance across files
- **Missing Context**: Provide sufficient detail for AI understanding
- **Scope Problems**: Use appropriate `applyTo` patterns for targeted application

### Debugging Tips
- **Test Instructions**: Verify instructions work with simple examples
- **Check File Paths**: Ensure relative paths are correct
- **Validate Syntax**: Confirm YAML front matter is properly formatted

## Next Steps

### Advanced Features
- [Custom Chat Modes](https://code.visualstudio.com/docs/copilot/chat/chat-modes)
- [Agent Mode Tools](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode#_agent-mode-tools)
- [Chat Configuration](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)

### Integration Opportunities
- Combine instructions with specific language models
- Integrate with CI/CD pipelines for automated code generation
- Create organization-wide instruction libraries

## Related Documentation

- [Copilot Chat Overview](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [Chat Modes](https://code.visualstudio.com/docs/copilot/chat/chat-modes)
- [Agent Mode Configuration](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [VS Code Settings Sync](https://code.visualstudio.com/docs/configure/settings-sync)
- [VS Code Profiles](https://code.visualstudio.com/docs/configure/profiles)
