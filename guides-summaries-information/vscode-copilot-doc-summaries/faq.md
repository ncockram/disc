# GitHub Copilot Frequently Asked Questions

## Overview

This comprehensive FAQ addresses common questions, troubleshooting scenarios, and practical guidance for using GitHub Copilot effectively in Visual Studio Code.

## GitHub Copilot Subscription

### How can I get a Copilot subscription?

**Individual Users:**
- **Copilot Free**: Explore basic functionality at no cost with monthly limits on completions and chat interactions
- **Paid Plans**: Upgrade for unlimited access and premium features

**Organization/Enterprise Members:**
- Request access through your organization at [GitHub Copilot settings](https://github.com/settings/copilot)
- Contact your IT administrator to enable Copilot for your organization
- Visit organization settings to request access under "Get Copilot from an organization"

### How can I monitor my Copilot usage?

Access the **Copilot Status Dashboard** through the VS Code Status Bar:

**Usage Metrics:**
- **Completions**: Percentage of code completion quota used
- **Chat Messages**: Percentage of chat request quota consumed
- **Premium Requests**: Premium feature usage percentage
- **Premium Overage**: Number of premium requests exceeding your plan

**Additional Monitoring:**
- View detailed usage statistics in GitHub account settings
- Track monthly usage patterns and trends
- Monitor team usage across organization accounts

### I reached my completions or chat interactions limit

**Understanding Limits:**
- Limits reset monthly from your initial signup date
- Free plan has monthly quotas for completions and chat interactions
- Paid subscriptions offer unlimited usage

**Solutions:**
1. **Upgrade to Paid Plan**: Get unlimited completions and chat messages
2. **Wait for Reset**: Continue with free tier when monthly quota resets
3. **Partial Usage**: Use remaining quota for either completions or chat if only one limit is reached

**Visual Indicators:**
- Status bar notifications when approaching limits
- Chat view warnings when limits are reached
- Title bar indicators for quota status

### My Copilot subscription is not detected in VS Code

**Account Verification:**
1. **Check GitHub Account**: Ensure you're signed in with the correct GitHub account
2. **Verify Subscription**: Confirm active subscription in [GitHub Copilot settings](https://github.com/settings/copilot)
3. **Account Switching**: Use VS Code Accounts menu to switch GitHub accounts

**Managed Accounts (GHE.com):**
- Update settings before signing in for managed accounts
- Configure enterprise-specific authentication
- Follow [GitHub Enterprise Cloud guidance](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/using-github-copilot-with-an-account-on-ghecom)

### How can I switch accounts for Copilot?

**Account Management:**
1. **Sign Out**: Use Accounts menu in Activity Bar to sign out
2. **Sign In**: Sign in with the account that has Copilot access
3. **Verification**: Confirm subscription detection in Status Bar

## General Questions

### How can I remove Copilot from VS Code?

**Quick Removal:**
1. **Hide Copilot**: Select "Hide Copilot" from Copilot menu in title bar
2. **Extension Removal**: Uninstall Copilot and Copilot Chat extensions from Extensions view
3. **Complete Cleanup**: Remove Copilot menu, Status Bar indicators, and Chat view

**Restoration:**
- Run `Chat: Use AI Features with Copilot for free` from Command Palette
- Reinstall extensions if previously uninstalled

### Network and firewall configuration for Copilot

**Corporate Networks:**
- **Firewall Allowlists**: Add GitHub Copilot domains to firewall allowlists
- **Proxy Configuration**: Configure HTTP proxy settings for corporate environments
- **VPN Considerations**: Ensure VPN settings don't block Copilot connections

**Troubleshooting Resources:**
- [Firewall Settings Guide](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot)
- [Network Error Troubleshooting](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-network-errors-for-github-copilot)

### My request is rate-limited

**Understanding Rate Limits:**
- GitHub implements rate limits for fair access and abuse protection
- Temporary restrictions to ensure service availability for all users
- Automatic reset after rate limit period expires

**Solutions:**
- Wait for rate limit reset (typically short-term)
- Review usage patterns to avoid excessive requests
- See [Rate Limits Documentation](https://docs.github.com/en/copilot/troubleshooting-github-copilot/rate-limits-for-github-copilot) for detailed guidance

### Are there pre-release builds of the Copilot extensions?

**Pre-release Access:**
1. **Switch to Pre-release**: Right-click extension in Extensions view
2. **Select Option**: Choose "Switch to Pre-Release Version"
3. **Identify Version**: Look for "Pre-release" badge in extension details

**Benefits:**
- Access to latest features and bug fixes
- Early testing of upcoming functionality
- Faster access to improvements and enhancements

## Code Completions

### How do I enable or disable code completions?

**Global Controls:**
- Use Copilot Status Dashboard from Status Bar
- Toggle completions globally or by file type
- Configure language-specific completion settings

**File-Type Specific:**
- Enable/disable for specific programming languages
- Maintain different settings for different file types
- Use workspace-specific completion preferences

### Inline completions are not working in the editor

**Troubleshooting Checklist:**
1. **Verify Settings**: Ensure Copilot is not disabled globally or for the current language
2. **Check Subscription**: Confirm active GitHub Copilot subscription
3. **Network Connectivity**: Verify connection to GitHub Copilot services
4. **Usage Limits**: Check if monthly completion limits have been reached (Free plan)

**Additional Steps:**
- Restart VS Code and reload extensions
- Check for extension updates
- Review error logs for specific issues

## Chat Features

### Chat features aren't working for me

**Requirements Verification:**
1. **VS Code Version**: Ensure latest VS Code version (`Code: Check for Updates`)
2. **Extension Updates**: Update GitHub Copilot and Copilot Chat extensions
3. **Active Subscription**: Verify active Copilot subscription in GitHub settings
4. **Usage Limits**: Check monthly chat interaction limits (Free plan)

**Additional Checks:**
- Confirm GitHub account authentication in VS Code
- Verify network connectivity to GitHub services
- Review extension compatibility and conflicts

## Troubleshooting and Feedback

### How can I provide feedback on Copilot?

**Code Completions Feedback:**
- Use "Send Copilot Completion Feedback" when hovering over completions
- Provide detailed reproduction steps in Issue Reporter
- Include context about expected vs. actual behavior

**Next Edit Suggestions:**
- Select "Feedback" action in next edit suggestions menu
- Describe issues with specific edit suggestions
- Include details about editor context and expected behavior

**General Issues:**
1. **Issue Reporter**: Use Help > Report Issue in VS Code
2. **Select Extension**: Choose "GitHub Copilot Chat" as extension
3. **Detailed Description**: Include reproduction steps and environment details

**GitHub Repository:**
- Submit issues to [microsoft/vscode](https://github.com/microsoft/vscode) repository
- Follow [Copilot Issues Wiki](https://github.com/microsoft/vscode/wiki/Copilot-Issues) guidelines

### View logs for GitHub Copilot in VS Code

**Detailed Logging:**
1. **Set Log Level**: Run `Developer: Set Log Level` and select "Trace"
2. **Output Channels**: Run `Output: Show Output Channels`
3. **Select Channel**: Choose "GitHub Copilot" or "GitHub Copilot Chat"
4. **View Logs**: Monitor real-time logging in Output panel

**Network Diagnostics:**
1. **Command Palette**: Open with `Ctrl+Shift+P`
2. **Run Diagnostics**: Execute `GitHub Copilot: Collect Diagnostics`
3. **Review Results**: Inspect connectivity and service status information

### Use the Chat Debug view

**Debugging Features:**
- **Request/Response Details**: View AI requests and responses
- **Prompt Analysis**: Inspect prompts sent to language models
- **Context Examination**: Understand context provided to AI
- **Response Interpretation**: Analyze how AI interprets requests

**Access Method:**
- Enable Chat Debug view from Copilot settings
- Access detailed interaction logs and debugging information
- Use for troubleshooting complex chat interactions

## Additional Resources

### Official Documentation
- [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center/)
- [GitHub Copilot FAQ](https://github.com/features/copilot#faq)
- [VS Code Copilot Documentation](https://code.visualstudio.com/docs/copilot/overview)

### Community Support
- [VS Code GitHub Repository](https://github.com/microsoft/vscode)
- [Stack Overflow - VS Code Tag](https://stackoverflow.com/questions/tagged/vscode)
- [GitHub Discussions](https://github.com/github/copilot-discussions)

### Learning Resources
- [Copilot Best Practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
- [Prompt Engineering Guide](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [VS Code Tips and Tricks](tips-and-tricks.md)

## Related Documentation
- [Copilot Setup](../setup.md)
- [Copilot Chat](../chat/copilot-chat.md)
- [Tips and Tricks](tips-and-tricks.md)
- [VS Code Copilot Features](../reference/copilot-vscode-features.md)

This FAQ serves as your comprehensive guide to resolving common issues and maximizing your GitHub Copilot experience in VS Code. For issues not covered here, consult the official documentation or submit feedback through the appropriate channels.
