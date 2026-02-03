---
title: ai-content-generation-pipeline
type: pattern
tags: ["[ai", " content-generation", " pipeline", " automation", " quality-control", " seo", " etsy", " midjourney]"]
lang: en
confidence: 100
---

# ai-content-generation-pipeline


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2024-11-22 |</div>

<div class="component-tags">
<span class="tag tag-[ai">[ai</span>
<span class="tag tag--content-generation"> content-generation</span>
<span class="tag tag--pipeline"> pipeline</span>
<span class="tag tag--automation"> automation</span>
<span class="tag tag--quality-control"> quality-control</span>
<span class="tag tag--seo"> seo</span>
<span class="tag tag--etsy"> etsy</span>
<span class="tag tag--midjourney]"> midjourney]</span>
</div>

## What It Does

${content.description}


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
┌─────────────────────────────────────────────────────────────────────┐
│                     AI CONTENT GENERATION PIPELINE                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────┐   ┌──────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐
│  │  INPUT  │──▶│ RESEARCH │──▶│ GENERATION │──▶│ REFINE   │──▶│ OUTPUT │
│  │ Process │   │  Phase   │   │   Phase    │   │  Phase   │   │ Package│
│  └────┬────┘   └────┬─────┘   └─────┬──────┘   └────┬─────┘   └───┬────┘
│       │             │               │               │              │
│       ▼             ▼               ▼               ▼              ▼
│  ┌─────────┐   ┌──────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐
│  │VALIDATE │   │CONFIDENCE│   │  STRUCT    │   │  QUALITY │   │COMPLETE│
│  │  GATE   │   │   GATE   │   │   GATE     │   │   GATE   │   │  GATE  │
│  │  ✓/✗    │   │  ≥90%    │   │  Schema    │   │  Score   │   │  All   │
│  └─────────┘   └──────────┘   └────────────┘   └──────────┘   └────────┘
│       │             │               │               │              │
│       ▼             ▼               ▼               ▼              ▼
│  [RETRY/FAIL]  [FALLBACK]    [REGENERATE]    [IMPROVE]      [SUCCESS]
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```typescript
// types/pipeline.ts
interface PipelineInput {
  type: 'poster' | 'blog' | 'product' | 'social' | 'email';
  rawInput: string;
  context?: {
    targetAudience?: string;
    platform?: string;
    language?: string;
    style?: string;
  };
  options?: {
    priority?: 'speed' | 'quality' | 'cost';
    maxRetries?: number;
    timeout?: number;
  };
}

interface ProcessedInput {
  type: PipelineInput['type'];
  normalizedInput: string;
  detectedCategory: string;
  keywords: string[];
  language: 'en' | 'de';
  enrichedContext: Record<string, any>;
  validationPassed: boolean;
  validationErrors?: string[];
}

// services/pipeline/input-processor.ts
export class InputProcessor {
  private readonly MIN_INPUT_LENGTH = 3;
  private readonly MAX_INPUT_LENGTH = 500;

  async process(input: PipelineInput): Promise<ProcessedInput> {
    // 1. Basic validation
    const validationResult = this.validateInput(input);
    if (!validationResult.valid) {
      return {
        ...this.createEmptyResult(input),
        validationPassed: false,
        validationErrors: validationResult.errors
      };
    }

    // 2. Normalize input
    const normalizedInput = this.normalizeInput(input.rawInput);

    // 3. Detect language
    const language = this.detectLanguage(normalizedInput);

    // 4. Extract keywords
    const keywords = await this.extractKeywords(normalizedInput, language);

    // 5. Detect category
    const detectedCategory = await this.detectCategory(normalizedInput, keywords);

    // 6. Enrich context
    const enrichedContext = await this.enrichContext(input, {
      language,
      keywords,
      category: detectedCategory
    });

    return {
      type: input.type,
      normalizedInput,
      detectedCategory,
      keywords,
      language,
      enrichedContext,
      validationPassed: true
    };
  }

  private validateInput(input: PipelineInput): { valid: boolean; errors: string[] } {
    const errors: string[] = [];

    if (!input.rawInput || input.rawInput.trim().length < this.MIN_INPUT_LENGTH) {
      errors.push(`Input must be at least ${this.MIN_INPUT_LENGTH} characters`);
    }

    if (input.rawInput && input.rawInput.length > this.MAX_INPUT_LENGTH) {
      errors.push(`Input must be less than ${this.MAX_INPUT_LENGTH} characters`);
    }

    if (!['poster', 'blog', 'product', 'social', 'email'].includes(input.type)) {
      errors.push(`Invalid content type: ${input.type}`);
    }

    return { valid: errors.length === 0, errors };
  }

  private normalizeInput(raw: string): string {
    return raw
      .trim()
      .replace(/\s+/g, ' ')           // Multiple spaces → single
      .replace(/[""]/g, '"')          // Curly quotes → straight
      .replace(/['']/g, "'")          // Curly apostrophes → straight
      .toLowerCase();
  }

  private detectLanguage(text: string): 'en' | 'de' {
    // Simple heuristic based on common words
    const germanIndicators = ['und', 'der', 'die', 'das', 'für', 'mit', 'ist', 'ein', 'eine'];
    const words = text.toLowerCase().split(/\s+/);
    const germanCount = words.filter(w => germanIndicators.includes(w)).length;
    return germanCount >= 2 ? 'de' : 'en';
  }

  private async extractKeywords(text: string, language: 'en' | 'de'): Promise<string[]> {
    // Use Claude for intelligent keyword extraction
    const response = await this.llm.generate({
      model: 'claude-haiku',  // Fast, cheap for this task
      prompt: `Extract 5-10 main keywords from this text. Return as JSON array.
        Language: ${language}
        Text: "${text}"

        Return ONLY the JSON array, no explanation.`,
      maxTokens: 100
    });

    try {
      return JSON.parse(response);
    } catch {
      // Fallback: simple word extraction
      return text.split(/\s+/).filter(w => w.length > 3).slice(0, 10);
    }
  }

  private async detectCategory(text: string, keywords: string[]): Promise<string> {
    // Category detection based on keywords
    const categoryMap: Record<string, string[]> = {
      'motivational': ['motivation', 'inspire', 'success', 'dream', 'goal', 'believe'],
      'nature': ['nature', 'forest', 'ocean', 'mountain', 'sunset', 'landscape'],
      'minimalist': ['minimal', 'simple', 'clean', 'modern', 'abstract'],
      'typography': ['quote', 'text', 'word', 'letter', 'font'],
      'vintage': ['vintage', 'retro', 'classic', 'old', 'antique'],
      'abstract': ['abstract', 'geometric', 'pattern', 'shape', 'color']
    };

    for (const [category, indicators] of Object.entries(categoryMap)) {
      if (keywords.some(k => indicators.includes(k.toLowerCase()))) {
        return category;
      }
    }

    return 'general';
  }

  private async enrichContext(
    input: PipelineInput,
    extracted: { language: string; keywords: string[]; category: string }
  ): Promise<Record<string, any>> {
    return {
      ...input.context,
      ...extracted,
      timestamp: new Date().toISOString(),
      processingPriority: input.options?.priority || 'quality'
    };
  }
}
```


#### Example



**Code:**
```typescript
// services/pipeline/research-phase.ts
interface ResearchResult {
  sources: ResearchSource[];
  aggregatedData: Record<string, any>;
  confidenceScore: number;          // 0-1
  researchComplete: boolean;
  fallbackUsed: boolean;
}

interface ResearchSource {
  type: 'internal' | 'seo' | 'trends' | 'competitor';
  data: any;
  confidence: number;
  timestamp: Date;
}

export class ResearchPhase {
  private readonly CONFIDENCE_THRESHOLD = 0.9;  // 90%
  private readonly MAX_SOURCES = 5;

  async research(input: ProcessedInput): Promise<ResearchResult> {
    const sources: ResearchSource[] = [];

    // 1. Internal Knowledge (from KB)
    const internalSource = await this.searchInternalKB(input);
    if (internalSource) sources.push(internalSource);

    // 2. SEO Research
    const seoSource = await this.researchSEO(input);
    if (seoSource) sources.push(seoSource);

    // 3. Trend Analysis
    const trendSource = await this.analyzeTrends(input);
    if (trendSource) sources.push(trendSource);

    // 4. Competitor Analysis (if applicable)
    if (input.type === 'poster' || input.type === 'product') {
      const competitorSource = await this.analyzeCompetitors(input);
      if (competitorSource) sources.push(competitorSource);
    }

    // 5. Aggregate and score
    const aggregatedData = this.aggregateResults(sources);
    const confidenceScore = this.calculateConfidence(sources);

    // Check threshold
    if (confidenceScore < this.CONFIDENCE_THRESHOLD) {
      // Try fallback sources
      const fallbackSource = await this.getFallbackData(input);
      if (fallbackSource) {
        sources.push(fallbackSource);
        const newConfidence = this.calculateConfidence(sources);
        return {
          sources,
          aggregatedData: this.aggregateResults(sources),
          confidenceScore: newConfidence,
          researchComplete: newConfidence >= this.CONFIDENCE_THRESHOLD,
          fallbackUsed: true
        };
      }
    }

    return {
      sources,
      aggregatedData,
      confidenceScore,
      researchComplete: confidenceScore >= this.CONFIDENCE_THRESHOLD,
      fallbackUsed: false
    };
  }

  private async researchSEO(input: ProcessedInput): Promise<ResearchSource | null> {
    // Platform-specific SEO research
    if (input.type === 'poster') {
      return this.etsySEOResearch(input);
    }

    // Generic SEO for other types
    return {
      type: 'seo',
      data: {
        primaryKeywords: input.keywords.slice(0, 3),
        secondaryKeywords: input.keywords.slice(3),
        recommendedTags: await this.generateSEOTags(input.keywords),
        competitorKeywords: []
      },
      confidence: 0.8,
      timestamp: new Date()
    };
  }

  private async etsySEOResearch(input: ProcessedInput): Promise<ResearchSource> {
    // Etsy-specific SEO best practices
    const etsyOptimization = {
      titleFormat: {
        maxLength: 140,
        structure: '[Primary Keyword] - [Style] - [Size/Type] - [Use Case]',
        frontLoadKeywords: true
      },
      tags: {
        count: 13,  // Etsy allows exactly 13
        maxLength: 20,
        includeVariations: true,
        mixLongTailAndShort: true
      },
      description: {
        frontLoad: 'First 160 chars are preview - include main keywords',
        structure: ['Hook', 'Features', 'Benefits', 'Specs', 'CTA']
      }
    };

    // Generate optimized tags based on category
    const categoryTags = await this.getCategoryTags(input.detectedCategory);
    const trendingTags = await this.getTrendingTags(input.keywords[0]);

    return {
      type: 'seo',
      data: {
        optimization: etsyOptimization,
        categoryTags,
        trendingTags,
        recommendedTags: this.mergeAndPrioritizeTags(categoryTags, trendingTags, input.keywords)
      },
      confidence: 0.85,
      timestamp: new Date()
    };
  }

  private async analyzeTrends(input: ProcessedInput): Promise<ResearchSource | null> {
    // Pinterest/Google Trends analysis
    const trendData = {
      seasonality: this.getSeasonalRelevance(new Date()),
      risingTopics: await this.getRisingTopics(input.detectedCategory),
      colorTrends: await this.getColorTrends(),
      styleTrends: await this.getStyleTrends(input.detectedCategory)
    };

    return {
      type: 'trends',
      data: trendData,
      confidence: 0.75,  // Trends are less certain
      timestamp: new Date()
    };
  }

  private calculateConfidence(sources: ResearchSource[]): number {
    if (sources.length === 0) return 0;

    // Weighted average based on source type importance
    const weights: Record<string, number> = {
      'internal': 1.0,
      'seo': 0.9,
      'competitor': 0.8,
      'trends': 0.7
    };

    let totalWeight = 0;
    let weightedSum = 0;

    for (const source of sources) {
      const weight = weights[source.type] || 0.5;
      totalWeight += weight;
      weightedSum += source.confidence * weight;
    }

    return totalWeight > 0 ? weightedSum / totalWeight : 0;
  }

  private aggregateResults(sources: ResearchSource[]): Record<string, any> {
    const aggregated: Record<string, any> = {
      keywords: new Set<string>(),
      tags: new Set<string>(),
      optimization: {},
      trends: {}
    };

    for (const source of sources) {
      if (source.data.keywords) {
        source.data.keywords.forEach((k: string) => aggregated.keywords.add(k));
      }
      if (source.data.tags || source.data.recommendedTags) {
        (source.data.tags || source.data.recommendedTags).forEach((t: string) =>
          aggregated.tags.add(t)
        );
      }
      if (source.data.optimization) {
        aggregated.optimization = { ...aggregated.optimization, ...source.data.optimization };
      }
      if (source.type === 'trends') {
        aggregated.trends = source.data;
      }
    }

    // Convert Sets to Arrays
    aggregated.keywords = [...aggregated.keywords];
    aggregated.tags = [...aggregated.tags];

    return aggregated;
  }
}
```


#### Example



**Code:**
```typescript
// services/pipeline/generation-phase.ts
interface GenerationConfig {
  primaryModel: 'claude-opus' | 'claude-sonnet' | 'claude-haiku';
  fallbackModels: Array<'claude-opus' | 'claude-sonnet' | 'claude-haiku'>;
  outputSchema: z.ZodSchema;
  maxRetries: number;
  temperature: number;
}

interface GenerationResult<T> {
  content: T;
  model: string;
  attempts: number;
  validationPassed: boolean;
  validationErrors?: string[];
  tokensUsed: number;
  cost: number;
}

// Etsy Listing Schema Example
const EtsyListingSchema = z.object({
  title: z.string().min(10).max(140),
  description: z.string().min(100).max(10000),
  tags: z.array(z.string().max(20)).length(13),
  primaryKeyword: z.string(),
  category: z.string(),
  priceRange: z.enum(['budget', 'mid', 'premium']),
  seoScore: z.number().min(0).max(10)
});

type EtsyListing = z.infer<typeof EtsyListingSchema>;

export class GenerationPhase {
  private readonly MODEL_COSTS = {
    'claude-opus': { input: 0.015, output: 0.075 },    // per 1k tokens
    'claude-sonnet': { input: 0.003, output: 0.015 },
    'claude-haiku': { input: 0.00025, output: 0.00125 }
  };

  async generate<T>(
    input: ProcessedInput,
    research: ResearchResult,
    config: GenerationConfig
  ): Promise<GenerationResult<T>> {
    const models = [config.primaryModel, ...config.fallbackModels];
    let lastError: Error | null = null;
    let totalTokens = 0;
    let totalCost = 0;
    let attempts = 0;

    for (const model of models) {
      for (let retry = 0; retry < config.maxRetries; retry++) {
        attempts++;
        try {
          const prompt = this.buildPrompt(input, research, config.outputSchema);

          const response = await this.llm.generate({
            model,
            prompt,
            temperature: config.temperature,
            maxTokens: 4000
          });

          totalTokens += response.usage.totalTokens;
          totalCost += this.calculateCost(model, response.usage);

          // Parse and validate
          const parsed = this.parseResponse<T>(response.content);
          const validation = config.outputSchema.safeParse(parsed);

          if (validation.success) {
            return {
              content: validation.data as T,
              model,
              attempts,
              validationPassed: true,
              tokensUsed: totalTokens,
              cost: totalCost
            };
          }

          // Validation failed - try to fix
          const fixed = await this.attemptFix(parsed, validation.error, model);
          const revalidation = config.outputSchema.safeParse(fixed);

          if (revalidation.success) {
            return {
              content: revalidation.data as T,
              model,
              attempts,
              validationPassed: true,
              tokensUsed: totalTokens,
              cost: totalCost
            };
          }

          lastError = new Error(`Validation failed: ${validation.error.message}`);
        } catch (error) {
          lastError = error as Error;
          // Continue to next retry/model
        }
      }
    }

    // All models/retries exhausted
    throw new Error(`Generation failed after ${attempts} attempts: ${lastError?.message}`);
  }

  private buildPrompt(
    input: ProcessedInput,
    research: ResearchResult,
    schema: z.ZodSchema
  ): string {
    const schemaDescription = this.zodToDescription(schema);

    return `You are an expert content creator specialized in ${input.type} content.

## Task
Create optimized content based on the following input and research.

## Input
- Topic: ${input.normalizedInput}
- Category: ${input.detectedCategory}
- Language: ${input.language}
- Keywords: ${input.keywords.join(', ')}

## Research Data
${JSON.stringify(research.aggregatedData, null, 2)}

## Output Requirements
${schemaDescription}

## Quality Standards
- SEO optimized with front-loaded keywords
- Engaging and actionable language
- Platform-specific formatting
- All required fields must be present

Return ONLY valid JSON matching the schema. No explanations or markdown.`;
  }

  private async attemptFix<T>(
    parsed: any,
    error: z.ZodError,
    model: string
  ): Promise<T> {
    const fixPrompt = `The following JSON has validation errors. Fix them.

JSON:
${JSON.stringify(parsed, null, 2)}

Errors:
${error.errors.map(e => `- ${e.path.join('.')}: ${e.message}`).join('\n')}

Return ONLY the fixed JSON, no explanations.`;

    const response = await this.llm.generate({
      model,
      prompt: fixPrompt,
      temperature: 0.1,  // Low temperature for fixing
      maxTokens: 4000
    });

    return this.parseResponse(response.content);
  }

  private parseResponse<T>(content: string): T {
    // Try to extract JSON from response
    const jsonMatch = content.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      throw new Error('No JSON found in response');
    }

    return JSON.parse(jsonMatch[0]);
  }

  private calculateCost(model: string, usage: { inputTokens: number; outputTokens: number }): number {
    const rates = this.MODEL_COSTS[model as keyof typeof this.MODEL_COSTS];
    if (!rates) return 0;

    return (usage.inputTokens / 1000 * rates.input) +
           (usage.outputTokens / 1000 * rates.output);
  }

  private zodToDescription(schema: z.ZodSchema): string {
    // Generate human-readable schema description
    // This is simplified - in production use zod-to-json-schema
    return `Return a JSON object with the following structure:
{
  "title": "string (10-140 chars)",
  "description": "string (100-10000 chars)",
  "tags": ["array of 13 strings, each max 20 chars"],
  "primaryKeyword": "string",
  "category": "string",
  "priceRange": "budget | mid | premium",
  "seoScore": "number 0-10"
}`;
  }
}
```


#### Example



**Code:**
```typescript
// services/pipeline/refinement-phase.ts
interface RefinementResult<T> {
  refined: T;
  improvements: Improvement[];
  qualityScore: QualityScore;
  passesGate: boolean;
}

interface Improvement {
  field: string;
  original: any;
  refined: any;
  reason: string;
}

interface QualityScore {
  seo: number;          // 0-10
  readability: number;  // 0-10
  engagement: number;   // 0-10
  completeness: number; // 0-10
  overall: number;      // Weighted average
}

export class RefinementPhase {
  private readonly QUALITY_THRESHOLD = 8;  // Minimum overall score

  async refine<T extends Record<string, any>>(
    generated: T,
    input: ProcessedInput,
    research: ResearchResult
  ): Promise<RefinementResult<T>> {
    const improvements: Improvement[] = [];
    let refined = { ...generated };

    // 1. SEO Optimization
    refined = await this.optimizeSEO(refined, research, improvements);

    // 2. Readability Enhancement
    refined = await this.enhanceReadability(refined, input.language, improvements);

    // 3. Platform-specific Formatting
    refined = await this.formatForPlatform(refined, input.type, improvements);

    // 4. Calculate Quality Score
    const qualityScore = await this.calculateQualityScore(refined, input, research);

    // 5. If score too low, attempt improvement
    if (qualityScore.overall < this.QUALITY_THRESHOLD) {
      const improved = await this.attemptImprovement(refined, qualityScore, input);
      const newScore = await this.calculateQualityScore(improved, input, research);

      if (newScore.overall > qualityScore.overall) {
        refined = improved;
        improvements.push({
          field: 'overall',
          original: qualityScore.overall,
          refined: newScore.overall,
          reason: 'AI-powered quality improvement'
        });
      }
    }

    const finalScore = await this.calculateQualityScore(refined, input, research);

    return {
      refined,
      improvements,
      qualityScore: finalScore,
      passesGate: finalScore.overall >= this.QUALITY_THRESHOLD
    };
  }

  private async optimizeSEO<T extends Record<string, any>>(
    content: T,
    research: ResearchResult,
    improvements: Improvement[]
  ): Promise<T> {
    const result = { ...content };

    // Title optimization
    if (result.title) {
      const optimizedTitle = this.frontLoadKeywords(
        result.title,
        research.aggregatedData.keywords.slice(0, 3)
      );

      if (optimizedTitle !== result.title) {
        improvements.push({
          field: 'title',
          original: result.title,
          refined: optimizedTitle,
          reason: 'Front-loaded primary keywords for SEO'
        });
        result.title = optimizedTitle;
      }
    }

    // Tag optimization (for Etsy)
    if (result.tags && Array.isArray(result.tags)) {
      const optimizedTags = this.optimizeTags(
        result.tags,
        research.aggregatedData.tags,
        13  // Etsy max
      );

      if (JSON.stringify(optimizedTags) !== JSON.stringify(result.tags)) {
        improvements.push({
          field: 'tags',
          original: result.tags,
          refined: optimizedTags,
          reason: 'Optimized tag mix for discoverability'
        });
        result.tags = optimizedTags;
      }
    }

    return result;
  }

  private frontLoadKeywords(title: string, keywords: string[]): string {
    // Check if primary keyword is already at front
    const lowerTitle = title.toLowerCase();
    const primaryKeyword = keywords[0]?.toLowerCase();

    if (primaryKeyword && !lowerTitle.startsWith(primaryKeyword)) {
      // Restructure title to front-load keyword
      // Example: "Beautiful Sunset Print" → "Sunset Print - Beautiful Nature Wall Art"
      const hasKeyword = lowerTitle.includes(primaryKeyword);

      if (hasKeyword) {
        // Move keyword to front
        const regex = new RegExp(keywords[0], 'i');
        const keyword = title.match(regex)?.[0] || keywords[0];
        const withoutKeyword = title.replace(regex, '').trim().replace(/^[-,]\s*/, '');
        return `${keyword} ${withoutKeyword}`.substring(0, 140);
      }
    }

    return title;
  }

  private optimizeTags(
    currentTags: string[],
    researchTags: string[],
    maxTags: number
  ): string[] {
    // Strategy: Mix of exact keywords, long-tail variations, and trending tags
    const optimized: string[] = [];
    const used = new Set<string>();

    // 1. Primary keywords (first 3)
    for (const tag of currentTags.slice(0, 3)) {
      if (optimized.length < maxTags && !used.has(tag.toLowerCase())) {
        optimized.push(tag);
        used.add(tag.toLowerCase());
      }
    }

    // 2. Research-backed tags
    for (const tag of researchTags) {
      if (optimized.length < maxTags && !used.has(tag.toLowerCase())) {
        optimized.push(tag);
        used.add(tag.toLowerCase());
      }
    }

    // 3. Fill with remaining original tags
    for (const tag of currentTags) {
      if (optimized.length < maxTags && !used.has(tag.toLowerCase())) {
        optimized.push(tag);
        used.add(tag.toLowerCase());
      }
    }

    return optimized.slice(0, maxTags);
  }

  private async calculateQualityScore<T extends Record<string, any>>(
    content: T,
    input: ProcessedInput,
    research: ResearchResult
  ): Promise<QualityScore> {
    // SEO Score
    const seoScore = this.calculateSEOScore(content, research.aggregatedData.keywords);

    // Readability Score
    const readabilityScore = this.calculateReadabilityScore(content);

    // Engagement Score
    const engagementScore = await this.calculateEngagementScore(content, input.type);

    // Completeness Score
    const completenessScore = this.calculateCompletenessScore(content);

    // Weighted overall
    const overall = (
      seoScore * 0.3 +
      readabilityScore * 0.2 +
      engagementScore * 0.3 +
      completenessScore * 0.2
    );

    return {
      seo: seoScore,
      readability: readabilityScore,
      engagement: engagementScore,
      completeness: completenessScore,
      overall
    };
  }

  private calculateSEOScore(content: Record<string, any>, keywords: string[]): number {
    let score = 5;  // Base score

    // Title contains primary keyword
    if (content.title?.toLowerCase().includes(keywords[0]?.toLowerCase())) {
      score += 2;
    }

    // Keyword at beginning of title
    if (content.title?.toLowerCase().startsWith(keywords[0]?.toLowerCase())) {
      score += 1;
    }

    // Tags cover main keywords
    if (content.tags) {
      const tagKeywordCoverage = keywords.filter(k =>
        content.tags.some((t: string) => t.toLowerCase().includes(k.toLowerCase()))
      ).length / keywords.length;
      score += tagKeywordCoverage * 2;
    }

    return Math.min(10, score);
  }

  private calculateReadabilityScore(content: Record<string, any>): number {
    if (!content.description) return 5;

    const text = content.description;
    const sentences = text.split(/[.!?]+/).filter(Boolean);
    const words = text.split(/\s+/);

    // Average sentence length (ideal: 15-20 words)
    const avgSentenceLength = words.length / sentences.length;
    let score = 5;

    if (avgSentenceLength >= 10 && avgSentenceLength <= 25) {
      score += 3;
    } else if (avgSentenceLength > 25) {
      score += 1;  // Too long
    }

    // Paragraph breaks (good for readability)
    const paragraphs = text.split(/\n\n+/).length;
    if (paragraphs >= 3) score += 2;

    return Math.min(10, score);
  }

  private async calculateEngagementScore(
    content: Record<string, any>,
    type: string
  ): Promise<number> {
    // Use AI to score engagement potential
    const response = await this.llm.generate({
      model: 'claude-haiku',
      prompt: `Rate the engagement potential of this ${type} content on a scale of 1-10.

Content:
${JSON.stringify(content, null, 2)}

Consider:
- Emotional appeal
- Clear value proposition
- Call to action
- Visual appeal description

Return ONLY a number 1-10.`,
      maxTokens: 10
    });

    return parseFloat(response) || 5;
  }

  private calculateCompletenessScore(content: Record<string, any>): number {
    const requiredFields = ['title', 'description', 'tags'];
    let filledCount = 0;

    for (const field of requiredFields) {
      if (content[field] && (
        typeof content[field] === 'string' ? content[field].length > 0 :
        Array.isArray(content[field]) ? content[field].length > 0 : true
      )) {
        filledCount++;
      }
    }

    return (filledCount / requiredFields.length) * 10;
  }
}
```


#### Example



**Code:**
```typescript
// services/pipeline/output-phase.ts
interface OutputPackage<T> {
  content: T;
  metadata: OutputMetadata;
  exports: OutputExport[];
  verification: OutputVerification;
}

interface OutputMetadata {
  id: string;
  type: string;
  createdAt: Date;
  pipeline: {
    inputHash: string;
    researchConfidence: number;
    generationModel: string;
    qualityScore: number;
    processingTimeMs: number;
    totalCost: number;
  };
  version: string;
}

interface OutputExport {
  format: 'json' | 'markdown' | 'csv' | 'html';
  content: string;
  filename: string;
}

interface OutputVerification {
  checksumValid: boolean;
  schemaValid: boolean;
  allFieldsPresent: boolean;
  ready: boolean;
}

export class OutputPhase {
  async package<T extends Record<string, any>>(
    content: T,
    pipelineData: {
      input: ProcessedInput;
      research: ResearchResult;
      generation: { model: string; cost: number };
      refinement: { qualityScore: QualityScore };
      startTime: Date;
    }
  ): Promise<OutputPackage<T>> {
    const now = new Date();
    const processingTimeMs = now.getTime() - pipelineData.startTime.getTime();

    // 1. Generate metadata
    const metadata: OutputMetadata = {
      id: this.generateId(),
      type: pipelineData.input.type,
      createdAt: now,
      pipeline: {
        inputHash: this.hashInput(pipelineData.input.normalizedInput),
        researchConfidence: pipelineData.research.confidenceScore,
        generationModel: pipelineData.generation.model,
        qualityScore: pipelineData.refinement.qualityScore.overall,
        processingTimeMs,
        totalCost: pipelineData.generation.cost
      },
      version: '1.0.0'
    };

    // 2. Generate exports
    const exports = await this.generateExports(content, metadata);

    // 3. Verify output
    const verification = this.verifyOutput(content, exports);

    return {
      content,
      metadata,
      exports,
      verification
    };
  }

  private async generateExports<T extends Record<string, any>>(
    content: T,
    metadata: OutputMetadata
  ): Promise<OutputExport[]> {
    const exports: OutputExport[] = [];
    const baseName = `${metadata.type}-${metadata.id}`;

    // JSON export
    exports.push({
      format: 'json',
      content: JSON.stringify({ content, metadata }, null, 2),
      filename: `${baseName}.json`
    });

    // Markdown export (for content types that support it)
    if (content.title && content.description) {
      exports.push({
        format: 'markdown',
        content: this.toMarkdown(content, metadata),
        filename: `${baseName}.md`
      });
    }

    // Platform-specific export
    if (metadata.type === 'poster') {
      exports.push({
        format: 'csv',
        content: this.toEtsyCSV(content),
        filename: `${baseName}-etsy.csv`
      });
    }

    return exports;
  }

  private toMarkdown<T extends Record<string, any>>(
    content: T,
    metadata: OutputMetadata
  ): string {
    return `# ${content.title}

## Description

${content.description}

## Tags

${content.tags?.map((t: string) => `- ${t}`).join('\n') || 'No tags'}

---

*Generated: ${metadata.createdAt.toISOString()}*
*Quality Score: ${metadata.pipeline.qualityScore.toFixed(1)}/10*
*Model: ${metadata.pipeline.generationModel}*
`;
  }

  private toEtsyCSV<T extends Record<string, any>>(content: T): string {
    // Etsy bulk upload CSV format
    const headers = ['title', 'description', 'tags', 'price', 'quantity', 'sku'];
    const values = [
      `"${content.title?.replace(/"/g, '""') || ''}"`,
      `"${content.description?.replace(/"/g, '""') || ''}"`,
      `"${content.tags?.join(',') || ''}"`,
      content.price || '',
      content.quantity || '999',
      content.sku || ''
    ];

    return `${headers.join(',')}\n${values.join(',')}`;
  }

  private verifyOutput<T extends Record<string, any>>(
    content: T,
    exports: OutputExport[]
  ): OutputVerification {
    const checksumValid = exports.every(e => e.content.length > 0);
    const schemaValid = Boolean(content.title && content.description);
    const allFieldsPresent = Boolean(
      content.title &&
      content.description &&
      content.tags?.length > 0
    );

    return {
      checksumValid,
      schemaValid,
      allFieldsPresent,
      ready: checksumValid && schemaValid && allFieldsPresent
    };
  }

  private generateId(): string {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  private hashInput(input: string): string {
    // Simple hash for deduplication
    let hash = 0;
    for (let i = 0; i < input.length; i++) {
      const char = input.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash = hash & hash;
    }
    return Math.abs(hash).toString(16);
  }
}
```


#### Example



**Code:**
```typescript
// services/pipeline/orchestrator.ts
interface PipelineResult<T> {
  success: boolean;
  output?: OutputPackage<T>;
  error?: PipelineError;
  stats: PipelineStats;
}

interface PipelineStats {
  totalTimeMs: number;
  stageTimings: Record<string, number>;
  cost: number;
  tokensUsed: number;
  retries: number;
}

interface PipelineError {
  stage: 'input' | 'research' | 'generation' | 'refinement' | 'output';
  message: string;
  recoverable: boolean;
}

export class ContentPipeline<T extends Record<string, any>> {
  private inputProcessor: InputProcessor;
  private researchPhase: ResearchPhase;
  private generationPhase: GenerationPhase;
  private refinementPhase: RefinementPhase;
  private outputPhase: OutputPhase;

  constructor(private config: GenerationConfig) {
    this.inputProcessor = new InputProcessor();
    this.researchPhase = new ResearchPhase();
    this.generationPhase = new GenerationPhase();
    this.refinementPhase = new RefinementPhase();
    this.outputPhase = new OutputPhase();
  }

  async run(input: PipelineInput): Promise<PipelineResult<T>> {
    const startTime = new Date();
    const stageTimings: Record<string, number> = {};
    let totalRetries = 0;
    let totalTokens = 0;
    let totalCost = 0;

    try {
      // Stage 1: Input Processing
      const inputStart = Date.now();
      const processedInput = await this.inputProcessor.process(input);
      stageTimings.input = Date.now() - inputStart;

      if (!processedInput.validationPassed) {
        return this.createErrorResult('input', processedInput.validationErrors?.join(', ') || 'Validation failed', false, {
          totalTimeMs: Date.now() - startTime.getTime(),
          stageTimings,
          cost: 0,
          tokensUsed: 0,
          retries: 0
        });
      }

      // Stage 2: Research
      const researchStart = Date.now();
      const research = await this.researchPhase.research(processedInput);
      stageTimings.research = Date.now() - researchStart;

      if (!research.researchComplete) {
        // Warning but continue - research is enhancement
        console.warn('Research incomplete, continuing with available data');
      }

      // Stage 3: Generation
      const generationStart = Date.now();
      const generation = await this.generationPhase.generate<T>(
        processedInput,
        research,
        this.config
      );
      stageTimings.generation = Date.now() - generationStart;
      totalRetries += generation.attempts - 1;
      totalTokens += generation.tokensUsed;
      totalCost += generation.cost;

      // Stage 4: Refinement
      const refinementStart = Date.now();
      const refinement = await this.refinementPhase.refine(
        generation.content,
        processedInput,
        research
      );
      stageTimings.refinement = Date.now() - refinementStart;

      if (!refinement.passesGate) {
        return this.createErrorResult('refinement', `Quality score ${refinement.qualityScore.overall} below threshold`, true, {
          totalTimeMs: Date.now() - startTime.getTime(),
          stageTimings,
          cost: totalCost,
          tokensUsed: totalTokens,
          retries: totalRetries
        });
      }

      // Stage 5: Output
      const outputStart = Date.now();
      const output = await this.outputPhase.package(refinement.refined, {
        input: processedInput,
        research,
        generation: { model: generation.model, cost: generation.cost },
        refinement: { qualityScore: refinement.qualityScore },
        startTime
      });
      stageTimings.output = Date.now() - outputStart;

      if (!output.verification.ready) {
        return this.createErrorResult('output', 'Output verification failed', true, {
          totalTimeMs: Date.now() - startTime.getTime(),
          stageTimings,
          cost: totalCost,
          tokensUsed: totalTokens,
          retries: totalRetries
        });
      }

      return {
        success: true,
        output,
        stats: {
          totalTimeMs: Date.now() - startTime.getTime(),
          stageTimings,
          cost: totalCost,
          tokensUsed: totalTokens,
          retries: totalRetries
        }
      };
    } catch (error) {
      return this.createErrorResult(
        'generation',
        (error as Error).message,
        false,
        {
          totalTimeMs: Date.now() - startTime.getTime(),
          stageTimings,
          cost: totalCost,
          tokensUsed: totalTokens,
          retries: totalRetries
        }
      );
    }
  }

  private createErrorResult(
    stage: PipelineError['stage'],
    message: string,
    recoverable: boolean,
    stats: PipelineStats
  ): PipelineResult<T> {
    return {
      success: false,
      error: { stage, message, recoverable },
      stats
    };
  }
}
```


#### Example



**Code:**
```typescript
// Usage: Create Etsy listing for motivational poster
const pipeline = new ContentPipeline<EtsyListing>({
  primaryModel: 'claude-sonnet',
  fallbackModels: ['claude-opus', 'claude-haiku'],
  outputSchema: EtsyListingSchema,
  maxRetries: 3,
  temperature: 0.7
});

const result = await pipeline.run({
  type: 'poster',
  rawInput: 'minimalist mountain sunset motivational quote poster',
  context: {
    targetAudience: 'home decor enthusiasts',
    platform: 'etsy',
    language: 'en',
    style: 'modern minimalist'
  },
  options: {
    priority: 'quality'
  }
});

if (result.success) {
  console.log('Title:', result.output.content.title);
  // Output: "Mountain Sunset Quote Print - Minimalist Nature Wall Art - Motivational Home Decor"

  console.log('Tags:', result.output.content.tags);
  // Output: ["mountain wall art", "sunset print", "motivational quote", ...]

  console.log('Quality Score:', result.output.metadata.pipeline.qualityScore);
  // Output: 8.7

  console.log('Cost:', result.stats.cost);
  // Output: 0.012 (USD)
}
```


#### Example



**Code:**
```typescript
// Batch process multiple poster ideas
const ideas = [
  'abstract geometric shapes blue',
  'vintage botanical illustration',
  'inspirational sunrise quote',
  'minimalist line art woman'
];

const results = await Promise.all(
  ideas.map(idea => pipeline.run({
    type: 'poster',
    rawInput: idea,
    options: { priority: 'cost' }  // Optimize for cost in batch
  }))
);

const successful = results.filter(r => r.success);
const failed = results.filter(r => !r.success);

console.log(`Processed: ${successful.length}/${results.length}`);
console.log(`Total cost: $${results.reduce((sum, r) => sum + r.stats.cost, 0).toFixed(3)}`);
```


#### Example



**Code:**
```typescript
// Model selection based on task priority
const MODEL_STRATEGIES = {
  // Maximum quality, higher cost
  quality: {
    primaryModel: 'claude-opus',
    fallbackModels: ['claude-sonnet'],
    maxRetries: 5,
    expectedCost: 0.05  // per item
  },

  // Balanced (default)
  balanced: {
    primaryModel: 'claude-sonnet',
    fallbackModels: ['claude-opus', 'claude-haiku'],
    maxRetries: 3,
    expectedCost: 0.015
  },

  // Cost optimized
  cost: {
    primaryModel: 'claude-haiku',
    fallbackModels: ['claude-sonnet'],
    maxRetries: 2,
    expectedCost: 0.003
  },

  // Speed optimized
  speed: {
    primaryModel: 'claude-haiku',
    fallbackModels: [],
    maxRetries: 1,
    expectedCost: 0.002
  }
};

// Monthly cost estimation
function estimateMonthlyCost(itemsPerDay: number, strategy: keyof typeof MODEL_STRATEGIES): number {
  const config = MODEL_STRATEGIES[strategy];
  return itemsPerDay * 30 * config.expectedCost;
}

// Example: 50 items/day with balanced strategy
// Cost: 50 * 30 * 0.015 = $22.50/month
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

<small>Source: `knowledge/patterns/ai-content-generation-pipeline.md`</small>
