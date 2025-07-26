# GitHub Copilot Settings Reference

## Overview

This comprehensive settings reference provides detailed configuration options for GitHub Copilot in Visual Studio Code. Each setting includes its purpose, default value, and practical usage guidance to help you customize your AI-powered development experience.

## General Settings

### Core Interface Controls
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.commandCenter.enabled` | `true` | Controls whether to show the Copilot menu in the VS Code title bar |
| `workbench.commandPalette.experimental.askChatLocation` | `"chatView"` | (Experimental) Controls where Command Palette should ask chat questions |
| `search.searchView.semanticSearchBehavior` | `"manual"` | (Preview) Configure when to run semantic search: manually, when no text results found, or always |
| `search.searchView.keywordSuggestions` | `false` | (Preview) Controls whether to show keyword suggestions in Search view |
| `workbench.settings.showAISearchToggle` | `true` | (Experimental) Enable searching settings with AI in Settings editor |

## Code Editing Settings

### Core Editing Features
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.editor.enableCodeActions` | `true` | Controls if Copilot commands are shown as Code Actions when available |
| `github.copilot.renameSuggestions.triggerAutomatically` | `true` | Generate symbol renaming suggestions automatically |
| `github.copilot.enable` | `{ "*": true, "plaintext": false, "markdown": false, "scminput": false }` | Enable or disable code completions for specified languages |
| `github.copilot.nextEditSuggestions.enabled` | `true` | Enables next edit suggestions (NES) |
| `editor.inlineSuggest.edits.allowCodeShifting` | `"always"` | Configure if NES can shift code to show suggestions |
| `editor.inlineSuggest.edits.renderSideBySide` | `"auto"` | Configure if NES shows larger suggestions side-by-side or below relevant code |

### Language-Specific Configuration
```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false,
    "markdown": false,
    "scminput": false,
    "properties": false
  }
}
```

## Chat Settings

### Conversation Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.localeOverride` | `"auto"` | Specify locale for chat responses (en, fr, etc.) |
| `github.copilot.chat.useProjectTemplates` | `true` | Use relevant GitHub projects as starter projects when using /new |
| `github.copilot.chat.scopeSelection` | `false` | Prompt for specific symbol scope if using /explain with no selection |
| `github.copilot.chat.terminalChatLocation` | `"chatView"` | Controls where terminal chat queries should open |
| `chat.detectParticipant.enabled` | `true` | Enable chat participant detection in Chat view |

### Chat Interface Customization
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.editor.fontFamily` | `"default"` | Font family in chat codeblocks |
| `chat.editor.fontSize` | `14` | Font size in pixels in chat codeblocks |
| `chat.editor.fontWeight` | `"default"` | Font weight in chat codeblocks |
| `chat.editor.lineHeight` | `0` | Line height in pixels in chat codeblocks |
| `chat.editor.wordWrap` | `"off"` | Toggle line wrapping in chat codeblocks |

### Chat Editing Behavior
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.editing.confirmEditRequestRemoval` | `true` | Ask for confirmation before undoing an edit |
| `chat.editing.confirmEditRequestRetry` | `true` | Ask for confirmation before redoing last edit |
| `chat.editing.autoAcceptDelay` | `0` | Configure delay for auto-accepting suggested edits (0 = disabled) |
| `chat.editRequests` | `"inline"` | (Experimental) Enable or disable editing previous chat requests |

### Advanced Chat Features
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.codesearch.enabled` | `false` | (Preview) Auto-discover relevant files when using #codebase |
| `github.copilot.chat.edits.suggestRelatedFilesFromGitHistory` | `true` | (Experimental) Suggest related files from git history in Copilot Edits |
| `chat.sendElementsToChat.enabled` | `true` | (Experimental) Enable sending Simple Browser elements to chat as context |

## Agent Mode Settings

### Core Agent Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.agent.enabled` | `true` | Enable or disable agent mode (requires VS Code 1.99+) |
| `chat.agent.maxRequests` | `25` | Maximum number of requests Copilot can make in agent mode |
| `github.copilot.chat.agent.autoFix` | `true` | Automatically diagnose and fix issues in generated code changes |
| `github.copilot.chat.agent.runTasks` | `true` | Run workspace tasks when using agent mode |

### MCP Integration
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.mcp.enabled` | `true` | Enable Model Context Protocol (MCP) support for adding tools from MCP servers |
| `chat.tools.autoApprove` | `false` | (Experimental) Automatically approve all tools |
| `github.copilot.chat.newWorkspaceCreation.enabled` | `true` | (Experimental) Enable agent mode tool for scaffolding new workspaces |

### Advanced Agent Features
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.agent.thinkingTool` | `false` | (Experimental) Enable thinking tool in agent mode |

### Terminal Command Control
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.agent.terminal.allowList` | `{ "echo": true, "cd": true, "ls": true, "cat": true, "pwd": true, "Write-Host": true, "Set-Location": true, "Get-ChildItem": true, "Get-Content": true, "Get-Location": true }` | (Experimental) Terminal commands allowed without confirmation |
| `github.copilot.chat.agent.terminal.denyList` | `{ "rm": true, "rmdir": true, "del": true, "kill": true, "curl": true, "wget": true, "eval": true, "chmod": true, "chown": true, "Remove-Item": true }` | (Experimental) Terminal commands not allowed without confirmation |

## Inline Chat Settings

### Interaction Behavior
| Setting | Default | Description |
|---------|---------|-------------|
| `inlineChat.finishOnType` | `false` | Finish inline chat session when typing outside changed regions |
| `inlineChat.holdToSpeech` | `true` | Holding Ctrl+I automatically enables speech recognition |
| `editor.inlineSuggest.syntaxHighlightingEnabled` | `true` | Show syntax highlighting for code completions |

### Experimental Inline Features
| Setting | Default | Description |
|---------|---------|-------------|
| `inlineChat.lineEmptyHint` | `false` | (Experimental) Show hint for inline chat on empty line |
| `inlineChat.lineNaturalLanguageHint` | `true` | (Experimental) Trigger inline chat when line mostly consists of words |
| `github.copilot.chat.editor.temporalContext.enabled` | `false` | (Experimental) Include recently viewed/edited files in inline chat context |

## Code Review Settings

### Review Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.reviewSelection.enabled` | `true` | (Preview) Enable code review with AI for editor text selection |
| `github.copilot.chat.reviewSelection.instructions` | `[]` | (Preview) Custom instructions added to review requests |

### Example Review Instructions
```json
{
  "github.copilot.chat.reviewSelection.instructions": [
    "Focus on security vulnerabilities",
    "Check for performance issues",
    "Verify error handling patterns",
    "Ensure code follows team standards"
  ]
}
```

## Custom Instructions Settings

### Instruction File Management
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.codeGeneration.useInstructionFiles` | `true` | Automatically add custom instructions from .github/copilot-instructions.md |
| `chat.instructionsFilesLocations` | `{ ".github/instructions": true }` | (Experimental) Locations to search for custom instructions files |

### Specialized Instructions
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.commitMessageGeneration.instructions` | `[]` | (Experimental) Custom instructions for generating commit messages |
| `github.copilot.chat.pullRequestDescriptionGeneration.instructions` | `[]` | (Experimental) Custom instructions for generating PR titles and descriptions |

### Example Custom Instructions
```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    "Always include TypeScript type annotations",
    "Use functional programming patterns when possible",
    "Include comprehensive error handling",
    "Follow company coding standards in .eslintrc"
  ]
}
```

## Reusable Prompt Files Settings

### Prompt File Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.promptFiles` | `true` | (Experimental) Enable or disable reusable prompt files |
| `chat.promptFilesLocations` | `{ ".github/prompts": true }` | (Experimental) Locations to search for prompt files |

## Chat Mode Settings

### Mode File Management
| Setting | Default | Description |
|---------|---------|-------------|
| `chat.modeFilesLocations` | `{ ".github/chatmodes": true }` | (Experimental) Locations to search for chat mode files |

## Debugging Settings

### Debug Feature Control
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.startDebugging.enabled` | `true` | (Preview) Enable /startDebugging intent in Chat view |
| `github.copilot.chat.copilotDebugCommand.enabled` | `true` | (Preview) Enable copilot-debug terminal command |

## Testing Settings

### Test Generation Features
| Setting | Default | Description |
|---------|---------|-------------|
| `github.copilot.chat.generateTests.codeLens` | `false` | (Experimental) Show Generate tests code lens for uncovered symbols |
| `github.copilot.chat.setupTests.enabled` | `true` | (Experimental) Enable /setupTests intent and prompting in /tests generation |

## Notebook Settings

### Jupyter Integration
| Setting | Default | Description |
|---------|---------|-------------|
| `notebook.experimental.generate` | `true` | (Experimental) Enable Generate action for creating code cells with inline chat |
| `github.copilot.chat.edits.newNotebook.enabled` | `true` | (Experimental) Enable notebook tool in edit mode |
| `github.copilot.chat.notebook.followCellExecution.enabled` | `false` | (Experimental) Show currently executing cell in editor |

## Accessibility Settings

### Diff and Interaction Accessibility
| Setting | Default | Description |
|---------|---------|-------------|
| `inlineChat.accessibleDiffView` | `"auto"` | Whether Inline Chat renders accessible diff viewer for changes |

### Audio Cues and Signals
| Setting | Default | Description |
|---------|---------|-------------|
| `accessibility.signals.chatRequestSent` | `{ "sound": "auto", "announcement": "auto" }` | Audio cue when chat request is made |
| `accessibility.signals.chatResponseReceived` | `{ "sound": "auto" }` | Audio cue when response received |
| `accessibility.signals.chatEditModifiedFile` | `{ "sound": "auto" }` | Audio cue when file modified by chat edits |
| `accessibility.signals.chatUserActionRequired` | `{ "sound": "auto", "announcement": "auto" }` | Audio cue when user action needed |
| `accessibility.signals.lineHasInlineSuggestion` | `{ "sound": "auto" }` | Audio cue when cursor on line with inline suggestion |
| `accessibility.signals.nextEditSuggestion` | `{ "sound": "auto", "announcement": "auto" }` | Audio cue when next edit suggestion available |

### Verbosity and Help
| Setting | Default | Description |
|---------|---------|-------------|
| `accessibility.verbosity.inlineChat` | `true` | Provide information about accessing inline chat accessibility help |
| `accessibility.verbosity.inlineCompletions` | `true` | Provide information about accessing inline completions hover and Accessible View |
| `accessibility.verbosity.panelChat` | `true` | Provide information about accessing chat help menu |

### Voice Integration
| Setting | Default | Description |
|---------|---------|-------------|
| `accessibility.voice.keywordActivation` | `"off"` | Controls whether 'Hey Code' phrase starts voice chat session |
| `accessibility.voice.autoSynthesize` | `"off"` | Controls whether textual responses are read aloud when speech was input |
| `accessibility.voice.speechTimeout` | `1200` | Duration in milliseconds that voice recognition remains active |

## Configuration Best Practices

### Workspace-Specific Settings
Store project-specific Copilot settings in `.vscode/settings.json`:
```json
{
  "github.copilot.enable": {
    "*": true,
    "markdown": true
  },
  "github.copilot.chat.localeOverride": "en",
  "chat.agent.maxRequests": 50
}
```

### Team Settings
Share team standards through version-controlled settings:
```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.instructionsFilesLocations": {
    ".github/instructions": true,
    "docs/copilot": true
  }
}
```

### Performance Optimization
```json
{
  "github.copilot.nextEditSuggestions.enabled": true,
  "editor.inlineSuggest.edits.allowCodeShifting": "always",
  "chat.editing.autoAcceptDelay": 3000
}
```

## Related Documentation
- [Copilot VS Code Features](copilot-vscode-features.md)
- [Workspace Context](workspace-context.md)
- [Tips and Tricks](../tips-and-tricks.md)
- [Copilot Chat](../chat/copilot-chat.md)

## External Resources
- [VS Code Settings Documentation](https://code.visualstudio.com/docs/getstarted/settings)
- [GitHub Copilot Feature Lifecycle](https://code.visualstudio.com/docs/configure/settings#_feature-lifecycle)
- [VS Code User and Workspace Settings](https://code.visualstudio.com/docs/configure/settings)

This settings reference empowers you to fully customize your GitHub Copilot experience in VS Code, from basic functionality to advanced AI-powered workflows, ensuring optimal productivity and alignment with your development preferences.
