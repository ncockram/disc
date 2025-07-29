# Get started with GitHub Copilot in VS Code

**Source:** https://code.visualstudio.com/docs/copilot/getting-started

## Summary

This comprehensive tutorial introduces the key AI features in Visual Studio Code powered by GitHub Copilot. It provides hands-on examples for code completions, chat interactions, multi-file editing, and error fixing using natural language prompts. The tutorial uses JavaScript and TypeScript examples but applies to numerous programming languages and frameworks.

## Prerequisites

Before starting this tutorial, ensure you have:

- **VS Code Installed**: Download from the [Visual Studio Code website](https://code.visualstudio.com/)
- **GitHub Copilot Access**: Follow [Set up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup) guide

> **Tip**: If you don't have a Copilot subscription, you can sign up for Copilot Free directly from VS Code with monthly limits on completions and chat interactions.

## Get Your First Code Suggestion

Code suggestions automatically appear as you type, requiring no special setup.

### Exercise: Calculator Class

1. **Create New File**
   - Open VS Code and create `calculator.js`

2. **Start Typing**
   ```javascript
   class Calculator
   ```

3. **Observe Suggestions**
   - Copilot shows implementation suggestions in gray dimmed text (ghost text)
   - Suggestions are non-deterministic and may vary

4. **Accept Suggestions**
   - Press **Tab** key to accept suggestions
   - Copilot updates suggestions as you continue typing

### Multiple Suggestions Feature

1. **Add Method**
   ```javascript
   factorial(n) {
   ```

2. **View Alternatives**
   - Hover over suggestions to see multiple options
   - Use arrow controls or keyboard shortcuts:
     - **Alt+]**: Next suggestion
     - **Alt+[**: Previous suggestion

### Benefits
- Generates boilerplate and repetitive code
- Maintains developer flow and focus
- Allows concentration on complex coding tasks

## Use Editor Inline Chat to Generate a Basic Web Server

Editor inline chat provides a natural language interface directly in the editor for code generation and questions.

### Exercise: Express Web Server

1. **Create TypeScript File**
   - Add new file `server.ts` to workspace

2. **Open Inline Chat**
   - Press **Ctrl+I** to bring up editor inline chat
   - Chat interface appears directly in the editor

3. **Generate Server Code**
   - Type: "add a simple express web server"
   - Press **Enter** to submit prompt

4. **Review and Accept**
   - Code changes stream directly in the editor
   - Response shows Node.js Express web server implementation
   - Select **Accept** or press **Ctrl+Enter** to apply changes

### Key Features
- Direct integration with active editor
- Real-time code streaming
- Context-aware generation
- Immediate application of changes

## Refactor Your Code Through AI Chat

Use inline chat to improve and modify existing code with natural language instructions.

### Exercise: Environment Variable Configuration

1. **Select Code**
   - Highlight the `3000` port number in `server.ts`
   - Press **Ctrl+I** to open inline chat

2. **Request Refactoring**
   - Type: "use an environment variable for the port number"
   - Press **Enter** to send request

3. **Apply Changes**
   - Review proposed code updates
   - Select **Accept** or press **Ctrl+Enter**

4. **Iterate if Needed**
   - Modify prompts for different solutions
   - Example: "use a different environment variable name for the port number"

### Benefits
- Quick code improvements
- Natural language refactoring instructions
- Iterative refinement capability
- Context-aware modifications

## Use Chat for General Programming Questions

The Chat view provides a persistent conversation interface for general programming questions and learning.

### Exercise: Learning About Recursion

1. **Open Chat View**
   - Use Copilot menu in title bar or press **Ctrl+Alt+I**

2. **Set Chat Mode**
   - Select **Ask** from the mode dropdown
   - This mode is optimized for questions

3. **Ask Question**
   - Type: "what is recursion?"
   - Press **Enter** to submit

4. **Review Response**
   - Rich results with Markdown text and code blocks
   - Chat maintains conversation history

### Advanced Features
- **Language Model Selection**: Choose different models from dropdown
- **Conversation History**: Tracks previous questions and answers
- **Rich Formatting**: Supports Markdown, code blocks, and syntax highlighting

### Use Cases
- Learning new programming concepts
- Understanding coding patterns
- Exploring new programming languages
- Getting explanations of complex topics

## Make Edits Across Multiple Files

AI-powered editing sessions can modify multiple files simultaneously for larger code changes.

### Exercise: HTML Page Integration

1. **Switch to Edit Mode**
   - Select **Edit** from mode dropdown in Chat view

2. **Review Context**
   - `server.ts` file automatically added as context
   - Use **Add Context** button for additional files

3. **Request Changes**
   - Type: "Return a static html page as the home page and implement it."
   - Press **Enter** to start edit session

4. **Review Edits**
   - Multiple files modified (server.ts updated, index.html created)
   - Changes applied across workspace

5. **Accept or Reject**
   - Select **Keep** to apply all changes
   - Use editor overlay controls for individual file decisions
   - Navigate between edited files for selective acceptance

### Capabilities
- Multi-file coordination
- Context-aware edits
- File creation and modification
- Granular acceptance/rejection controls

## Fix Coding Errors with AI

AI functionality integrates throughout VS Code, including error resolution through the sparkle icon.

### Exercise: Dependency Error Resolution

1. **Identify Error**
   - Open `server.ts` with red squiggle on `import express from 'express';`
   - Position cursor on red squiggle

2. **Access AI Code Actions**
   - Look for sparkle icon appearance
   - Select sparkle icon to view AI Code Actions

3. **Apply Fix**
   - Select **Fix using Copilot**
   - Editor inline chat opens with prepopulated error message

4. **Implement Solution**
   - Review proposed solution
   - Use **Insert into Terminal** button for command execution
   - Apply suggested fixes

### Error-Fixing Features
- Automatic error detection
- Context-aware solutions
- Terminal integration
- Streamlined fix application

## Next Steps

After completing this tutorial, you've successfully used:
- AI-powered code completions
- Editor inline chat for generation and refactoring
- Chat view for questions and learning
- Multi-file editing sessions
- Error resolution with AI

### Recommended Learning Path

1. **Advanced Chat**: [Copilot Chat Tutorial](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)
2. **AI Code Editing**: [Copilot Edits](https://code.visualstudio.com/docs/copilot/chat/copilot-edits) documentation

## Related Resources

### Video Content
- [Copilot Best Practices](https://youtu.be/2q0BoioYSxQ) on YouTube
- [Advanced Features](https://www.youtube.com/watch?v=SLMfhuptCo8) tutorial

### Documentation Links
- [Set up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup)
- [Copilot Chat Tutorial](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)
- [Copilot Edits Documentation](https://code.visualstudio.com/docs/copilot/chat/copilot-edits)

## Key Takeaways

1. **Code Completions**: Automatic suggestions as you type with Tab acceptance
2. **Inline Chat**: Direct editor integration for generation and refactoring
3. **Chat View**: Persistent conversations for learning and complex questions
4. **Multi-file Editing**: Coordinated changes across workspace files
5. **Error Resolution**: AI-powered fixes integrated into editor workflow
6. **Language Support**: Works with numerous programming languages and frameworks
7. **Iterative Improvement**: Ability to refine and modify AI suggestions
