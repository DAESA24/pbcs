# Crawl4AI Custom LLM Context
Generated on: 2025-12-03T20:27:14.986Z
Total files: 2
Estimated tokens: 9,463

---

## Docker - Full Content
Component ID: docker
Context Type: memory
Estimated tokens: 5,155

## Docker Deployment

Complete Docker deployment guide with pre-built images, API endpoints, configuration, and MCP integration.

### Quick Start with Pre-built Images

```bash
# Pull latest image
docker pull unclecode/crawl4ai:latest

# Setup LLM API keys
cat > .llm.env << EOL
OPENAI_API_KEY=sk-your-key
ANTHROPIC_API_KEY=your-anthropic-key
GROQ_API_KEY=your-groq-key
GEMINI_API_TOKEN=your-gemini-token
EOL

# Run with LLM support
docker run -d \
  -p 11235:11235 \
  --name crawl4ai \
  --env-file .llm.env \
  --shm-size=1g \
  unclecode/crawl4ai:latest

# Basic run (no LLM)
docker run -d \
  -p 11235:11235 \
  --name crawl4ai \
  --shm-size=1g \
  unclecode/crawl4ai:latest

# Check health
curl http://localhost:11235/health
```

### Docker Compose Deployment

```bash
# Clone and setup
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai
cp deploy/docker/.llm.env.example .llm.env
# Edit .llm.env with your API keys

# Run pre-built image
IMAGE=unclecode/crawl4ai:latest docker compose up -d

# Build locally
docker compose up --build -d

# Build with all features
INSTALL_TYPE=all docker compose up --build -d

# Build with GPU support
ENABLE_GPU=true docker compose up --build -d

# Stop service
docker compose down
```

### Manual Build with Multi-Architecture

```bash
# Clone repository
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai

# Build for current architecture
docker buildx build -t crawl4ai-local:latest --load .

# Build for multiple architectures
docker buildx build --platform linux/amd64,linux/arm64 \
  -t crawl4ai-local:latest --load .

# Build with specific features
docker buildx build \
  --build-arg INSTALL_TYPE=all \
  --build-arg ENABLE_GPU=false \
  -t crawl4ai-local:latest --load .

# Run custom build
docker run -d \
  -p 11235:11235 \
  --name crawl4ai-custom \
  --env-file .llm.env \
  --shm-size=1g \
  crawl4ai-local:latest
```

### Build Arguments

```bash
# Available build options
docker buildx build \
  --build-arg INSTALL_TYPE=all \     # default|all|torch|transformer
  --build-arg ENABLE_GPU=true \      # true|false
  --build-arg APP_HOME=/app \        # Install path
  --build-arg USE_LOCAL=true \       # Use local source
  --build-arg GITHUB_REPO=url \      # Git repo if USE_LOCAL=false
  --build-arg GITHUB_BRANCH=main \   # Git branch
  -t crawl4ai-custom:latest --load .
```

### Core API Endpoints

```python
# Main crawling endpoints
import requests
import json

# Basic crawl
payload = {
    "urls": ["https://example.com"],
    "browser_config": {"type": "BrowserConfig", "params": {"headless": True}},
    "crawler_config": {"type": "CrawlerRunConfig", "params": {"cache_mode": "bypass"}}
}
response = requests.post("http://localhost:11235/crawl", json=payload)

# Streaming crawl
payload["crawler_config"]["params"]["stream"] = True
response = requests.post("http://localhost:11235/crawl/stream", json=payload)

# Health check
response = requests.get("http://localhost:11235/health")

# API schema
response = requests.get("http://localhost:11235/schema")

# Metrics (Prometheus format)
response = requests.get("http://localhost:11235/metrics")
```

### Specialized Endpoints

```python
# HTML extraction (preprocessed for schema)
response = requests.post("http://localhost:11235/html", 
    json={"url": "https://example.com"})

# Screenshot capture
response = requests.post("http://localhost:11235/screenshot", json={
    "url": "https://example.com",
    "screenshot_wait_for": 2,
    "output_path": "/path/to/save/screenshot.png"
})

# PDF generation
response = requests.post("http://localhost:11235/pdf", json={
    "url": "https://example.com",
    "output_path": "/path/to/save/document.pdf"
})

# JavaScript execution
response = requests.post("http://localhost:11235/execute_js", json={
    "url": "https://example.com",
    "scripts": [
        "return document.title",
        "return Array.from(document.querySelectorAll('a')).map(a => a.href)"
    ]
})

# Markdown generation
response = requests.post("http://localhost:11235/md", json={
    "url": "https://example.com",
    "f": "fit",  # raw|fit|bm25|llm
    "q": "extract main content",  # query for filtering
    "c": "0"  # cache: 0=bypass, 1=use
})

# LLM Q&A
response = requests.get("http://localhost:11235/llm/https://example.com?q=What is this page about?")

# Library context (for AI assistants)
response = requests.get("http://localhost:11235/ask", params={
    "context_type": "all",  # code|doc|all
    "query": "how to use extraction strategies",
    "score_ratio": 0.5,
    "max_results": 20
})
```

### Python SDK Usage

```python
import asyncio
from crawl4ai.docker_client import Crawl4aiDockerClient
from crawl4ai import BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    async with Crawl4aiDockerClient(base_url="http://localhost:11235") as client:
        # Non-streaming crawl
        results = await client.crawl(
            ["https://example.com"],
            browser_config=BrowserConfig(headless=True),
            crawler_config=CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        )
        
        for result in results:
            print(f"URL: {result.url}, Success: {result.success}")
            print(f"Content length: {len(result.markdown)}")
        
        # Streaming crawl
        stream_config = CrawlerRunConfig(stream=True, cache_mode=CacheMode.BYPASS)
        async for result in await client.crawl(
            ["https://example.com", "https://python.org"],
            browser_config=BrowserConfig(headless=True),
            crawler_config=stream_config
        ):
            print(f"Streamed: {result.url} - {result.success}")
        
        # Get API schema
        schema = await client.get_schema()
        print(f"Schema available: {bool(schema)}")

asyncio.run(main())
```

### Advanced API Configuration

```python
# Complex extraction with LLM
payload = {
    "urls": ["https://example.com"],
    "browser_config": {
        "type": "BrowserConfig",
        "params": {
            "headless": True,
            "viewport": {"type": "dict", "value": {"width": 1200, "height": 800}}
        }
    },
    "crawler_config": {
        "type": "CrawlerRunConfig",
        "params": {
            "extraction_strategy": {
                "type": "LLMExtractionStrategy",
                "params": {
                    "llm_config": {
                        "type": "LLMConfig",
                        "params": {
                            "provider": "openai/gpt-4o-mini",
                            "api_token": "env:OPENAI_API_KEY"
                        }
                    },
                    "schema": {
                        "type": "dict",
                        "value": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "content": {"type": "string"}
                            }
                        }
                    },
                    "instruction": "Extract title and main content"
                }
            },
            "markdown_generator": {
                "type": "DefaultMarkdownGenerator",
                "params": {
                    "content_filter": {
                        "type": "PruningContentFilter",
                        "params": {"threshold": 0.6}
                    }
                }
            }
        }
    }
}

response = requests.post("http://localhost:11235/crawl", json=payload)
```

### CSS Extraction Strategy

```python
# CSS-based structured extraction
schema = {
    "name": "ProductList",
    "baseSelector": ".product",
    "fields": [
        {"name": "title", "selector": "h2", "type": "text"},
        {"name": "price", "selector": ".price", "type": "text"},
        {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
}

payload = {
    "urls": ["https://example-shop.com"],
    "browser_config": {"type": "BrowserConfig", "params": {"headless": True}},
    "crawler_config": {
        "type": "CrawlerRunConfig",
        "params": {
            "extraction_strategy": {
                "type": "JsonCssExtractionStrategy",
                "params": {
                    "schema": {"type": "dict", "value": schema}
                }
            }
        }
    }
}

response = requests.post("http://localhost:11235/crawl", json=payload)
data = response.json()
extracted = json.loads(data["results"][0]["extracted_content"])
```

### MCP (Model Context Protocol) Integration

```bash
# Add Crawl4AI as MCP provider to Claude Code
claude mcp add --transport sse c4ai-sse http://localhost:11235/mcp/sse

# List MCP providers
claude mcp list

# Test MCP connection
python tests/mcp/test_mcp_socket.py

# Available MCP endpoints
# SSE: http://localhost:11235/mcp/sse
# WebSocket: ws://localhost:11235/mcp/ws
# Schema: http://localhost:11235/mcp/schema
```

Available MCP tools:
- `md` - Generate markdown from web content
- `html` - Extract preprocessed HTML  
- `screenshot` - Capture webpage screenshots
- `pdf` - Generate PDF documents
- `execute_js` - Run JavaScript on web pages
- `crawl` - Perform multi-URL crawling
- `ask` - Query Crawl4AI library context

### Configuration Management

```yaml
# config.yml structure
app:
  title: "Crawl4AI API"
  version: "1.0.0"
  host: "0.0.0.0"
  port: 11235
  timeout_keep_alive: 300

llm:
  provider: "openai/gpt-4o-mini"
  api_key_env: "OPENAI_API_KEY"

security:
  enabled: false
  jwt_enabled: false
  trusted_hosts: ["*"]

crawler:
  memory_threshold_percent: 95.0
  rate_limiter:
    base_delay: [1.0, 2.0]
  timeouts:
    stream_init: 30.0
    batch_process: 300.0
  pool:
    max_pages: 40
    idle_ttl_sec: 1800

rate_limiting:
  enabled: true
  default_limit: "1000/minute"
  storage_uri: "memory://"

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### Custom Configuration Deployment

```bash
# Method 1: Mount custom config
docker run -d -p 11235:11235 \
  --name crawl4ai-custom \
  --env-file .llm.env \
  --shm-size=1g \
  -v $(pwd)/my-config.yml:/app/config.yml \
  unclecode/crawl4ai:latest

# Method 2: Build with custom config
# Edit deploy/docker/config.yml then build
docker buildx build -t crawl4ai-custom:latest --load .
```

### Monitoring and Health Checks

```bash
# Health endpoint
curl http://localhost:11235/health

# Prometheus metrics
curl http://localhost:11235/metrics

# Configuration validation
curl -X POST http://localhost:11235/config/dump \
  -H "Content-Type: application/json" \
  -d '{"code": "CrawlerRunConfig(cache_mode=\"BYPASS\", screenshot=True)"}'
```

### Playground Interface

Access the interactive playground at `http://localhost:11235/playground` for:
- Testing configurations with visual interface
- Generating JSON payloads for REST API
- Converting Python config to JSON format
- Testing crawl operations directly in browser

### Async Job Processing

```python
# Submit job for async processing
import time

# Submit crawl job
response = requests.post("http://localhost:11235/crawl/job", json=payload)
task_id = response.json()["task_id"]

# Poll for completion
while True:
    result = requests.get(f"http://localhost:11235/crawl/job/{task_id}")
    status = result.json()
    
    if status["status"] in ["COMPLETED", "FAILED"]:
        break
    time.sleep(1.5)

print("Final result:", status)
```

### Production Deployment

```bash
# Production-ready deployment
docker run -d \
  --name crawl4ai-prod \
  --restart unless-stopped \
  -p 11235:11235 \
  --env-file .llm.env \
  --shm-size=2g \
  --memory=8g \
  --cpus=4 \
  -v /path/to/custom-config.yml:/app/config.yml \
  unclecode/crawl4ai:latest

# With Docker Compose for production
version: '3.8'
services:
  crawl4ai:
    image: unclecode/crawl4ai:latest
    ports:
      - "11235:11235"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./config.yml:/app/config.yml
    shm_size: 2g
    deploy:
      resources:
        limits:
          memory: 8G
          cpus: '4'
    restart: unless-stopped
```

### Configuration Validation and JSON Structure

```python
# Method 1: Create config objects and dump to see expected JSON structure
from crawl4ai import BrowserConfig, CrawlerRunConfig, LLMConfig, CacheMode
from crawl4ai import JsonCssExtractionStrategy, LLMExtractionStrategy
import json

# Create browser config and see JSON structure
browser_config = BrowserConfig(
    headless=True,
    viewport_width=1280,
    viewport_height=720,
    proxy="http://user:pass@proxy:8080"
)

# Get JSON structure
browser_json = browser_config.dump()
print("BrowserConfig JSON structure:")
print(json.dumps(browser_json, indent=2))

# Create crawler config with extraction strategy
schema = {
    "name": "Articles",
    "baseSelector": ".article",
    "fields": [
        {"name": "title", "selector": "h2", "type": "text"},
        {"name": "content", "selector": ".content", "type": "html"}
    ]
}

crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    screenshot=True,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    js_code=["window.scrollTo(0, document.body.scrollHeight);"],
    wait_for="css:.loaded"
)

crawler_json = crawler_config.dump()
print("\nCrawlerRunConfig JSON structure:")
print(json.dumps(crawler_json, indent=2))
```

### Reverse Validation - JSON to Objects

```python
# Method 2: Load JSON back to config objects for validation
from crawl4ai.async_configs import from_serializable_dict

# Test JSON structure by converting back to objects
test_browser_json = {
    "type": "BrowserConfig",
    "params": {
        "headless": True,
        "viewport_width": 1280,
        "proxy": "http://user:pass@proxy:8080"
    }
}

try:
    # Convert JSON back to object
    restored_browser = from_serializable_dict(test_browser_json)
    print(f"✅ Valid BrowserConfig: {type(restored_browser)}")
    print(f"Headless: {restored_browser.headless}")
    print(f"Proxy: {restored_browser.proxy}")
except Exception as e:
    print(f"❌ Invalid BrowserConfig JSON: {e}")

# Test complex crawler config JSON
test_crawler_json = {
    "type": "CrawlerRunConfig", 
    "params": {
        "cache_mode": "bypass",
        "screenshot": True,
        "extraction_strategy": {
            "type": "JsonCssExtractionStrategy",
            "params": {
                "schema": {
                    "type": "dict",
                    "value": {
                        "name": "Products",
                        "baseSelector": ".product",
                        "fields": [
                            {"name": "title", "selector": "h3", "type": "text"}
                        ]
                    }
                }
            }
        }
    }
}

try:
    restored_crawler = from_serializable_dict(test_crawler_json)
    print(f"✅ Valid CrawlerRunConfig: {type(restored_crawler)}")
    print(f"Cache mode: {restored_crawler.cache_mode}")
    print(f"Has extraction strategy: {restored_crawler.extraction_strategy is not None}")
except Exception as e:
    print(f"❌ Invalid CrawlerRunConfig JSON: {e}")
```

### Using Server's /config/dump Endpoint for Validation

```python
import requests

# Method 3: Use server endpoint to validate configuration syntax
def validate_config_with_server(config_code: str) -> dict:
    """Validate configuration using server's /config/dump endpoint"""
    response = requests.post(
        "http://localhost:11235/config/dump",
        json={"code": config_code}
    )
    
    if response.status_code == 200:
        print("✅ Valid configuration syntax")
        return response.json()
    else:
        print(f"❌ Invalid configuration: {response.status_code}")
        print(response.json())
        return None

# Test valid configuration
valid_config = """
CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    screenshot=True,
    js_code=["window.scrollTo(0, document.body.scrollHeight);"],
    wait_for="css:.content-loaded"
)
"""

result = validate_config_with_server(valid_config)
if result:
    print("Generated JSON structure:")
    print(json.dumps(result, indent=2))

# Test invalid configuration (should fail)
invalid_config = """
CrawlerRunConfig(
    cache_mode="invalid_mode",
    screenshot=True,
    js_code=some_function()  # This will fail
)
"""

validate_config_with_server(invalid_config)
```

### Configuration Builder Helper

```python
def build_and_validate_request(urls, browser_params=None, crawler_params=None):
    """Helper to build and validate complete request payload"""
    
    # Create configurations
    browser_config = BrowserConfig(**(browser_params or {}))
    crawler_config = CrawlerRunConfig(**(crawler_params or {}))
    
    # Build complete request payload
    payload = {
        "urls": urls if isinstance(urls, list) else [urls],
        "browser_config": browser_config.dump(),
        "crawler_config": crawler_config.dump()
    }
    
    print("✅ Complete request payload:")
    print(json.dumps(payload, indent=2))
    
    # Validate by attempting to reconstruct
    try:
        test_browser = from_serializable_dict(payload["browser_config"])
        test_crawler = from_serializable_dict(payload["crawler_config"])
        print("✅ Payload validation successful")
        return payload
    except Exception as e:
        print(f"❌ Payload validation failed: {e}")
        return None

# Example usage
payload = build_and_validate_request(
    urls=["https://example.com"],
    browser_params={"headless": True, "viewport_width": 1280},
    crawler_params={
        "cache_mode": CacheMode.BYPASS,
        "screenshot": True,
        "word_count_threshold": 10
    }
)

if payload:
    # Send to server
    response = requests.post("http://localhost:11235/crawl", json=payload)
    print(f"Server response: {response.status_code}")
```

### Common JSON Structure Patterns

```python
# Pattern 1: Simple primitive values
simple_config = {
    "type": "CrawlerRunConfig",
    "params": {
        "cache_mode": "bypass",  # String enum value
        "screenshot": True,      # Boolean
        "page_timeout": 60000   # Integer
    }
}

# Pattern 2: Nested objects
nested_config = {
    "type": "CrawlerRunConfig", 
    "params": {
        "extraction_strategy": {
            "type": "LLMExtractionStrategy",
            "params": {
                "llm_config": {
                    "type": "LLMConfig",
                    "params": {
                        "provider": "openai/gpt-4o-mini",
                        "api_token": "env:OPENAI_API_KEY"
                    }
                },
                "instruction": "Extract main content"
            }
        }
    }
}

# Pattern 3: Dictionary values (must use type: dict wrapper)
dict_config = {
    "type": "CrawlerRunConfig",
    "params": {
        "extraction_strategy": {
            "type": "JsonCssExtractionStrategy", 
            "params": {
                "schema": {
                    "type": "dict",  # Required wrapper
                    "value": {       # Actual dictionary content
                        "name": "Products",
                        "baseSelector": ".product",
                        "fields": [
                            {"name": "title", "selector": "h2", "type": "text"}
                        ]
                    }
                }
            }
        }
    }
}

# Pattern 4: Lists and arrays
list_config = {
    "type": "CrawlerRunConfig",
    "params": {
        "js_code": [  # Lists are handled directly
            "window.scrollTo(0, document.body.scrollHeight);",
            "document.querySelector('.load-more')?.click();"
        ],
        "excluded_tags": ["script", "style", "nav"]
    }
}
```

### Troubleshooting Common JSON Errors

```python
def diagnose_json_errors():
    """Common JSON structure errors and fixes"""
    
    # ❌ WRONG: Missing type wrapper for objects
    wrong_config = {
        "browser_config": {
            "headless": True  # Missing type wrapper
        }
    }
    
    # ✅ CORRECT: Proper type wrapper
    correct_config = {
        "browser_config": {
            "type": "BrowserConfig",
            "params": {
                "headless": True
            }
        }
    }
    
    # ❌ WRONG: Dictionary without type: dict wrapper  
    wrong_dict = {
        "schema": {
            "name": "Products"  # Raw dict, should be wrapped
        }
    }
    
    # ✅ CORRECT: Dictionary with proper wrapper
    correct_dict = {
        "schema": {
            "type": "dict",
            "value": {
                "name": "Products"
            }
        }
    }
    
    # ❌ WRONG: Invalid enum string
    wrong_enum = {
        "cache_mode": "DISABLED"  # Wrong case/value
    }
    
    # ✅ CORRECT: Valid enum string  
    correct_enum = {
        "cache_mode": "bypass"  # or "enabled", "disabled", etc.
    }
    
    print("Common error patterns documented above")

# Validate your JSON structure before sending
def pre_flight_check(payload):
    """Run checks before sending to server"""
    required_keys = ["urls", "browser_config", "crawler_config"]
    
    for key in required_keys:
        if key not in payload:
            print(f"❌ Missing required key: {key}")
            return False
    
    # Check type wrappers
    for config_key in ["browser_config", "crawler_config"]:
        config = payload[config_key]
        if not isinstance(config, dict) or "type" not in config:
            print(f"❌ {config_key} missing type wrapper")
            return False
        if "params" not in config:
            print(f"❌ {config_key} missing params")
            return False
    
    print("✅ Pre-flight check passed")
    return True

# Example usage
payload = {
    "urls": ["https://example.com"],
    "browser_config": {"type": "BrowserConfig", "params": {"headless": True}},
    "crawler_config": {"type": "CrawlerRunConfig", "params": {"cache_mode": "bypass"}}
}

if pre_flight_check(payload):
    # Safe to send to server
    pass
```

**📖 Learn more:** [Complete Docker Guide](https://docs.crawl4ai.com/core/docker-deployment/), [API Reference](https://docs.crawl4ai.com/api/), [MCP Integration](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support), [Configuration Options](https://docs.crawl4ai.com/core/docker-deployment/#server-configuration)

---


## Docker - Diagrams & Workflows
Component ID: docker
Context Type: reasoning
Estimated tokens: 4,308

## Docker Deployment Architecture and Workflows

Visual representations of Crawl4AI Docker deployment, API architecture, configuration management, and service interactions.

### Docker Deployment Decision Flow

```mermaid
flowchart TD
    A[Start Docker Deployment] --> B{Deployment Type?}
    
    B -->|Quick Start| C[Pre-built Image]
    B -->|Development| D[Docker Compose]
    B -->|Custom Build| E[Manual Build]
    B -->|Production| F[Production Setup]
    
    C --> C1[docker pull unclecode/crawl4ai]
    C1 --> C2{Need LLM Support?}
    C2 -->|Yes| C3[Setup .llm.env]
    C2 -->|No| C4[Basic run]
    C3 --> C5[docker run with --env-file]
    C4 --> C6[docker run basic]
    
    D --> D1[git clone repository]
    D1 --> D2[cp .llm.env.example .llm.env]
    D2 --> D3{Build Type?}
    D3 -->|Pre-built| D4[IMAGE=latest docker compose up]
    D3 -->|Local Build| D5[docker compose up --build]
    D3 -->|All Features| D6[INSTALL_TYPE=all docker compose up]
    
    E --> E1[docker buildx build]
    E1 --> E2{Architecture?}
    E2 -->|Single| E3[--platform linux/amd64]
    E2 -->|Multi| E4[--platform linux/amd64,linux/arm64]
    E3 --> E5[Build complete]
    E4 --> E5
    
    F --> F1[Production configuration]
    F1 --> F2[Custom config.yml]
    F2 --> F3[Resource limits]
    F3 --> F4[Health monitoring]
    F4 --> F5[Production ready]
    
    C5 --> G[Service running on :11235]
    C6 --> G
    D4 --> G
    D5 --> G
    D6 --> G
    E5 --> H[docker run custom image]
    H --> G
    F5 --> I[Production deployment]
    
    G --> J[Access playground at /playground]
    G --> K[Health check at /health]
    I --> L[Production monitoring]
    
    style A fill:#e1f5fe
    style G fill:#c8e6c9
    style I fill:#c8e6c9
    style J fill:#fff3e0
    style K fill:#fff3e0
    style L fill:#e8f5e8
```

### Docker Container Architecture

```mermaid
graph TB
    subgraph "Host Environment"
        A[Docker Engine] --> B[Crawl4AI Container]
        C[.llm.env] --> B
        D[Custom config.yml] --> B
        E[Port 11235] --> B
        F[Shared Memory 1GB+] --> B
    end
    
    subgraph "Container Services"
        B --> G[FastAPI Server :8020]
        B --> H[Gunicorn WSGI]
        B --> I[Supervisord Process Manager]
        B --> J[Redis Cache :6379]
        
        G --> K[REST API Endpoints]
        G --> L[WebSocket Connections]
        G --> M[MCP Protocol]
        
        H --> N[Worker Processes]
        I --> O[Service Monitoring]
        J --> P[Request Caching]
    end
    
    subgraph "Browser Management"
        B --> Q[Playwright Framework]
        Q --> R[Chromium Browser]
        Q --> S[Firefox Browser]
        Q --> T[WebKit Browser]
        
        R --> U[Browser Pool]
        S --> U
        T --> U
        
        U --> V[Page Sessions]
        U --> W[Context Management]
    end
    
    subgraph "External Services"
        X[OpenAI API] -.-> K
        Y[Anthropic Claude] -.-> K
        Z[Local Ollama] -.-> K
        AA[Groq API] -.-> K
        BB[Google Gemini] -.-> K
    end
    
    subgraph "Client Interactions"
        CC[Python SDK] --> K
        DD[REST API Calls] --> K
        EE[MCP Clients] --> M
        FF[Web Browser] --> G
        GG[Monitoring Tools] --> K
    end
    
    style B fill:#e3f2fd
    style G fill:#f3e5f5
    style Q fill:#e8f5e8
    style K fill:#fff3e0
```

### API Endpoints Architecture

```mermaid
graph LR
    subgraph "Core Endpoints"
        A[/crawl] --> A1[Single URL crawl]
        A2[/crawl/stream] --> A3[Streaming multi-URL]
        A4[/crawl/job] --> A5[Async job submission]
        A6[/crawl/job/{id}] --> A7[Job status check]
    end
    
    subgraph "Specialized Endpoints"
        B[/html] --> B1[Preprocessed HTML]
        B2[/screenshot] --> B3[PNG capture]
        B4[/pdf] --> B5[PDF generation]
        B6[/execute_js] --> B7[JavaScript execution]
        B8[/md] --> B9[Markdown extraction]
    end
    
    subgraph "Utility Endpoints"
        C[/health] --> C1[Service status]
        C2[/metrics] --> C3[Prometheus metrics]
        C4[/schema] --> C5[API documentation]
        C6[/playground] --> C7[Interactive testing]
    end
    
    subgraph "LLM Integration"
        D[/llm/{url}] --> D1[Q&A over URL]
        D2[/ask] --> D3[Library context search]
        D4[/config/dump] --> D5[Config validation]
    end
    
    subgraph "MCP Protocol"
        E[/mcp/sse] --> E1[Server-Sent Events]
        E2[/mcp/ws] --> E3[WebSocket connection]
        E4[/mcp/schema] --> E5[MCP tool definitions]
    end
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
```

### Request Processing Flow

```mermaid
sequenceDiagram
    participant Client
    participant FastAPI
    participant RequestValidator
    participant BrowserPool
    participant Playwright
    participant ExtractionEngine
    participant LLMProvider
    
    Client->>FastAPI: POST /crawl with config
    FastAPI->>RequestValidator: Validate JSON structure
    
    alt Valid Request
        RequestValidator-->>FastAPI: ✓ Validated
        FastAPI->>BrowserPool: Request browser instance
        BrowserPool->>Playwright: Launch browser/reuse session
        Playwright-->>BrowserPool: Browser ready
        BrowserPool-->>FastAPI: Browser allocated
        
        FastAPI->>Playwright: Navigate to URL
        Playwright->>Playwright: Execute JS, wait conditions
        Playwright-->>FastAPI: Page content ready
        
        FastAPI->>ExtractionEngine: Process content
        
        alt LLM Extraction
            ExtractionEngine->>LLMProvider: Send content + schema
            LLMProvider-->>ExtractionEngine: Structured data
        else CSS Extraction
            ExtractionEngine->>ExtractionEngine: Apply CSS selectors
        end
        
        ExtractionEngine-->>FastAPI: Extraction complete
        FastAPI->>BrowserPool: Release browser
        FastAPI-->>Client: CrawlResult response
        
    else Invalid Request
        RequestValidator-->>FastAPI: ✗ Validation error
        FastAPI-->>Client: 400 Bad Request
    end
```

### Configuration Management Flow

```mermaid
stateDiagram-v2
    [*] --> ConfigLoading
    
    ConfigLoading --> DefaultConfig: Load default config.yml
    ConfigLoading --> CustomConfig: Custom config mounted
    ConfigLoading --> EnvOverrides: Environment variables
    
    DefaultConfig --> ConfigMerging
    CustomConfig --> ConfigMerging
    EnvOverrides --> ConfigMerging
    
    ConfigMerging --> ConfigValidation
    
    ConfigValidation --> Valid: Schema validation passes
    ConfigValidation --> Invalid: Validation errors
    
    Invalid --> ConfigError: Log errors and exit
    ConfigError --> [*]
    
    Valid --> ServiceInitialization
    ServiceInitialization --> FastAPISetup
    ServiceInitialization --> BrowserPoolInit
    ServiceInitialization --> CacheSetup
    
    FastAPISetup --> Running
    BrowserPoolInit --> Running
    CacheSetup --> Running
    
    Running --> ConfigReload: Config change detected
    ConfigReload --> ConfigValidation
    
    Running --> [*]: Service shutdown
    
    note right of ConfigMerging : Priority: ENV > Custom > Default
    note right of ServiceInitialization : All services must initialize successfully
```

### Multi-Architecture Build Process

```mermaid
flowchart TD
    A[Developer Push] --> B[GitHub Repository]
    
    B --> C[Docker Buildx]
    C --> D{Build Strategy}
    
    D -->|Multi-arch| E[Parallel Builds]
    D -->|Single-arch| F[Platform-specific Build]
    
    E --> G[AMD64 Build]
    E --> H[ARM64 Build]
    
    F --> I[Target Platform Build]
    
    subgraph "AMD64 Build Process"
        G --> G1[Ubuntu base image]
        G1 --> G2[Python 3.11 install]
        G2 --> G3[System dependencies]
        G3 --> G4[Crawl4AI installation]
        G4 --> G5[Playwright setup]
        G5 --> G6[FastAPI configuration]
        G6 --> G7[AMD64 image ready]
    end
    
    subgraph "ARM64 Build Process"
        H --> H1[Ubuntu ARM64 base]
        H1 --> H2[Python 3.11 install]
        H2 --> H3[ARM-specific deps]
        H3 --> H4[Crawl4AI installation]
        H4 --> H5[Playwright setup]
        H5 --> H6[FastAPI configuration]
        H6 --> H7[ARM64 image ready]
    end
    
    subgraph "Single Architecture"
        I --> I1[Base image selection]
        I1 --> I2[Platform dependencies]
        I2 --> I3[Application setup]
        I3 --> I4[Platform image ready]
    end
    
    G7 --> J[Multi-arch Manifest]
    H7 --> J
    I4 --> K[Platform Image]
    
    J --> L[Docker Hub Registry]
    K --> L
    
    L --> M[Pull Request Auto-selects Architecture]
    
    style A fill:#e1f5fe
    style J fill:#c8e6c9
    style K fill:#c8e6c9
    style L fill:#f3e5f5
    style M fill:#e8f5e8
```

### MCP Integration Architecture

```mermaid
graph TB
    subgraph "MCP Client Applications"
        A[Claude Code] --> B[MCP Protocol]
        C[Cursor IDE] --> B
        D[Windsurf] --> B
        E[Custom MCP Client] --> B
    end
    
    subgraph "Crawl4AI MCP Server"
        B --> F[MCP Endpoint Router]
        F --> G[SSE Transport /mcp/sse]
        F --> H[WebSocket Transport /mcp/ws]
        F --> I[Schema Endpoint /mcp/schema]
        
        G --> J[MCP Tool Handler]
        H --> J
        
        J --> K[Tool: md]
        J --> L[Tool: html]
        J --> M[Tool: screenshot]
        J --> N[Tool: pdf]
        J --> O[Tool: execute_js]
        J --> P[Tool: crawl]
        J --> Q[Tool: ask]
    end
    
    subgraph "Crawl4AI Core Services"
        K --> R[Markdown Generator]
        L --> S[HTML Preprocessor]
        M --> T[Screenshot Service]
        N --> U[PDF Generator]
        O --> V[JavaScript Executor]
        P --> W[Batch Crawler]
        Q --> X[Context Search]
        
        R --> Y[Browser Pool]
        S --> Y
        T --> Y
        U --> Y
        V --> Y
        W --> Y
        X --> Z[Knowledge Base]
    end
    
    subgraph "External Resources"
        Y --> AA[Playwright Browsers]
        Z --> BB[Library Documentation]
        Z --> CC[Code Examples]
        AA --> DD[Web Pages]
    end
    
    style B fill:#e3f2fd
    style J fill:#f3e5f5
    style Y fill:#e8f5e8
    style Z fill:#fff3e0
```

### API Request/Response Flow Patterns

```mermaid
sequenceDiagram
    participant Client
    participant LoadBalancer
    participant FastAPI
    participant ConfigValidator
    participant BrowserManager
    participant CrawlEngine
    participant ResponseBuilder
    
    Note over Client,ResponseBuilder: Basic Crawl Request
    
    Client->>LoadBalancer: POST /crawl
    LoadBalancer->>FastAPI: Route request
    
    FastAPI->>ConfigValidator: Validate browser_config
    ConfigValidator-->>FastAPI: ✓ Valid BrowserConfig
    
    FastAPI->>ConfigValidator: Validate crawler_config
    ConfigValidator-->>FastAPI: ✓ Valid CrawlerRunConfig
    
    FastAPI->>BrowserManager: Allocate browser
    BrowserManager-->>FastAPI: Browser instance
    
    FastAPI->>CrawlEngine: Execute crawl
    
    Note over CrawlEngine: Page processing
    CrawlEngine->>CrawlEngine: Navigate & wait
    CrawlEngine->>CrawlEngine: Extract content
    CrawlEngine->>CrawlEngine: Apply strategies
    
    CrawlEngine-->>FastAPI: CrawlResult
    
    FastAPI->>ResponseBuilder: Format response
    ResponseBuilder-->>FastAPI: JSON response
    
    FastAPI->>BrowserManager: Release browser
    FastAPI-->>LoadBalancer: Response ready
    LoadBalancer-->>Client: 200 OK + CrawlResult
    
    Note over Client,ResponseBuilder: Streaming Request
    
    Client->>FastAPI: POST /crawl/stream
    FastAPI-->>Client: 200 OK (stream start)
    
    loop For each URL
        FastAPI->>CrawlEngine: Process URL
        CrawlEngine-->>FastAPI: Result ready
        FastAPI-->>Client: NDJSON line
    end
    
    FastAPI-->>Client: Stream completed
```

### Configuration Validation Workflow

```mermaid
flowchart TD
    A[Client Request] --> B[JSON Payload]
    B --> C{Pre-validation}
    
    C -->|✓ Valid JSON| D[Extract Configurations]
    C -->|✗ Invalid JSON| E[Return 400 Bad Request]
    
    D --> F[BrowserConfig Validation]
    D --> G[CrawlerRunConfig Validation]
    
    F --> H{BrowserConfig Valid?}
    G --> I{CrawlerRunConfig Valid?}
    
    H -->|✓ Valid| J[Browser Setup]
    H -->|✗ Invalid| K[Log Browser Config Errors]
    
    I -->|✓ Valid| L[Crawler Setup]
    I -->|✗ Invalid| M[Log Crawler Config Errors]
    
    K --> N[Collect All Errors]
    M --> N
    N --> O[Return 422 Validation Error]
    
    J --> P{Both Configs Valid?}
    L --> P
    
    P -->|✓ Yes| Q[Proceed to Crawling]
    P -->|✗ No| O
    
    Q --> R[Execute Crawl Pipeline]
    R --> S[Return CrawlResult]
    
    E --> T[Client Error Response]
    O --> T
    S --> U[Client Success Response]
    
    style A fill:#e1f5fe
    style Q fill:#c8e6c9
    style S fill:#c8e6c9
    style U fill:#c8e6c9
    style E fill:#ffcdd2
    style O fill:#ffcdd2
    style T fill:#ffcdd2
```

### Production Deployment Architecture

```mermaid
graph TB
    subgraph "Load Balancer Layer"
        A[NGINX/HAProxy] --> B[Health Check]
        A --> C[Request Routing]
        A --> D[SSL Termination]
    end
    
    subgraph "Application Layer"
        C --> E[Crawl4AI Instance 1]
        C --> F[Crawl4AI Instance 2]
        C --> G[Crawl4AI Instance N]
        
        E --> H[FastAPI Server]
        F --> I[FastAPI Server]
        G --> J[FastAPI Server]
        
        H --> K[Browser Pool 1]
        I --> L[Browser Pool 2]
        J --> M[Browser Pool N]
    end
    
    subgraph "Shared Services"
        N[Redis Cluster] --> E
        N --> F
        N --> G
        
        O[Monitoring Stack] --> P[Prometheus]
        O --> Q[Grafana]
        O --> R[AlertManager]
        
        P --> E
        P --> F
        P --> G
    end
    
    subgraph "External Dependencies"
        S[OpenAI API] -.-> H
        T[Anthropic API] -.-> I
        U[Local LLM Cluster] -.-> J
    end
    
    subgraph "Persistent Storage"
        V[Configuration Volume] --> E
        V --> F
        V --> G
        
        W[Cache Volume] --> N
        X[Logs Volume] --> O
    end
    
    style A fill:#e3f2fd
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style G fill:#f3e5f5
    style N fill:#e8f5e8
    style O fill:#fff3e0
```

### Docker Resource Management

```mermaid
graph TD
    subgraph "Resource Allocation"
        A[Host Resources] --> B[CPU Cores]
        A --> C[Memory GB]
        A --> D[Disk Space]
        A --> E[Network Bandwidth]
        
        B --> F[Container Limits]
        C --> F
        D --> F
        E --> F
    end
    
    subgraph "Container Configuration"
        F --> G[--cpus=4]
        F --> H[--memory=8g]
        F --> I[--shm-size=2g]
        F --> J[Volume Mounts]
        
        G --> K[Browser Processes]
        H --> L[Browser Memory]
        I --> M[Shared Memory for Browsers]
        J --> N[Config & Cache Storage]
    end
    
    subgraph "Monitoring & Scaling"
        O[Resource Monitor] --> P[CPU Usage %]
        O --> Q[Memory Usage %]
        O --> R[Request Queue Length]
        
        P --> S{CPU > 80%?}
        Q --> T{Memory > 90%?}
        R --> U{Queue > 100?}
        
        S -->|Yes| V[Scale Up]
        T -->|Yes| V
        U -->|Yes| V
        
        V --> W[Add Container Instance]
        W --> X[Update Load Balancer]
    end
    
    subgraph "Performance Optimization"
        Y[Browser Pool Tuning] --> Z[Max Pages: 40]
        Y --> AA[Idle TTL: 30min]
        Y --> BB[Concurrency Limits]
        
        Z --> CC[Memory Efficiency]
        AA --> DD[Resource Cleanup]
        BB --> EE[Throughput Control]
    end
    
    style A fill:#e1f5fe
    style F fill:#f3e5f5
    style O fill:#e8f5e8
    style Y fill:#fff3e0
```

**📖 Learn more:** [Docker Deployment Guide](https://docs.crawl4ai.com/core/docker-deployment/), [API Reference](https://docs.crawl4ai.com/api/), [MCP Integration](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support), [Production Configuration](https://docs.crawl4ai.com/core/docker-deployment/#production-deployment)

---

