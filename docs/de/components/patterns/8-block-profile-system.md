---
title: 8-block-profile-system
type: pattern
tags: []
lang: en
confidence: 100
---

# 8-block-profile-system


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2024-11-22 |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "blocks": [
    {
      "id": "demographic_core",
      "name": "Persönliche Daten",
      "fields": 15,
      "required": 6,
      "progressive_stage": 1
    },
    {
      "id": "family_dynamics",
      "name": "Familie & Haushalt",
      "fields": 18,
      "required": 4,
      "progressive_stage": 1
    },
    {
      "id": "financial_profile",
      "name": "Finanzielle Situation",
      "fields": 22,
      "required": 5,
      "progressive_stage": 2
    },
    {
      "id": "career_profile",
      "name": "Berufliche Situation",
      "fields": 16,
      "required": 4,
      "progressive_stage": 2
    },
    {
      "id": "motivation_matrix",
      "name": "Auswanderungs-Plan",
      "fields": 20,
      "required": 3,
      "progressive_stage": 3
    },
    {
      "id": "practical_constraints",
      "name": "Besondere Umstände",
      "fields": 12,
      "required": 0,
      "progressive_stage": 3
    },
    {
      "id": "destination_preferences",
      "name": "Präferenzen & Prioritäten",
      "fields": 15,
      "required": 3,
      "progressive_stage": 4
    },
    {
      "id": "psychological_profile",
      "name": "Zusätzliche Informationen",
      "fields": 8,
      "required": 0,
      "progressive_stage": 4
    }
  ]
}
```


#### Example



**Code:**
```typescript
interface DemographicCore {
  // Required (6)
  age: number;                           // Alter in Jahren
  gender: 'male' | 'female' | 'diverse';
  family_status: 'single' | 'couple' | 'family_with_children' | 'caring_for_elderly';
  education_level: 'basic' | 'vocational' | 'bachelor' | 'master' | 'phd';
  current_location: string;              // PLZ oder Stadt
  target_destinations: string[];         // Zielländer Array

  // Optional (9)
  nationality: string;
  second_nationality?: string;
  birth_country: string;
  current_country_years: number;         // Jahre im aktuellen Land
  previous_countries: string[];          // Frühere Wohnorte
  language_native: string;
  languages_fluent: string[];
  languages_basic: string[];
  timezone_preference: string;
}
```


#### Example



**Code:**
```typescript
interface FamilyDynamics {
  // Required (4)
  children_count: number;
  partner_included: boolean;
  family_mobility: 'aligned' | 'conflicted' | 'undecided';
  social_support_local: 'strong' | 'moderate' | 'weak';

  // Conditional (wenn children_count > 0)
  children_ages: number[];
  children_school_status: ('pre_school' | 'primary' | 'secondary' | 'university')[];
  children_special_needs: boolean;
  education_priorities: number;          // 1-10

  // Conditional (wenn partner_included)
  partner_career: {
    employment_status: string;
    remote_capable: boolean;
    career_priority: number;             // 1-10
  };
  partner_language_skills: string[];
  partner_adaptation_willingness: number; // 1-10

  // Conditional (wenn family_status includes elderly)
  elderly_care_responsibility: boolean;
  elderly_care_type: 'daily' | 'weekly' | 'financial' | 'remote';
  elderly_relocation_possible: boolean;

  // Optional
  pets: { type: string; count: number }[];
  extended_family_ties: 'strong' | 'moderate' | 'weak';
  family_abroad: string[];               // Länder mit Familie
}
```


#### Example



**Code:**
```typescript
interface FinancialProfile {
  // Required (5)
  annual_income: number;                 // Euro brutto
  liquid_assets: number;                 // Verfügbare Mittel
  risk_tolerance: 'conservative' | 'moderate' | 'aggressive';
  income_stability: 'stable' | 'variable' | 'uncertain';
  debt_obligations: number;

  // Asset Details
  property_assets: number;
  property_locations: string[];
  property_mortgages: number;
  business_assets: number;
  investment_portfolio: number;
  retirement_savings: number;
  crypto_assets: number;

  // Income Sources
  income_sources: ('salary' | 'self_employed' | 'rental' | 'dividends' | 'pension' | 'other')[];
  passive_income_percentage: number;     // % des Gesamteinkommens
  income_currency_exposure: string[];

  // Financial Goals
  target_cost_of_living: 'lower' | 'similar' | 'higher_acceptable';
  tax_optimization_priority: number;     // 1-10
  wealth_preservation_priority: number;  // 1-10

  // Obligations
  alimony_obligations: number;
  child_support_obligations: number;
  loan_commitments: number;
}
```


#### Example



**Code:**
```typescript
interface CareerProfile {
  // Required (4)
  profession: string;
  employment_status: 'employed' | 'self_employed' | 'freelancer' | 'retired' | 'student';
  remote_work_capability: boolean;
  professional_mobility: 'local' | 'national' | 'international';

  // Professional Details
  industry: string;
  experience_years: number;
  current_employer_type: 'startup' | 'sme' | 'corporate' | 'government' | 'ngo';
  management_level: 'entry' | 'mid' | 'senior' | 'executive';

  // Skills & Credentials
  professional_licenses: string[];       // Berufslizenzen
  certifications: string[];
  specialized_skills: string[];
  language_skills_professional: { language: string; level: 'basic' | 'professional' | 'native' }[];

  // Career Goals
  career_change_openness: number;        // 1-10
  entrepreneurship_interest: boolean;
  income_growth_priority: number;        // 1-10
  work_life_balance_priority: number;    // 1-10
}
```


#### Example



**Code:**
```typescript
interface MotivationMatrix {
  // Required (3)
  primary_drivers: ('tax_optimization' | 'lifestyle' | 'career' | 'safety' | 'adventure' | 'family' | 'health' | 'politics')[];
  timeline_urgency: 'immediate' | 'within_year' | 'flexible' | 'long_term';
  commitment_level: 'exploring' | 'planning' | 'decided' | 'executing';

  // Push Factors (warum weg?)
  stress_factors: ('taxes' | 'regulations' | 'climate' | 'politics' | 'economy' | 'social' | 'healthcare' | 'crime')[];
  stress_intensity: number;              // 1-10

  // Pull Factors (warum dort?)
  attraction_factors: string[];
  destination_research_depth: 'none' | 'basic' | 'moderate' | 'extensive';
  visited_destinations: string[];

  // Success Definition
  success_financial: string;             // Freitext
  success_lifestyle: string;
  success_family: string;
  success_career: string;

  // Timeline Details
  ideal_departure_date: string;          // ISO Date
  hard_deadline: string | null;
  flexibility_months: number;

  // Constraints
  must_have_criteria: string[];
  deal_breakers: string[];
  compromise_areas: string[];
}
```


#### Example



**Code:**
```typescript
interface PracticalConstraints {
  // All Optional - conditional relevance
  visa_limitations: string[];            // Bekannte Visa-Einschränkungen
  health_conditions: string[];           // Relevante Gesundheitsthemen
  medication_requirements: string[];     // Regelmäßige Medikamente

  language_barriers: string[];           // Sprachen die Probleme machen
  professional_licensing: string[];      // Berufsanerkennungs-Hürden

  property_commitments: {
    type: string;
    location: string;
    value: number;
    sellable: boolean;
  }[];

  contract_obligations: {
    type: string;
    end_date: string;
    penalty: number;
  }[];

  legal_issues: string[];                // Laufende Rechtsverfahren etc.
  custody_arrangements: string;
  military_obligations: string;

  accessibility_needs: string[];
  dietary_restrictions: string[];
}
```


#### Example



**Code:**
```typescript
interface DestinationPreferences {
  // Required (3)
  climate_preferences: 'tropical' | 'mediterranean' | 'temperate' | 'continental' | 'any';
  culture_preferences: 'similar' | 'moderately_different' | 'completely_different';
  cost_of_living_preference: 'lower' | 'similar' | 'higher_acceptable';

  // Priority Scores (1-10)
  tax_priority: number;
  healthcare_priority: number;
  education_priority: number;
  safety_priority: number;
  infrastructure_priority: number;
  expat_community_priority: number;

  // Specific Preferences
  urban_rural: 'urban' | 'suburban' | 'rural' | 'flexible';
  population_size_preference: 'small_town' | 'medium_city' | 'large_city' | 'any';
  nature_access_priority: number;        // 1-10
  entertainment_priority: number;        // 1-10

  // Exclusions
  excluded_regions: string[];
  excluded_climates: string[];
}
```


#### Example



**Code:**
```typescript
interface PsychologicalProfile {
  // All Optional - enhanced personalization
  personality_type: string;              // z.B. MBTI oder Big Five
  adaptation_style: 'quick_adapter' | 'gradual_adapter' | 'careful_planner';
  stress_tolerance: number;              // 1-10
  change_comfort: number;                // 1-10
  cultural_openness: number;             // 1-10
  decision_making_style: 'analytical' | 'intuitive' | 'consensus';
  risk_taking_tendency: number;          // 1-10
  social_needs: 'high' | 'moderate' | 'low';
}
```


#### Example



**Code:**
```typescript
const conditionalRules = {
  // Familie
  "show_children_details": {
    condition: "family_dynamics.children_count > 0",
    show: ["children_ages", "children_school_status", "education_priorities"]
  },

  // Partner
  "show_partner_details": {
    condition: "family_dynamics.partner_included === true",
    show: ["partner_career", "partner_language_skills", "partner_adaptation_willingness"]
  },

  // Elderly Care
  "show_elderly_care": {
    condition: "family_dynamics.family_status === 'caring_for_elderly'",
    show: ["elderly_care_responsibility", "elderly_care_type", "elderly_relocation_possible"]
  },

  // Business
  "show_business_details": {
    condition: "financial_profile.business_assets > 0 || career_profile.employment_status === 'self_employed'",
    show: ["business_migration_block"]
  },

  // Crypto
  "show_crypto_details": {
    condition: "financial_profile.crypto_assets > 50000",
    show: ["crypto_strategy_block"]
  },

  // Pets
  "show_pet_logistics": {
    condition: "family_dynamics.pets.length > 0",
    show: ["pet_transport_requirements"]
  }
};
```


#### Example



**Code:**
```typescript
const defaultValues = {
  // 80% Use Cases abdecken
  demographic_core: {
    languages_basic: ["English"],
    timezone_preference: "Europe/Berlin"
  },

  family_dynamics: {
    children_count: 0,
    partner_included: false,
    social_support_local: "moderate",
    pets: []
  },

  financial_profile: {
    crypto_assets: 0,
    business_assets: 0,
    passive_income_percentage: 0,
    risk_tolerance: "moderate"
  },

  career_profile: {
    remote_work_capability: false,
    professional_mobility: "national",
    career_change_openness: 5,
    entrepreneurship_interest: false
  },

  motivation_matrix: {
    timeline_urgency: "flexible",
    commitment_level: "exploring",
    destination_research_depth: "basic"
  },

  destination_preferences: {
    culture_preferences: "moderately_different",
    urban_rural: "flexible",
    excluded_regions: []
  },

  psychological_profile: {
    adaptation_style: "gradual_adapter",
    stress_tolerance: 5,
    cultural_openness: 5,
    decision_making_style: "analytical"
  }
};
```


#### Example



**Code:**
```typescript
const progressiveStages = [
  {
    stage: 1,
    name: "Grunddaten",
    blocks: ["demographic_core", "family_dynamics"],
    estimated_time: "3-5 min",
    completion_threshold: 0.7,  // 70% der required fields
    unlock_message: "Wir können jetzt erste Empfehlungen geben"
  },
  {
    stage: 2,
    name: "Finanzielle Situation",
    blocks: ["financial_profile", "career_profile"],
    estimated_time: "5-8 min",
    completion_threshold: 0.8,
    unlock_message: "Jetzt können wir Steueroptimierung berechnen"
  },
  {
    stage: 3,
    name: "Auswanderungsplan",
    blocks: ["motivation_matrix", "practical_constraints"],
    estimated_time: "5-7 min",
    completion_threshold: 0.6,
    unlock_message: "Vollständige Analyse möglich"
  },
  {
    stage: 4,
    name: "Feintuning",
    blocks: ["destination_preferences", "psychological_profile"],
    estimated_time: "3-5 min",
    completion_threshold: 0.5,
    unlock_message: "Personalisierte Empfehlungen freigeschaltet"
  }
];
```


#### Example



**Code:**
```typescript
const validationRules = {
  // Cross-Field Validation
  "income_vs_assets": {
    rule: "financial_profile.liquid_assets >= financial_profile.annual_income * 0.5",
    warning: "Empfehlung: Mindestens 6 Monate Einkommen als Liquidität",
    severity: "warning"
  },

  "children_age_consistency": {
    rule: "family_dynamics.children_ages.every(age => age >= 0 && age <= 30)",
    error: "Ungültiges Kindesalter",
    severity: "error"
  },

  "timeline_vs_complexity": {
    rule: "!(motivation_matrix.timeline_urgency === 'immediate' && career_profile.professional_licensing.length > 2)",
    warning: "Sofortige Auswanderung mit vielen Berufslizenzen ist unrealistisch",
    severity: "warning"
  },

  "partner_alignment": {
    rule: "!(family_dynamics.partner_included && family_dynamics.partner_adaptation_willingness < 3)",
    warning: "Niedriger Partner-Wille erhöht Risiko signifikant",
    severity: "warning"
  }
};
```


#### Example



**Code:**
```json
{
  "demographic_core": {
    "age": 32,
    "gender": "male",
    "family_status": "single",
    "education_level": "master",
    "current_location": "München",
    "target_destinations": ["Portugal", "Thailand", "Singapore"]
  },
  "financial_profile": {
    "annual_income": 95000,
    "liquid_assets": 120000,
    "risk_tolerance": "moderate",
    "crypto_assets": 25000
  },
  "career_profile": {
    "profession": "Software Engineer",
    "employment_status": "employed",
    "remote_work_capability": true,
    "professional_mobility": "international"
  }
}
// → Archetype: "Digital Nomad / Strategic Optimizer"
// → Success Probability: 85-90%
// → Recommended Timeline: 6-12 Monate
```


#### Example



**Code:**
```json
{
  "demographic_core": {
    "age": 42,
    "family_status": "family_with_children",
    "target_destinations": ["Schweiz", "Österreich"]
  },
  "family_dynamics": {
    "children_count": 2,
    "children_ages": [8, 12],
    "partner_included": true,
    "partner_career": {
      "employment_status": "employed",
      "remote_capable": false,
      "career_priority": 6
    },
    "family_mobility": "aligned",
    "education_priorities": 9
  },
  "financial_profile": {
    "annual_income": 180000,
    "liquid_assets": 350000,
    "property_assets": 450000
  }
}
// → Archetype: "Family Coordinator"
// → Success Probability: 75-80%
// → Recommended Timeline: 18-36 Monate
// → Critical Agents: familie_kinder, steueroptimierung
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/8-block-profile-system.md`</small>
