# VS Code Copilot Edit Mode (Copilot Edits)

**Source:** [VS Code Copilot Edits](https://code.visualstudio.com/docs/copilot/chat/copilot-edits)

## Introduction

Copilot Edit mode (also known as Copilot Edits) is designed for **targeted code modifications** across multiple files. Unlike Ask mode which provides information, Edit mode directly modifies your codebase with precise, reviewable changes that you can accept or reject.

## Key Features

### Multi-File Editing
- **Coordinated changes** across related files
- **Dependency awareness** - understands file relationships
- **Consistent updates** - maintains code style and patterns
- **Atomic operations** - related changes grouped together

### Change Management
- **Diff-based previews** - see exactly what will change
- **Granular control** - accept/reject individual edits
- **Undo/redo support** - revert changes if needed
- **Integration with Git** - works with version control workflows

### Intelligent Code Modification
- **Context-aware edits** - understands existing code structure
- **Syntax preservation** - maintains valid code at all times
- **Import management** - automatically handles imports/exports
- **Style consistency** - follows existing code patterns

## Getting Started with Edit Mode

### Activating Edit Mode

1. **Chat View** (`Ctrl+Alt+I`) - Select "Edit" from the mode dropdown
2. **Quick command** - Use `Ctrl+Shift+P` → "Copilot: Start Edit Session"  
3. **Mode switcher** - Click the mode selector in an existing chat
4. **Context menu** - Right-click in editor → "Edit with Copilot"

### Basic Edit Requests

**Simple modifications:**
```
Add error handling to this function

Refactor this component to use React hooks

Fix the TypeScript errors in this file
```

**Feature additions:**
```
Add input validation to this form

Implement dark mode toggle functionality

Add logging to all API endpoints
```

**Code improvements:**
```
Optimize this database query

Make this component more accessible

Improve the performance of this algorithm
```

## Working with File Context

### Single File Edits

Target specific files for modification:

```
#components/Header.jsx Add responsive design to this header component

#utils/validation.js Add email and phone number validation functions

#api/auth.js Implement JWT token refresh logic
```

### Multi-File Coordination

Edit related files together:

```
#components/LoginForm.jsx #hooks/useAuth.js #types/User.ts 
Add password strength requirements to the login system

#server.js #routes/api.js #middleware/auth.js 
Add rate limiting to all authentication endpoints
```

### Project-Wide Changes

Make consistent changes across the codebase:

```
Convert all class components to functional components with hooks

Add TypeScript type annotations to all JavaScript files

Implement proper error boundaries throughout the application
```

## Edit Mode Workflow

### 1. Request Changes

Describe what you want to modify:

```
#src/components/ProductCard.jsx 
Add a "Add to Cart" button with loading state and success feedback
```

### 2. Review Proposed Changes

Edit mode shows:
- **Files to be modified** - List of affected files
- **Change preview** - Diff view of modifications
- **Added/removed lines** - Clear indication of what changes
- **Syntax highlighting** - Easy-to-read code formatting

### 3. Accept or Reject Changes

For each file, you can:
- **Accept all changes** - Apply all modifications to the file
- **Reject all changes** - Cancel all modifications
- **Review individual changes** - Examine specific sections
- **Partial acceptance** - Accept some changes, reject others

### 4. Iterate and Refine

Continue with follow-up requests:

```
Now add unit tests for the new Add to Cart functionality

Improve the accessibility of the button we just added

Make the loading state more visually appealing
```

## Advanced Edit Patterns

### Refactoring Workflows

**Extract functionality:**
```
#src/utils/api.js Extract the authentication logic into a separate auth service
```

**Consolidate code:**
```
#components/Button/ #components/Input/ #components/Select/
Create a unified form component library from these individual components
```

**Modernize code:**
```
#legacy/oldController.js Convert this legacy code to use modern async/await patterns
```

### Feature Implementation

**Complete feature additions:**
```
#src/pages/Profile.jsx #src/hooks/ #src/types/
Add user profile editing functionality with form validation and image upload
```

**API integration:**
```
#src/services/ #src/types/ #src/hooks/
Integrate with the new payment API including error handling and loading states
```

### Bug Fixes and Improvements

**Targeted fixes:**
```
#src/components/DataTable.jsx Fix the pagination bug that occurs with filtered data
```

**Performance improvements:**
```
#src/hooks/useDataFetching.js Optimize this hook to prevent unnecessary API calls
```

**Security enhancements:**
```
#src/middleware/validation.js Add input sanitization to prevent XSS attacks
```

## Change Review and Management

### Understanding Diffs

Edit mode provides clear diff views:

```diff
// Before (Red background)
- function handleSubmit(data) {
-   fetch('/api/submit', { method: 'POST', body: data });
- }

// After (Green background)  
+ async function handleSubmit(data) {
+   try {
+     const response = await fetch('/api/submit', { 
+       method: 'POST', 
+       body: JSON.stringify(data),
+       headers: { 'Content-Type': 'application/json' }
+     });
+     if (!response.ok) throw new Error('Submission failed');
+     return await response.json();
+   } catch (error) {
+     console.error('Error submitting data:', error);
+     throw error;
+   }
+ }
```

### File-by-File Review

Review changes systematically:

1. **Open each modified file** - See changes in context
2. **Check imports/exports** - Verify dependencies are updated
3. **Test functionality** - Ensure changes work as expected
4. **Review style consistency** - Check adherence to project conventions

### Selective Acceptance

Accept only the changes you want:

- **Accept file** - Apply all changes to this file
- **Reject file** - Keep original version
- **Review sections** - Examine specific code blocks
- **Manual editing** - Modify accepted changes further

### Undo and Redo

Manage change history:

- **Undo last edit** - Revert the most recent change set
- **Redo edits** - Reapply previously undone changes
- **View edit history** - See sequence of modifications
- **Reset session** - Return to original state

## Integration with Development Workflow

### Version Control Integration

Edit mode works with Git:

- **Stage changes** - Git sees edit mode changes as normal file modifications
- **Commit incrementally** - Commit accepted changes as you review
- **Branch workflows** - Use edit mode on feature branches
- **Merge conflict resolution** - Edit mode can help resolve conflicts

### Testing Integration

Combine edits with testing:

```
#src/components/Calculator.jsx Add comprehensive error handling to all calculation methods

#tests/Calculator.test.js Update tests to cover the new error handling scenarios
```

### Code Review Process

Use edit mode in code reviews:

1. **Review pull requests** with edit mode assistance
2. **Implement feedback** using targeted edit requests
3. **Refactor based on comments** with multi-file coordination
4. **Document changes** automatically

## Best Practices

### Effective Edit Requests

**Be specific about requirements:**
```
// Instead of: "Make this better"
// Use: "Add input validation, error handling, and loading states to this form component"
```

**Provide context and constraints:**
```
#components/UserForm.jsx Add form validation using Yup schema validation, following the existing validation patterns in #utils/validation.js
```

**Specify scope clearly:**
```
// For single file: 
#Button.jsx Make this button component more accessible

// For related files:
#Button.jsx #Button.test.js #Button.stories.js Update button component and all related files for new size variants
```

### Change Management

**Review before accepting:**
- Always examine proposed changes
- Test functionality after accepting
- Check for unintended side effects
- Verify imports and dependencies

**Iterate incrementally:**
- Make small, focused changes
- Test each iteration
- Build complexity gradually
- Keep changes logically grouped

**Document significant changes:**
- Update comments and documentation
- Add changelog entries
- Update README files
- Inform team members

### Performance Considerations

**Limit scope appropriately:**
- Avoid overly broad change requests
- Focus on specific functionality
- Break large tasks into smaller edits
- Consider performance impact of changes

**Use context efficiently:**
- Include only relevant files in context
- Reference specific functions/classes when possible
- Avoid including large files unnecessarily
- Be mindful of token limits

## Common Edit Patterns

### Component Enhancement

```
#src/components/ProductList.jsx 
Add infinite scrolling, loading states, and error handling to this product list component
```

### API Integration

```
#src/services/api.js #src/hooks/useProducts.js #src/types/Product.ts
Update the product API service to include filtering and sorting capabilities
```

### State Management Updates

```
#src/store/userSlice.js #src/hooks/useUser.js 
Add user preferences functionality to the existing user state management
```

### Testing and Documentation

```
#src/utils/formatters.js #tests/formatters.test.js #docs/utils.md
Add comprehensive tests and documentation for all formatter functions
```

### Migration and Modernization

```
#src/legacy/ Convert all class components in this directory to functional components with hooks
```

## Troubleshooting

### Common Issues

**Changes not applied correctly:**
- Check file permissions and write access
- Verify files aren't read-only
- Ensure proper Git status
- Check for syntax errors in modified files

**Context not understood:**
- Provide more specific file references
- Include related dependencies in context
- Clarify the relationship between files
- Add comments explaining complex logic

**Performance problems:**
- Reduce context size for large edits
- Break complex changes into smaller requests
- Avoid including very large files
- Focus on specific functions/sections

### Best Debugging Practices

**Incremental validation:**
```
// 1. Make small changes first
Add just the button component without any functionality

// 2. Add behavior incrementally  
Now add the click handler for the button

// 3. Add advanced features
Finally add the loading state and success feedback
```

**Test immediately:**
- Run tests after each significant change
- Verify functionality in browser/environment
- Check console for errors
- Validate type checking (TypeScript)

## Related Resources

- **[Chat Modes Overview](./chat-modes.md)** - Understanding when to use Edit mode
- **[Chat Context Management](./copilot-chat-context.md)** - Providing effective context for edits
- **[Agent Mode Guide](./chat-agent-mode.md)** - For more complex, autonomous editing
- **[Ask Mode Guide](./chat-ask-mode.md)** - For understanding before editing
- **[Getting Started Guide](./getting-started-chat.md)** - Hands-on tutorial including Edit mode

---

*Edit mode is powerful for making precise, coordinated changes across your codebase. Use it when you know what needs to change and want direct control over the modification process.*
