---
title: manager-pattern-multi-agent-systems
type: pattern
tags: []
lang: en
confidence: 100
---

# manager-pattern-multi-agent-systems


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```python
class BaseManager:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        self.db = JSONDatabase(base_path)  # JSON operations
        self.file_ops = FileOps(base_path)  # Atomic writes

    def list(self, filters: Optional[Dict] = None) -> List[Model]:
        """List all items, optionally filtered"""
        pass

    def get(self, id: str) -> Optional[Model]:
        """Get single item by ID"""
        pass

    def create(self, data: Dict[str, Any]) -> Model:
        """Create new item with atomic write + backup"""
        pass

    def update(self, id: str, updates: Dict[str, Any]) -> Model:
        """Update existing item with atomic write + backup"""
        pass

    def delete(self, id: str) -> bool:
        """Delete item (optional)"""
        pass
```


#### Example



**Code:**
```python
@dataclass
class Model:
    field1: str
    field2: int
    # ... fields

    @classmethod
    def from_dict(cls, data: dict) -> 'Model':
        """Deserialize from JSON"""
        return cls(**data)

    def to_dict(self) -> dict:
        """Serialize to JSON"""
        return asdict(self)
```


#### Example



**Code:**
```python
class FileOps:
    """Atomic writes with automatic backups"""
    def write_json_atomic(self, path: Path, data: dict):
        temp = path.with_suffix('.tmp')
        temp.write_text(json.dumps(data, indent=2))
        if path.exists():
            shutil.copy(path, path.with_suffix('.backup'))
        temp.rename(path)  # Atomic!

class JSONDatabase:
    """Read-only JSON operations with caching"""
    def read(self, path: Path) -> dict:
        return json.loads(path.read_text())
```


#### Example



**Code:**
```python
# evolving_core/managers/base_manager.py
class BaseManager:
    """Base class für alle Managers"""
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        self.db = JSONDatabase(base_path)
        self.file_ops = FileOps(base_path)
```


#### Example



**Code:**
```python
# evolving_core/managers/agent_manager.py
class AgentManager(BaseManager):
    def __init__(self, base_path: Path):
        super().__init__(base_path)
        self.agents_dir = base_path / ".claude" / "agents"
        self._agents_cache = None  # Lazy loading

    def list(self, filter_by_type: Optional[str] = None) -> List[Agent]:
        """List all agents, optionally filtered by type"""
        if self._agents_cache is None:
            self._load_agents()

        agents = list(self._agents_cache.values())
        if filter_by_type:
            agents = [a for a in agents if a.agent_type == filter_by_type]
        return agents

    def get(self, agent_name: str) -> Optional[Agent]:
        """Get agent by name (fuzzy matching)"""
        # Implementation with fuzzy matching
        pass

    # Keine create/update/delete - Agents sind file-based
```


#### Example



**Code:**
```python
# mcp_server/server.py
Tool(
    name="agent_list",
    inputSchema={
        "type": "object",
        "properties": {
            "filter_by_type": {"type": "string", "enum": ["specialist", "research"]}
        }
    }
)

async def _handle_agent_list(self, arguments: dict):
    agents = self.agent_manager.list(
        filter_by_type=arguments.get("filter_by_type")
    )
    return [TextContent(
        type="text",
        text=json.dumps([a.to_dict() for a in agents], indent=2)
    )]
```


#### Example



**Code:**
```python
# Gleicher Test-Pattern für alle Managers
class TestAgentManager:
    def test_list(self, manager):
        agents = manager.list()
        assert isinstance(agents, list)
        assert all(isinstance(a, Agent) for a in agents)

    def test_get(self, manager):
        agent = manager.get("some-agent")
        assert agent is None or isinstance(agent, Agent)
```


#### Example



**Code:**
```python
# Gleicher Handler-Pattern für ALLE Tools
async def _handle_X_list(self, arguments: dict):
    items = self.X_manager.list(arguments.get("filters"))
    return [TextContent(type="text", text=json.dumps(...))]
```


#### Example



**Code:**
```python
# DON'T: Jeder Manager eigene Methoden
class AgentManager:
    def fetch_all_agents(self): ...
    def find_agent_by_name(self): ...

class SkillManager:
    def get_skills_list(self): ...
    def lookup_skill(self): ...
```


#### Example



**Code:**
```python
# DON'T: Mixed return types
def list(self) -> dict:  # Manager A
def list(self) -> List[dict]:  # Manager B
def list(self) -> str:  # Manager C (JSON string)
```


#### Example



**Code:**
```python
# DON'T: Unterschiedliches Error Handling
def get(self, id):
    if not found:
        raise ValueError  # Manager A
        return None  # Manager B
        return {"error": "..."}  # Manager C
```


#### Example



**Code:**
```python
class AsyncManager:
    async def list(self) -> List[Model]:
        data = await self.db.read_async(...)
        return [Model.from_dict(d) for d in data]
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/manager-pattern-multi-agent-systems.md`</small>
