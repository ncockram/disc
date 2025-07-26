# AI Language Models in VS Code

**Source:** https://code.visualstudio.com/docs/copilot/language-models

## Summary

VS Code Copilot offers multiple AI language models optimized for different tasks, from fast code completions to complex reasoning. Users can choose between built-in models provided by GitHub Copilot or bring their own API keys to access models from various providers like Anthropic, Azure, Google, Groq, OpenAI, OpenRouter, and Ollama.

## Overview

Copilot provides flexible model selection to optimize for:
- **Speed**: Fast responses for quick tasks
- **Capability**: Advanced reasoning for complex problems
- **Specialization**: Models optimized for specific domains
- **Experimentation**: Access to latest models and features

## Model Selection Strategy

### Default Model Behavior
- **Base Model**: Fast, capable responses for general tasks
- **Task Coverage**: Coding, summarization, knowledge questions, reasoning
- **Optimization**: Balanced speed and capability

### Task-Specific Optimization
Different models excel in different areas:
- **Code Completions**: Fast models for real-time suggestions
- **Complex Analysis**: Reasoning models for architectural decisions
- **Domain Expertise**: Specialized models for specific technologies
- **Creative Tasks**: Models optimized for documentation and explanation

### Chat Mode Considerations
Model availability varies by chat mode:
- **Agent Mode**: Limited to models with strong tool calling support
- **Ask Mode**: Broader model selection available
- **Edit Mode**: Models optimized for code modification

## Built-in Models

### GitHub Copilot Models
- **Managed Experience**: No API key required
- **Rate Limits**: Standard limits with upgrade options
- **Quality Assurance**: Responsible AI filtering applied
- **Enterprise Support**: Business and Enterprise plans available

### Premium Models
- **Request Multipliers**: Higher resource cost for advanced models
- **Enhanced Capabilities**: Superior reasoning and analysis
- **Usage Tracking**: Monitor premium request consumption

### Model Comparison
For detailed model capabilities and comparisons, see [Choosing the right AI model for your task](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task) in GitHub Copilot documentation.

## Changing Models

### Chat Conversation Models

#### Model Picker Interface
1. **Access**: Language model picker in chat input field
2. **Selection**: Choose from available models dropdown
3. **Context**: Model applies to current and future chat messages

#### Visual Indicators
- **Premium Multiplier**: Shows cost factor for premium models
- **Availability**: Different models based on subscription tier
- **Tool Support**: Models compatible with current chat mode

### Code Completion Models

#### Changing Completion Models
1. **Method 1 - Title Bar Menu**:
   - Select Copilot menu in VS Code title bar
   - Choose "Configure Code Completions..."
   - Select "Change Completions Model..."

2. **Method 2 - Command Palette**:
   - Run `GitHub Copilot: Change Completions Model`
   - Select desired model from list

#### Model Considerations
- **Speed**: Optimize for real-time completion performance
- **Quality**: Balance accuracy with response time
- **Language Support**: Some models better for specific programming languages

## Bring Your Own Model Key

### Supported Providers
Access models directly from:
- **Anthropic**: Claude models
- **Azure**: Azure OpenAI services
- **Google**: Gemini models  
- **Groq**: High-speed inference
- **Ollama**: Local model hosting
- **OpenAI**: GPT models
- **OpenRouter**: Multiple provider access

### Benefits of Custom API Keys

#### Model Access
- **Hundreds of Models**: Beyond built-in Copilot models
- **Latest Releases**: Immediate access to new models
- **Specialized Models**: Domain-specific or experimental models

#### Control and Flexibility
- **Rate Limits**: Bypass standard restrictions
- **Local Compute**: Use own infrastructure for privacy
- **Experimentation**: Test cutting-edge models and features
- **Cost Management**: Direct control over usage and billing

### Setup Process

#### Adding a Provider
1. **Access Management**: Select "Manage Models" from model picker
2. **Alternative**: Run `GitHub Copilot: Manage Models` command
3. **Provider Selection**: Choose from supported provider list
4. **Configuration**: Enter API key and endpoint details
5. **Model Selection**: Choose specific model or select from available list

#### Provider-Specific Configuration

**OpenAI Example**:
```
API Key: sk-...
Model: gpt-4
Endpoint: https://api.openai.com/v1
```

**Ollama Example** (Local):
```
Endpoint: http://localhost:11434
Model: phi-4 (selected from available local models)
```

**Azure Example**:
```
API Key: ...
Endpoint: https://your-resource.openai.azure.com/
Deployment: your-gpt-4-deployment
```

#### Model Management
- **Update Details**: Modify API keys and endpoints via gear icon
- **Model Selection**: Choose from provider's available models
- **Local Models**: Ollama shows locally deployed models

### Usage Considerations

#### Limitations
- **Chat Only**: Custom models only affect chat experience
- **Code Completions**: Still use built-in Copilot models
- **Feature Support**: Some AI features may not work with custom models

#### Capability Differences
- **Vision Support**: Not all models support image analysis
- **Tool Calling**: Reduced functionality in agent mode
- **Response Quality**: May vary from built-in models

#### Technical Requirements
- **API Compatibility**: Models must support OpenAI-compatible APIs
- **Network Access**: Requires stable internet for cloud models
- **Local Setup**: Ollama requires local installation and model management

### Responsible AI Considerations
- **Filtering**: No guarantee of responsible AI filtering on custom models
- **Content Moderation**: User responsibility for output monitoring
- **Compliance**: Ensure model usage meets organizational policies

## Enterprise and Business Plans

### Current Limitations
- **Preview Feature**: Custom API keys not available for Business/Enterprise
- **Timeline**: Feature coming later in 2025
- **Current Options**: Built-in managed models only

### Future Capabilities
- **Enterprise Requirements**: Better understanding of organizational needs
- **Scale Considerations**: Managing custom models at organization level
- **Security**: Enhanced security and compliance features

### Workarounds
- **Built-in Models**: Use extensive selection of managed models
- **Feature Requests**: Engage with GitHub for enterprise-specific needs
- **Policy Configuration**: Enable preview features when available

## Configuration and Settings

### Model Persistence
- **Chat Sessions**: Model selection persists within sessions
- **Global Settings**: Set preferred models across VS Code
- **Context Switching**: Easy model switching for different tasks

### Performance Optimization
- **Model Caching**: Frequently used models load faster
- **Endpoint Configuration**: Optimize for geographic proximity
- **Timeout Settings**: Configure for network conditions

### Integration Settings
- **Workspace**: Model preferences per project
- **User Profile**: Personal model preferences
- **Team Standards**: Shared configuration approaches

## Best Practices

### Model Selection Strategy
- **Task Matching**: Choose models optimized for specific tasks
- **Speed vs Quality**: Balance response time with accuracy needs
- **Cost Consideration**: Monitor usage of premium models
- **Experimentation**: Test different models for different use cases

### API Key Management
- **Security**: Store API keys securely
- **Rotation**: Regular key rotation for security
- **Monitoring**: Track usage and costs
- **Team Sharing**: Secure methods for team key distribution

### Performance Optimization
- **Local Models**: Consider Ollama for privacy and speed
- **Provider Selection**: Choose based on geographic proximity
- **Model Size**: Balance capability with response time
- **Fallback Options**: Configure backup models for reliability

## Troubleshooting

### Common Issues
- **API Key Errors**: Verify key validity and permissions
- **Model Unavailability**: Check provider status and model access
- **Slow Responses**: Consider model size and network latency
- **Feature Limitations**: Understand custom model constraints

### Debugging Steps
1. **Verify Configuration**: Check API keys and endpoints
2. **Test Connectivity**: Ensure network access to providers
3. **Model Status**: Confirm model availability with provider
4. **Fallback Testing**: Try alternative models or providers

### Performance Issues
- **Network Latency**: Use geographically closer endpoints
- **Model Size**: Try smaller, faster models for quick tasks
- **Rate Limiting**: Monitor and manage API usage
- **Local Options**: Consider Ollama for consistent performance

## Future Developments

### Expanding Provider Support
- Additional model providers
- Enhanced integration capabilities
- Improved model discovery and selection

### Enterprise Features
- Organization-wide model management
- Enhanced security and compliance
- Cost management and reporting tools

### Performance Improvements
- Faster model switching
- Better caching mechanisms
- Optimized API integration

## Related Resources

### Documentation
- [Available Language Models in GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat?tool=vscode)
- [Choosing the Right AI Model](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task)
- [Premium Requests](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests#premium-requests)

### Related VS Code Features
- [Chat Modes](https://code.visualstudio.com/docs/copilot/chat/copilot-chat#_chat-mode)
- [Code Completions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions)
- [Copilot Customization](https://code.visualstudio.com/docs/copilot/copilot-customization)

### Provider Documentation
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference)
- [Google AI Studio](https://ai.google.dev/tutorials)
- [Ollama Documentation](https://ollama.ai/docs)
