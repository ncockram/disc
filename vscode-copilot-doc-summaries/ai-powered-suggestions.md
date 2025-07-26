# Code completions with GitHub Copilot in VS Code

**Source:** https://code.visualstudio.com/docs/copilot/ai-powered-suggestions

## Summary

GitHub Copilot provides AI-powered code completion capabilities directly in the VS Code editor, offering two main types of suggestions: code completions that appear as you type, and next edit suggestions that predict future code changes. The system analyzes your coding style, existing code context, and provides suggestions across a broad range of programming languages and frameworks.

## Overview

GitHub Copilot acts as an AI-powered pair programmer, automatically offering suggestions for:
- Code completion and implementation
- Comments and documentation
- Tests and validation code
- Refactoring and improvements

### Two Types of Suggestions

1. **Code Completions**: Real-time suggestions that appear as you type, matching your coding style and considering existing code context
2. **Next Edit Suggestions (NES)**: Predictive suggestions that anticipate your next code edit based on current changes

## Getting Started

### Setup Requirements
1. **Install GitHub Copilot Extension**: Use VS Code extension marketplace
2. **Authentication**: Sign in with your GitHub account
3. **Subscription**: Use Copilot Free plan or paid subscription

> **Tip**: Copilot Free provides monthly limits on completions and chat interactions without requiring a paid subscription.

### Quick Start
- Follow the [Copilot Quickstart](https://code.visualstudio.com/docs/copilot/getting-started) to discover key features
- No additional configuration needed - suggestions appear automatically as you type

## Inline Suggestions

### Basic Functionality
- Suggestions appear as dimmed ghost text while typing
- Accept suggestions with **Tab** key
- Copilot adapts to your existing coding style and patterns

### Example Scenarios
```javascript
// Typing this...
function calculateDaysBetweenDates

// Copilot suggests complete implementation
function calculateDaysBetweenDates(date1, date2) {
    const timeDifference = date2.getTime() - date1.getTime();
    return Math.ceil(timeDifference / (1000 * 3600 * 24));
}
```

### Advanced Features

#### Partially Accepting Suggestions
- **Ctrl+Right**: Accept next word of suggestion
- **Ctrl+Right** (continued): Accept next line of suggestion
- Allows granular control over suggestion acceptance

#### Alternative Suggestions
- Hover over suggestions to view multiple alternatives
- Navigate between options using:
  - Arrow controls in hover menu
  - **Alt+]**: Next suggestion
  - **Alt+[**: Previous suggestion

#### Generate Suggestions from Code Comments
Use descriptive comments to guide Copilot's suggestions:

```typescript
// Create a Student class with name, age, and grade properties
// Include methods for getGPA() and isEligibleForGraduation()
class Student {
    // Copilot generates implementation based on comments
}
```

#### Style Consistency
Copilot maintains consistency with existing code patterns:
- Parameter naming conventions
- Indentation and formatting
- Code organization patterns
- Language-specific idioms

## Next Edit Suggestions (NES)

### Overview
Next Edit Suggestions represent an evolution beyond traditional code completion, predicting both:
- **Location** of your next edit
- **Content** of that edit

### Enabling NES
Enable in VS Code settings: `github.copilot.nextEditSuggestions.enabled`

### Visual Indicators
- **Gutter Arrow**: Points to suggested edit locations
- **Arrow Direction**: Points down if suggestion is below current view
- **Hover Menu**: Shows keyboard shortcuts and configuration options

### Navigation and Acceptance
- **Tab**: Navigate to next suggested edit
- **Tab** (at suggestion): Accept the suggestion
- **Hover**: Explore edit suggestion menu with options

### Display Options
Control visual distractions with `editor.inlineSuggest.edits.showCollapsed`:
- **Expanded** (default): Show code changes immediately
- **Collapsed**: Hide changes until Tab navigation or hover

### Use Cases

#### Catching and Correcting Mistakes
- **Simple Typos**: `cont x = 5` → `const x = 5`
- **Logic Errors**: Inverted ternary expressions, incorrect operators
- **Comparison Mistakes**: `||` → `&&` where appropriate

#### Changing Intent
- **Class Evolution**: `Point` → `Point3D` triggers suggestions to add `z` properties
- **Cascading Updates**: Automatically suggests related changes throughout codebase

#### Refactoring Support
- **Variable Renaming**: Rename once, get suggestions for all occurrences
- **Naming Pattern Updates**: Apply new naming conventions consistently
- **Code Style Matching**: Adapt pasted code to match existing style

## Configuration and Control

### Enable/Disable Code Completions

#### Global Settings
- **Status Bar Menu**: Toggle completions on/off
- **Settings**: Modify `github.copilot.enable` for all languages
- **Language-Specific**: Set per-language enablement

#### Snooze Functionality
- **Temporary Disable**: Use snooze button for 5-minute intervals
- **Quick Resume**: Cancel snooze when ready
- **Command Palette**: Access snooze commands

### Language Model Selection

#### Changing Completion Models
1. **Command Palette**: `GitHub Copilot: Change Completions Model`
2. **Model Selection**: Choose from available models
3. **Command Center**: Access via Copilot menu in title bar

#### Model Considerations
- Different models have varying capabilities and strengths
- Available models may change over time
- Enterprise users may have additional model options

### Workspace Management

#### Context Optimization
- **Related Files**: Keep relevant files open for better context
- **Project Structure**: Copilot analyzes open files for context
- **File Relationships**: Better suggestions with comprehensive context

## Settings Configuration

### Code Completion Settings
- `github.copilot.enable`: Enable/disable for all or specific languages
- `editor.inlineSuggest.fontFamily`: Configure suggestion font
- `editor.inlineSuggest.showToolbar`: Show/hide suggestion toolbar
- `editor.inlineSuggest.syntaxHighlightingEnabled`: Enable syntax highlighting

### Next Edit Suggestions Settings
- `github.copilot.nextEditSuggestions.enabled`: Enable NES feature
- `editor.inlineSuggest.edits.allowCodeShifting`: Allow code shifting for suggestions
- `editor.inlineSuggest.edits.renderSideBySide`: Control suggestion display layout
  - `auto`: Show side-by-side when space allows
  - `never`: Always show below relevant code

### Display Customization
- **Side-by-Side**: Automatic based on viewport space
- **Below Code**: Consistent placement option
- **Toolbar Controls**: Customizable suggestion interface

## Tips & Tricks

### Context Optimization
- **Open Related Files**: Helps Copilot understand project structure
- **Maintain File Relationships**: Keep dependent files accessible
- **Project Organization**: Better context leads to more relevant suggestions

### Effective Usage Patterns
- **Descriptive Comments**: Guide suggestions with clear intent
- **Consistent Coding Style**: Helps Copilot match your patterns
- **Iterative Refinement**: Use alternative suggestions for better results
- **Strategic Acceptance**: Use partial acceptance for precision

## Troubleshooting

### Common Issues
- **No Suggestions**: Check internet connection and authentication
- **Irrelevant Suggestions**: Improve context with related files
- **Performance**: Consider model selection for speed vs. quality trade-offs

### Configuration Problems
- **Extension Issues**: Reinstall GitHub Copilot extension
- **Settings Reset**: Check and reset relevant settings
- **Authentication**: Re-authenticate with GitHub account

## Next Steps

### Learning Path
1. **Quickstart Tutorial**: [Copilot Quickstart](https://code.visualstudio.com/docs/copilot/chat/getting-started-chat)
2. **Chat Features**: [Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
3. **Video Series**: [VS Code Copilot Series](https://www.youtube.com/playlist?list=PLj6YeMhvp2S5_hvBl2SE-7YCHYlLQ0bPt)

### Advanced Features
- **Language Models**: [Choose between different AI models](https://code.visualstudio.com/docs/copilot/language-models)
- **Chat Integration**: Combine completions with conversational AI
- **Customization**: Tailor Copilot to your specific workflow

## Related Documentation

- [Copilot Setup Guide](https://code.visualstudio.com/docs/copilot/setup)
- [Getting Started Tutorial](https://code.visualstudio.com/docs/copilot/getting-started)
- [Language Model Selection](https://code.visualstudio.com/docs/copilot/language-models)
- [Copilot Chat Features](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [GitHub Copilot Free Plan](https://github.com/github-copilot/signup)
