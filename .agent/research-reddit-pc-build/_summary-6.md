# AI PC Build Summary 6: LLaMA.cpp Hardware Optimization

**Source:** https://github.com/ggerganov/llama.cpp

## Key Findings

### Platform Support and Optimization
- **Multi-Platform**: Supports CUDA, Metal, Vulkan, SYCL, HIP, and CPU backends
- **Quantization**: 1.5-bit to 8-bit quantization for reduced memory usage
- **Hybrid Inference**: CPU+GPU hybrid for models larger than VRAM capacity

### Performance Optimization Features
- **Hardware Acceleration**: Optimized for Apple Silicon, x86 AVX/AVX2/AVX512
- **Custom Kernels**: CUDA kernels for NVIDIA GPUs, Metal for Apple Silicon
- **Memory Efficiency**: Sophisticated memory management for large model deployment

### Deployment Options
- **Local Inference**: Designed for edge deployment with minimal dependencies
- **OpenAI Compatibility**: Server mode with REST API for easy integration
- **Model Format**: GGUF format optimized for inference efficiency

## Hardware Requirements by Model Size
- **Small Models (1-7B)**: 8GB VRAM sufficient with quantization
- **Medium Models (13-30B)**: 16-24GB VRAM recommended
- **Large Models (70B+)**: Multi-GPU or CPU+GPU hybrid inference
- **System Requirements**: Fast CPU beneficial for prompt processing and CPU inference portions
