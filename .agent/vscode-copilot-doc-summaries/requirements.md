# VS Code Copilot Documentation Download Requirements

## Overview
Download and summarize all VS Code Copilot documentation to create a comprehensive knowledge base for development assistance.

## Base URLs
- **Main Copilot docs**: https://code.visualstudio.com/docs/copilot/overview
- **Base URL pattern**: https://code.visualstudio.com/docs/copilot/

## Documentation URLs to Process

### Core Documentation
1. **Overview**: https://code.visualstudio.com/docs/copilot/overview
2. **Setup**: https://code.visualstudio.com/docs/copilot/setup
3. **Quickstart**: https://code.visualstudio.com/docs/copilot/getting-started
4. **Code Completions**: https://code.visualstudio.com/docs/copilot/ai-powered-suggestions
5. **Smart Actions**: https://code.visualstudio.com/docs/copilot/copilot-smart-actions
6. **Customize Copilot**: https://code.visualstudio.com/docs/copilot/copilot-customization
7. **Language Models**: https://code.visualstudio.com/docs/copilot/language-models

### Chat and Interaction
8. **Chat Overview**: https://code.visualstudio.com/docs/copilot/chat/copilot-chat
9. **Chat Tutorial**: https://code.visualstudio.com/docs/copilot/chat/getting-started-chat
10. **Manage Context**: https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context
11. **Chat Modes**: https://code.visualstudio.com/docs/copilot/chat/chat-modes
12. **Ask Mode**: https://code.visualstudio.com/docs/copilot/chat/chat-ask-mode
13. **Edit Mode**: https://code.visualstudio.com/docs/copilot/chat/copilot-edits
14. **Agent Mode**: https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
15. **MCP Servers**: https://code.visualstudio.com/docs/copilot/chat/mcp-servers
16. **Inline Chat**: https://code.visualstudio.com/docs/copilot/chat/inline-chat
17. **Prompt Engineering**: https://code.visualstudio.com/docs/copilot/chat/prompt-crafting

### Guides and Use Cases
18. **Edit Notebooks with AI**: https://code.visualstudio.com/docs/copilot/guides/notebooks-with-ai
19. **Test with AI**: https://code.visualstudio.com/docs/copilot/guides/test-with-copilot
20. **Debug with AI**: https://code.visualstudio.com/docs/copilot/guides/debug-with-copilot
21. **MCP Dev Guide**: https://code.visualstudio.com/docs/copilot/guides/mcp-developer-guide

### General Resources
22. **Tips and Tricks**: https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks
23. **FAQ**: https://code.visualstudio.com/docs/copilot/faq

### Reference
24. **Cheat Sheet**: https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features
25. **Settings Reference**: https://code.visualstudio.com/docs/copilot/reference/copilot-settings
26. **Workspace Context**: https://code.visualstudio.com/docs/copilot/reference/workspace-context

## Processing Requirements

### For Each URL:
1. **Fetch content** using fetch-summary chatmode request
   - .github\chatmodes\fetch-summary.chatmode.md
2. **Generate summary** that includes:
   - Key concepts and features
   - Step-by-step instructions/procedures
   - Code examples (if any)
   - Best practices mentioned
   - Links to related documentation
3. **File naming convention**: 
   - Convert URL path to filename: `/docs/copilot/chat/copilot-chat` → `copilot-chat-copilot-chat.md`
   - Remove special characters and use dashes
   - Add `.md` extension
4. **Store in**: `vscode-copilot-documentation/` directory

### Output Format Requirements:
- **Markdown format** with proper headers
- **Include original URL** at the top of each file
- **Structured sections** for easy navigation
- **Preserve code examples** with proper syntax highlighting
- **Extract key takeaways** as bullet points
- **Cross-reference related articles** when mentioned

### Quality Assurance:
- Ensure all 26 URLs are processed
- Verify completeness of summaries
- Check for consistent formatting across files
- Validate that all key information is captured
- Include any important warnings or prerequisites

### File Organization:
```
vscode-copilot-documentation/
├── overview.md
├── setup.md
├── getting-started.md
├── ai-powered-suggestions.md
├── copilot-smart-actions.md
├── copilot-customization.md
├── language-models.md
├── copilot-tips-and-tricks.md
├── faq.md
├── chat/
│   ├── copilot-chat.md
│   ├── getting-started-chat.md
│   ├── copilot-chat-context.md
│   ├── chat-modes.md
│   ├── chat-ask-mode.md
│   ├── copilot-edits.md
│   ├── chat-agent-mode.md
│   ├── mcp-servers.md
│   ├── inline-chat.md
│   └── prompt-crafting.md
├── guides/
│   ├── notebooks-with-ai.md
│   ├── test-with-copilot.md
│   ├── debug-with-copilot.md
│   └── mcp-developer-guide.md
└── reference/
    ├── copilot-vscode-features.md
    ├── copilot-settings.md
    └── workspace-context.md
```

## Success Criteria:
- [ ] All 26 documentation URLs processed
- [ ] Summaries capture key information comprehensively
- [ ] Files organized in logical directory structure
- [ ] Consistent markdown formatting
- [ ] Code examples preserved and properly formatted
- [ ] Cross-references and related links documented