---
title: multi-source-aggregation-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# multi-source-aggregation-pattern


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

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────┐
│              Trigger (Scheduled/Manual)          │
└─────────────────────┬───────────────────────────┘
                      │
      ┌───────────────┼───────────────┬───────────────┐
      ▼               ▼               ▼               ▼
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ Source A │   │ Source B │   │ Source C │   │ Source N │
│ Fetcher  │   │ Fetcher  │   │ Fetcher  │   │ Fetcher  │
└────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
     │              │              │              │
     └──────────────┴──────────────┴──────────────┘
                          │
                    Promise.all
                          │
                 ┌────────▼────────┐
                 │   Normalize to  │
                 │ Unified Schema  │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │  Score & Filter │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │ Idempotent Save │
                 └─────────────────┘
```


#### Example



**Code:**
```typescript
interface AggregatedItem {
  id: string;           // Unique identifier
  source: string;       // Origin (github, reddit, api-x, ...)
  title: string;        // Display name
  author: string;       // Creator/Owner
  score: number;        // Normalized popularity metric
  description: string;  // Summary/excerpt
  url: string;          // Link to original
  created_at: string;   // ISO timestamp
  metadata?: Record<string, unknown>;  // Source-specific extras
}
```


#### Example



**Code:**
```typescript
interface SourceFetcher {
  name: string;
  fetch(config: FetchConfig): Promise<AggregatedItem[]>;
}

interface FetchConfig {
  since?: Date;         // Only items after this date
  limit?: number;       // Max items to fetch
  filters?: string[];   // Source-specific filters
}
```


#### Example



**Code:**
```typescript
async function fetchAllSources(
  fetchers: SourceFetcher[],
  config: FetchConfig
): Promise<AggregatedItem[]> {

  // Parallel execution
  const results = await Promise.all(
    fetchers.map(f => f.fetch(config).catch(err => {
      console.error(`Fetcher ${f.name} failed:`, err);
      return []; // Graceful degradation
    }))
  );

  // Flatten all results
  return results.flat();
}
```


#### Example



**Code:**
```typescript
type ScoreNormalizer = (item: AggregatedItem) => number;

const normalizers: Record<string, ScoreNormalizer> = {
  // High-volume sources: dampen
  reddit: (item) => item.score * 0.3,

  // Log-scale for exponential metrics
  replicate: (item) => Math.pow(item.score, 0.6),

  // Linear passthrough
  github: (item) => item.score,

  // Custom per source
  hackernews: (item) => item.score * 2.5,
};

function normalizeScore(item: AggregatedItem): number {
  const normalizer = normalizers[item.source] || (i => i.score);
  return normalizer(item);
}
```


#### Example



**Code:**
```typescript
interface ContentFilter {
  bannedStrings?: string[];
  bannedPatterns?: RegExp[];
  minScore?: number;
  requiredFields?: string[];
  customFilter?: (item: AggregatedItem) => boolean;
}

function filterItems(
  items: AggregatedItem[],
  filter: ContentFilter
): AggregatedItem[] {
  return items.filter(item => {
    // Banned strings check
    const text = `${item.title} ${item.description}`.toLowerCase();
    for (const banned of filter.bannedStrings || []) {
      if (text.includes(banned)) return false;
    }

    // Min score check
    if (filter.minScore && item.score < filter.minScore) {
      return false;
    }

    // Required fields
    for (const field of filter.requiredFields || []) {
      if (!item[field as keyof AggregatedItem]) return false;
    }

    // Custom filter
    if (filter.customFilter && !filter.customFilter(item)) {
      return false;
    }

    return true;
  });
}
```


#### Example



**Code:**
```typescript
interface Storage {
  upsert(item: AggregatedItem): Promise<void>;
  query(options: QueryOptions): Promise<AggregatedItem[]>;
}

// Composite key prevents duplicates
const compositeKey = `${item.source}:${item.id}`;

// Upsert pattern (insert or update)
await storage.upsert(item, {
  onConflict: ['source', 'id']
});
```


#### Example



**Code:**
```typescript
// 1. Define fetchers
const fetchers: SourceFetcher[] = [
  {
    name: 'github',
    async fetch(config) {
      const resp = await fetch(
        `https://api.github.com/search/repositories?q=created:>${config.since?.toISOString().slice(0,10)}&sort=stars`
      );
      const data = await resp.json();
      return data.items.map(repo => ({
        id: repo.id.toString(),
        source: 'github',
        title: repo.full_name,
        author: repo.owner.login,
        score: repo.stargazers_count,
        description: repo.description || '',
        url: repo.html_url,
        created_at: repo.created_at,
      }));
    }
  },
  // ... more fetchers
];

// 2. Define filters
const filter: ContentFilter = {
  bannedStrings: ['crypto', 'nft', 'telegram'],
  minScore: 5,
  requiredFields: ['author', 'title'],
};

// 3. Aggregate
async function aggregate() {
  const since = new Date();
  since.setDate(since.getDate() - 7);

  // Fetch from all sources
  const items = await fetchAllSources(fetchers, { since });

  // Normalize scores
  const scored = items.map(item => ({
    ...item,
    score: normalizeScore(item),
  }));

  // Filter
  const filtered = filterItems(scored, filter);

  // Sort by normalized score
  filtered.sort((a, b) => b.score - a.score);

  // Save idempotently
  for (const item of filtered) {
    await storage.upsert(item);
  }

  return filtered;
}
```


#### Example



**Code:**
```typescript
type TimeBucket = 'past_day' | 'past_week' | 'past_month';

function getFromDate(bucket: TimeBucket): Date {
  const now = new Date();
  const days = { past_day: 1, past_week: 7, past_month: 30 };
  now.setDate(now.getDate() - days[bucket]);
  return now;
}
```


#### Example



**Code:**
```typescript
function calculateScore(item: AggregatedItem): number {
  const recencyWeight = getRecencyWeight(item.created_at); // 0-1
  const popularityWeight = normalizeScore(item) / 1000;    // 0-1
  const qualityWeight = item.metadata?.quality || 0.5;     // 0-1

  return (
    recencyWeight * 0.3 +
    popularityWeight * 0.5 +
    qualityWeight * 0.2
  ) * 100;
}
```


#### Example



**Code:**
```typescript
async function fetchWithFallback(
  primary: SourceFetcher,
  fallback: SourceFetcher,
  config: FetchConfig
): Promise<AggregatedItem[]> {
  try {
    return await primary.fetch(config);
  } catch (err) {
    console.warn(`${primary.name} failed, using ${fallback.name}`);
    return fallback.fetch(config);
  }
}
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/multi-source-aggregation-pattern.md`</small>
