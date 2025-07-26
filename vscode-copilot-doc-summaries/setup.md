# Set up GitHub Copilot in VS Code

**Source:** https://code.visualstudio.com/docs/copilot/setup

## Summary

This guide provides step-by-step instructions for setting up GitHub Copilot in Visual Studio Code. It covers getting access to Copilot, installation, configuration, and management options for different use cases.

## Get Access to GitHub Copilot

There are different ways to access GitHub Copilot depending on your situation:

### Individual Users
- **Copilot Free**: Set up GitHub Copilot Free for a limited experience without subscription
- **Paid Subscription**: Sign up for unlimited completions and chat interactions
- **Free Trial**: Try GitHub Copilot for free with a one-time 30-day trial
- **Resources**: See "Setting up GitHub Copilot for yourself" for all options

### Organization/Enterprise Members
- **Request Access**: Go to https://github.com/settings/copilot
- **Organization Access**: Request access under "Get Copilot from an organization"
- **Admin Setup**: Organization administrators can enable Copilot using "Setting up GitHub Copilot for your organization"

## Set up Copilot in VS Code

### Prerequisites
- Active GitHub Copilot subscription or access to Copilot Free
- Visual Studio Code installed

### Installation Steps

1. **Access Setup Interface**
   - Hover over the Copilot icon in the Status Bar
   - Select "Set up Copilot"

2. **Sign In Process**
   - Select "Sign in" to sign in to your GitHub account
   - Or select "Use Copilot" if already signed in

3. **Free Plan Enrollment**
   - If no subscription exists, automatic enrollment in Copilot Free plan
   - Monthly limits apply for completions and chat interactions

### Important Telemetry Information
- Telemetry is enabled by default in free version
- Code suggestions matching public code are allowed by default
- **Disable Telemetry**: Set `telemetry.telemetryLevel` to `off` in VS Code settings
- **Adjust Settings**: Modify telemetry and code suggestions in [Copilot Settings](https://github.com/settings/copilot)

### Getting Started
- Once setup is complete, Copilot is ready to use
- Follow the [Copilot Quickstart](https://code.visualstudio.com/docs/copilot/getting-started) to learn basics

## Use a Different GitHub Account with Copilot

### Sign Out Process
1. **Access Accounts Menu**
   - Select the Accounts menu in the Activity Bar
   - Choose "Sign out" for the current GitHub account used with Copilot

### Sign In Methods
Choose any of the following methods to sign in with a different account:

1. **Status Menu Method**
   - Select "Sign in to use Copilot" from the Copilot status menu

2. **Activity Bar Method**
   - Select the Accounts menu in Activity Bar
   - Choose "Sign in with GitHub to use GitHub Copilot"

3. **Command Palette Method**
   - Run the "GitHub Copilot: Sign in" command
   - Use keyboard shortcut: Ctrl+Shift+P

## Hide Copilot in VS Code

### Complete Hiding
- Select "Hide Copilot" from the Copilot menu in VS Code title bar
- Completely removes Copilot from the interface

### Re-enabling Hidden Copilot
- Run "Chat: Use AI Features with Copilot for Free" command
- Access via Command Palette (Ctrl+Shift+P)

## Disable Copilot for a Workspace

### Workspace-Specific Disabling
1. **Open Extensions View**
   - Use keyboard shortcut: Ctrl+Shift+X

2. **Find GitHub Copilot Extension**
   - Search for "GitHub Copilot"

3. **Disable Extension**
   - Select the gear icon
   - Choose "Disable (Workspace)"

4. **Restart Extensions**
   - Select "Restart extensions"

5. **Re-enabling**
   - Select "Enable (Workspace)" button after restart

### Benefits of Workspace Disabling
- Maintains Copilot availability in other workspaces
- Useful for projects where AI assistance is not desired
- Easy to toggle on/off as needed

## Configuration Options

### Telemetry Management
- **Global Disable**: Set telemetry level to "off" in VS Code settings
- **Copilot-Specific**: Adjust settings in GitHub Copilot Settings dashboard
- **Code Matching**: Control whether suggestions can match public code

### Account Management
- **Multiple Accounts**: Easy switching between different GitHub accounts
- **Organization Access**: Request access through organization administrators
- **Subscription Tiers**: Support for Free, Individual, and Enterprise plans

## Troubleshooting

### Common Issues
- **Sign-in Problems**: Use multiple sign-in methods available
- **Workspace Conflicts**: Disable/enable per workspace as needed
- **Account Switching**: Clear current session and sign in with correct account

### Access Issues
- **No Subscription**: Sign up for Copilot Free to get started
- **Organization Access**: Contact administrators for enterprise access
- **Trial Expiry**: Upgrade to paid subscription for continued access

## Next Steps

- **Quickstart Guide**: Continue with the [Copilot Quickstart](https://code.visualstudio.com/docs/copilot/getting-started)
- **Feature Discovery**: Learn key features and capabilities
- **Workflow Integration**: Understand how to incorporate Copilot into development workflow

## Related Resources

- [GitHub Copilot Free Plan](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-free/about-github-copilot-free)
- [Copilot Settings Dashboard](https://github.com/settings/copilot)
- [Setting up GitHub Copilot for Organizations](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-for-business)
- [Copilot Quickstart Guide](https://code.visualstudio.com/docs/copilot/getting-started)
- [VS Code Telemetry Settings](vscode://settings/telemetry.telemetryLevel)
