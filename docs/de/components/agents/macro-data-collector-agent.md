---
title: macro-data-collector-agent
type: agent
tags: []
lang: en
confidence: 100
---

# macro-data-collector-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```python
SOURCES = {
    'crypto': ['CoinGecko', 'Binance', 'Blockchain.com'],
    'metals': ['FRED', 'LBMA', 'COMEX'],
    'macro': ['BLS', 'Treasury', 'Zillow'],
    'events': ['SEC RSS', 'Congress.gov', 'FedWatch'],
    'news': ['Reuters', 'CryptoPanic', 'Reddit PRAW'],
    'msm': ['Bloomberg RSS', 'CNBC RSS', 'Yahoo Finance'],
    'geopolitical': ['NewsAPI', 'World Bank', 'UN Data']
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/macro-data-collector-agent.md`</small>
