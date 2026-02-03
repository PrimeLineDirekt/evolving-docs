---
title: gdpr-compliant-saas
type: pattern
tags: ["[gdpr", " dsgvo", " compliance", " privacy", " legal", " firebase", " consent", " data-protection]"]
lang: en
confidence: 100
---

# gdpr-compliant-saas


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
<span class="tag tag-[gdpr">[gdpr</span>
<span class="tag tag--dsgvo"> dsgvo</span>
<span class="tag tag--compliance"> compliance</span>
<span class="tag tag--privacy"> privacy</span>
<span class="tag tag--legal"> legal</span>
<span class="tag tag--firebase"> firebase</span>
<span class="tag tag--consent"> consent</span>
<span class="tag tag--data-protection]"> data-protection]</span>
</div>

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
```typescript
// firebase.config.ts
import { initializeApp, FirebaseOptions } from 'firebase/app';
import { getFirestore, initializeFirestore, CACHE_SIZE_UNLIMITED } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';
import { getStorage } from 'firebase/storage';

const firebaseConfig: FirebaseOptions = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = initializeApp(firebaseConfig);

// Firestore mit EU-Region und Offline-Persistence
export const db = initializeFirestore(app, {
  cacheSizeBytes: CACHE_SIZE_UNLIMITED,
  // Experimentelle Long-Polling für bessere Offline-Support
  experimentalForceLongPolling: true,
});

export const auth = getAuth(app);
export const storage = getStorage(app);
```


#### Example



**Code:**
```bash
# Bei Projekt-Erstellung Region wählen:
# - europe-west3 (Frankfurt) ← EMPFOHLEN für DE
# - europe-west1 (Belgien)
# - europe-west6 (Zürich)

# Firestore Location setzen (nur bei Erstellung möglich!)
firebase init firestore
# Wähle: europe-west3

# Cloud Functions Region
firebase functions:config:set region="europe-west3"
```


#### Example



**Code:**
```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Hilfsfunktion: Ist User authentifiziert?
    function isAuthenticated() {
      return request.auth != null;
    }

    // Hilfsfunktion: Ist User der Besitzer?
    function isOwner(userId) {
      return isAuthenticated() && request.auth.uid == userId;
    }

    // Hilfsfunktion: Hat User Consent gegeben?
    function hasConsent() {
      return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.gdprConsent == true;
    }

    // User-Dokumente: Nur eigene Daten
    match /users/{userId} {
      // Lesen: Nur eigene Daten
      allow read: if isOwner(userId);

      // Erstellen: Bei Registrierung
      allow create: if isOwner(userId) &&
        request.resource.data.keys().hasAll(['email', 'gdprConsent', 'gdprConsentDate', 'createdAt']);

      // Update: Nur eigene Daten + Audit-Trail
      allow update: if isOwner(userId) &&
        request.resource.data.updatedAt == request.time;

      // Löschen: Nur eigene Daten (Recht auf Löschung)
      allow delete: if isOwner(userId);

      // Sub-Collection: Consent-Historie
      match /consentHistory/{consentId} {
        allow read: if isOwner(userId);
        allow create: if isOwner(userId);
        // Consent-Historie darf NICHT gelöscht werden (Legal Requirement)
        allow delete: if false;
      }

      // Sub-Collection: Audit-Logs
      match /auditLogs/{logId} {
        allow read: if isOwner(userId);
        allow create: if isOwner(userId);
        // Audit-Logs dürfen NICHT gelöscht werden
        allow delete: if false;
      }
    }

    // Öffentliche Dokumente (Impressum, etc.)
    match /public/{docId} {
      allow read: if true;
      allow write: if false; // Nur Admin via Backend
    }
  }
}
```


#### Example



**Code:**
```typescript
// types/legal.ts
interface Impressum {
  // Pflichtangaben nach §5 TMG
  companyName: string;           // Firma oder Name
  legalForm?: string;            // GmbH, UG, etc.
  representedBy?: string;        // Geschäftsführer
  address: {
    street: string;
    zipCode: string;
    city: string;
    country: string;             // Deutschland
  };
  contact: {
    email: string;               // PFLICHT
    phone?: string;              // Optional
    fax?: string;                // Optional
  };
  registration?: {
    court: string;               // z.B. "Amtsgericht München"
    number: string;              // HRB XXXXX
  };
  vatId?: string;                // USt-IdNr.
  taxId?: string;                // Steuernummer
  supervisoryAuthority?: string; // Bei regulierten Berufen
  professionalRegulations?: string; // Bei Freiberuflern

  // Streitbeilegung (seit 2016 Pflicht)
  disputeResolution: {
    euPlatformUrl: string;       // https://ec.europa.eu/consumers/odr
    participates: boolean;       // Nimmt an Schlichtung teil?
  };
}

// Template Generator
function generateImpressum(data: Impressum): string {
  return `
# Impressum

## Angaben gemäß § 5 TMG

${data.companyName}${data.legalForm ? ` (${data.legalForm})` : ''}
${data.representedBy ? `Vertreten durch: ${data.representedBy}` : ''}

${data.address.street}
${data.address.zipCode} ${data.address.city}
${data.address.country}

## Kontakt

E-Mail: ${data.contact.email}
${data.contact.phone ? `Telefon: ${data.contact.phone}` : ''}
${data.contact.fax ? `Fax: ${data.contact.fax}` : ''}

${data.registration ? `
## Registereintrag

Registergericht: ${data.registration.court}
Registernummer: ${data.registration.number}
` : ''}

${data.vatId ? `## Umsatzsteuer-ID

Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz:
${data.vatId}
` : ''}

## Streitschlichtung

Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:
${data.disputeResolution.euPlatformUrl}

Unsere E-Mail-Adresse finden Sie oben im Impressum.

Wir sind ${data.disputeResolution.participates ? '' : 'nicht '}bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.
  `.trim();
}
```


#### Example



**Code:**
```typescript
// types/privacy-policy.ts
interface PrivacyPolicySection {
  title: string;
  content: string;
  required: boolean;
}

interface DataProcessingActivity {
  purpose: string;
  legalBasis: 'consent' | 'contract' | 'legal_obligation' | 'vital_interest' | 'public_interest' | 'legitimate_interest';
  dataCategories: string[];
  recipients?: string[];
  retentionPeriod: string;
  thirdCountryTransfer?: boolean;
}

const REQUIRED_SECTIONS: PrivacyPolicySection[] = [
  {
    title: "1. Verantwortlicher",
    content: "Name und Kontaktdaten des Verantwortlichen gemäß Art. 4 Abs. 7 DSGVO",
    required: true
  },
  {
    title: "2. Datenschutzbeauftragter",
    content: "Kontaktdaten (falls bestellt - Pflicht ab 20 Mitarbeitern)",
    required: false // Abhängig von Unternehmensgröße
  },
  {
    title: "3. Betroffenenrechte",
    content: `
Sie haben folgende Rechte:
- **Auskunftsrecht** (Art. 15 DSGVO)
- **Recht auf Berichtigung** (Art. 16 DSGVO)
- **Recht auf Löschung** (Art. 17 DSGVO)
- **Recht auf Einschränkung** (Art. 18 DSGVO)
- **Recht auf Datenübertragbarkeit** (Art. 20 DSGVO)
- **Widerspruchsrecht** (Art. 21 DSGVO)
- **Recht auf Widerruf** (Art. 7 Abs. 3 DSGVO)
- **Beschwerderecht** bei Aufsichtsbehörde (Art. 77 DSGVO)
    `,
    required: true
  },
  {
    title: "4. Datenverarbeitung im Einzelnen",
    content: "Auflistung aller Verarbeitungstätigkeiten",
    required: true
  },
  {
    title: "5. Cookies und Tracking",
    content: "Cookie-Kategorien, Opt-in/Opt-out Mechanismen",
    required: true
  },
  {
    title: "6. Drittanbieter und Auftragsverarbeiter",
    content: "Liste aller Sub-Processors mit Zweck",
    required: true
  },
  {
    title: "7. Datentransfer in Drittländer",
    content: "Wenn ja: Rechtsgrundlage (SCCs, Angemessenheitsbeschluss)",
    required: true // Falls zutreffend
  },
  {
    title: "8. Speicherdauer",
    content: "Aufbewahrungsfristen pro Datenkategorie",
    required: true
  },
  {
    title: "9. Automatisierte Entscheidungsfindung",
    content: "Falls Profiling/AI-Entscheidungen",
    required: false // Falls zutreffend
  }
];

// Typische Verarbeitungstätigkeiten für SaaS
const TYPICAL_PROCESSING_ACTIVITIES: DataProcessingActivity[] = [
  {
    purpose: "Nutzerkonto-Verwaltung",
    legalBasis: "contract",
    dataCategories: ["E-Mail", "Name", "Passwort (gehasht)"],
    retentionPeriod: "Bis Kontolöschung + 30 Tage Backup"
  },
  {
    purpose: "Zahlungsabwicklung",
    legalBasis: "contract",
    dataCategories: ["Zahlungsdaten", "Rechnungsadresse"],
    recipients: ["Stripe", "PayPal"],
    retentionPeriod: "10 Jahre (§ 147 AO)",
    thirdCountryTransfer: true
  },
  {
    purpose: "Produkt-Analytics",
    legalBasis: "consent",
    dataCategories: ["Nutzungsverhalten", "Geräteinformationen"],
    recipients: ["Google Analytics (anonymisiert)"],
    retentionPeriod: "14 Monate"
  },
  {
    purpose: "Newsletter",
    legalBasis: "consent",
    dataCategories: ["E-Mail", "Öffnungsraten"],
    recipients: ["Mailchimp"],
    retentionPeriod: "Bis Abmeldung"
  },
  {
    purpose: "Support-Anfragen",
    legalBasis: "contract",
    dataCategories: ["Kommunikationsinhalte", "Kontaktdaten"],
    retentionPeriod: "3 Jahre nach Abschluss"
  }
];
```


#### Example



**Code:**
```typescript
// types/terms.ts
interface TermsOfService {
  sections: {
    scope: string;               // Geltungsbereich
    contractConclusion: string;  // Vertragsschluss
    serviceDescription: string;  // Leistungsbeschreibung
    userObligations: string;     // Pflichten des Nutzers
    intellectualProperty: string; // Geistiges Eigentum
    liability: string;           // Haftung
    warranty: string;            // Gewährleistung
    termination: string;         // Kündigung
    dataProtection: string;      // Datenschutz (Verweis)
    amendments: string;          // Änderungen der AGB
    severability: string;        // Salvatorische Klausel
    jurisdiction: string;        // Gerichtsstand
  };
  version: string;
  effectiveDate: Date;
}

// KRITISCHE Klauseln für SaaS
const CRITICAL_CLAUSES = {
  // Haftungsbeschränkung (deutsches Recht)
  liabilityLimitation: `
## Haftung

1. Der Anbieter haftet unbeschränkt für Vorsatz und grobe Fahrlässigkeit.

2. Bei leichter Fahrlässigkeit haftet der Anbieter nur bei Verletzung
   wesentlicher Vertragspflichten (Kardinalpflichten). Die Haftung ist
   dabei auf den vorhersehbaren, vertragstypischen Schaden begrenzt.

3. Die vorstehenden Haftungsbeschränkungen gelten nicht für Schäden
   aus der Verletzung des Lebens, des Körpers oder der Gesundheit.

4. Die Haftung nach dem Produkthaftungsgesetz bleibt unberührt.

5. Die Haftung ist der Höhe nach auf [X Euro / Jahresentgelt] begrenzt.
  `,

  // Subscription-Kündigung
  subscriptionTermination: `
## Kündigung

1. Das Abonnement kann jederzeit zum Ende der Laufzeit gekündigt werden.

2. Die Kündigung muss in Textform (E-Mail genügt) erfolgen.

3. Die Kündigung muss spätestens [X Tage] vor Ablauf eingehen.

4. Nach Kündigung bleiben Ihre Daten noch 30 Tage verfügbar für Export.

5. Nach Ablauf der 30-Tage-Frist werden alle Daten unwiderruflich gelöscht.
  `,

  // Salvatorische Klausel (immer erforderlich)
  severability: `
## Schlussbestimmungen

Sollten einzelne Bestimmungen dieser AGB unwirksam sein oder werden,
bleibt die Wirksamkeit der übrigen Bestimmungen unberührt. Anstelle
der unwirksamen Bestimmung gilt eine wirksame Bestimmung als vereinbart,
die dem wirtschaftlichen Zweck der unwirksamen Bestimmung am nächsten kommt.
  `
};
```


#### Example



**Code:**
```typescript
// types/withdrawal.ts
interface WithdrawalPolicy {
  withdrawalPeriod: number;      // 14 Tage Standard
  startCondition: string;        // Wann beginnt Frist?
  exceptions: string[];          // Wann kein Widerruf?
  consequences: string;          // Was passiert nach Widerruf?
  withdrawalForm: string;        // Muster-Widerrufsformular
}

const STANDARD_WITHDRAWAL_POLICY: WithdrawalPolicy = {
  withdrawalPeriod: 14,
  startCondition: "ab dem Tag des Vertragsschlusses",
  exceptions: [
    "Digitale Inhalte, wenn die Ausführung mit ausdrücklicher Zustimmung begonnen hat",
    "Individuell angefertigte Produkte",
    "Dienstleistungen, die vollständig erbracht wurden"
  ],
  consequences: `
Bei Widerruf erstatten wir Ihnen alle erhaltenen Zahlungen unverzüglich,
spätestens binnen 14 Tagen. Für die Rückzahlung verwenden wir dasselbe
Zahlungsmittel, das Sie bei der ursprünglichen Transaktion eingesetzt haben.
  `,
  withdrawalForm: `
## Muster-Widerrufsformular

An: [Ihr Unternehmen]
    [Adresse]
    [E-Mail]

Hiermit widerrufe(n) ich/wir (*) den von mir/uns (*) abgeschlossenen
Vertrag über die Erbringung der folgenden Dienstleistung (*):

_______________________________________

Bestellt am (*) / erhalten am (*): ___________

Name des/der Verbraucher(s): ___________

Anschrift des/der Verbraucher(s): ___________

Datum: ___________

Unterschrift des/der Verbraucher(s) (nur bei Papierform): ___________

(*) Unzutreffendes streichen.
  `
};

// WICHTIG: Widerrufsverzicht bei digitalen Inhalten
const DIGITAL_CONTENT_WAIVER = `
## Verzicht auf Widerrufsrecht (Digitale Inhalte)

[ ] Ich stimme ausdrücklich zu, dass der Anbieter vor Ablauf der
    Widerrufsfrist mit der Ausführung des Vertrages beginnt.

[ ] Mir ist bekannt, dass ich durch diese Zustimmung mit Beginn der
    Ausführung mein Widerrufsrecht verliere.

Diese Checkboxen MÜSSEN aktiv angeklickt werden (kein Pre-Check!).
`;
```


#### Example



**Code:**
```typescript
// components/CookieConsent.tsx
import { useState, useEffect } from 'react';
import { doc, setDoc, getDoc, serverTimestamp, collection, addDoc } from 'firebase/firestore';
import { db, auth } from '@/lib/firebase';

interface CookieConsent {
  necessary: boolean;      // Immer true, nicht abwählbar
  functional: boolean;     // Session, Preferences
  analytics: boolean;      // Google Analytics, Mixpanel
  marketing: boolean;      // Facebook Pixel, Google Ads
}

interface ConsentRecord {
  userId?: string;
  sessionId: string;
  consent: CookieConsent;
  consentDate: Date;
  ipHash: string;          // Gehashte IP für Nachweis
  userAgent: string;
  consentVersion: string;  // Version der Consent-Texte
  action: 'accept_all' | 'accept_selected' | 'reject_optional' | 'update';
}

// Cookie-Kategorien mit rechtlicher Erklärung
const COOKIE_CATEGORIES = {
  necessary: {
    name: "Notwendig",
    description: "Diese Cookies sind für die Grundfunktionen der Website erforderlich.",
    examples: ["Session-Cookies", "Sicherheits-Cookies", "Consent-Cookie"],
    canDisable: false,
    retention: "Session bis 1 Jahr"
  },
  functional: {
    name: "Funktional",
    description: "Diese Cookies ermöglichen erweiterte Funktionen und Personalisierung.",
    examples: ["Sprach-Präferenzen", "Login-Status", "UI-Einstellungen"],
    canDisable: true,
    retention: "1-12 Monate"
  },
  analytics: {
    name: "Analyse",
    description: "Diese Cookies helfen uns, die Nutzung der Website zu verstehen.",
    examples: ["Google Analytics", "Hotjar", "Mixpanel"],
    canDisable: true,
    retention: "14 Monate"
  },
  marketing: {
    name: "Marketing",
    description: "Diese Cookies werden verwendet, um relevante Werbung anzuzeigen.",
    examples: ["Facebook Pixel", "Google Ads", "LinkedIn Insights"],
    canDisable: true,
    retention: "6-24 Monate"
  }
};

// Consent-Banner Komponente
export function CookieBanner() {
  const [showBanner, setShowBanner] = useState(false);
  const [showDetails, setShowDetails] = useState(false);
  const [consent, setConsent] = useState<CookieConsent>({
    necessary: true,
    functional: false,
    analytics: false,
    marketing: false
  });

  useEffect(() => {
    // Prüfe ob Consent bereits gegeben
    const existingConsent = localStorage.getItem('gdpr_consent');
    if (!existingConsent) {
      setShowBanner(true);
    }
  }, []);

  const saveConsent = async (action: ConsentRecord['action']) => {
    const record: ConsentRecord = {
      sessionId: getOrCreateSessionId(),
      consent,
      consentDate: new Date(),
      ipHash: await hashIP(),
      userAgent: navigator.userAgent,
      consentVersion: "2.0",
      action
    };

    // Lokal speichern
    localStorage.setItem('gdpr_consent', JSON.stringify({
      ...consent,
      date: new Date().toISOString(),
      version: "2.0"
    }));

    // In Firestore für Nachweis
    if (auth.currentUser) {
      record.userId = auth.currentUser.uid;
      await addDoc(
        collection(db, 'users', auth.currentUser.uid, 'consentHistory'),
        {
          ...record,
          createdAt: serverTimestamp()
        }
      );
    } else {
      // Anonymer Consent-Log
      await addDoc(collection(db, 'anonymousConsents'), {
        ...record,
        createdAt: serverTimestamp()
      });
    }

    // Cookies entsprechend aktivieren/deaktivieren
    applyCookieSettings(consent);
    setShowBanner(false);
  };

  const handleAcceptAll = () => {
    setConsent({
      necessary: true,
      functional: true,
      analytics: true,
      marketing: true
    });
    saveConsent('accept_all');
  };

  const handleRejectOptional = () => {
    setConsent({
      necessary: true,
      functional: false,
      analytics: false,
      marketing: false
    });
    saveConsent('reject_optional');
  };

  const handleAcceptSelected = () => {
    saveConsent('accept_selected');
  };

  if (!showBanner) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 bg-white border-t shadow-lg p-6 z-50">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-lg font-bold mb-2">Cookie-Einstellungen</h2>

        <p className="text-sm text-gray-600 mb-4">
          Wir nutzen Cookies, um Ihnen die bestmögliche Erfahrung zu bieten.
          Einige sind notwendig, andere helfen uns, die Website zu verbessern.
          <button
            onClick={() => setShowDetails(!showDetails)}
            className="text-blue-600 underline ml-1"
          >
            {showDetails ? 'Weniger anzeigen' : 'Details anzeigen'}
          </button>
        </p>

        {showDetails && (
          <div className="space-y-4 mb-6 border rounded p-4">
            {Object.entries(COOKIE_CATEGORIES).map(([key, category]) => (
              <div key={key} className="flex items-start">
                <input
                  type="checkbox"
                  id={key}
                  checked={consent[key as keyof CookieConsent]}
                  disabled={!category.canDisable}
                  onChange={(e) => setConsent({
                    ...consent,
                    [key]: e.target.checked
                  })}
                  className="mt-1 mr-3"
                />
                <label htmlFor={key} className="flex-1">
                  <span className="font-medium">{category.name}</span>
                  {!category.canDisable && (
                    <span className="text-xs ml-2 text-gray-500">(erforderlich)</span>
                  )}
                  <p className="text-sm text-gray-600">{category.description}</p>
                  <p className="text-xs text-gray-400">
                    Beispiele: {category.examples.join(', ')}
                  </p>
                </label>
              </div>
            ))}
          </div>
        )}

        <div className="flex flex-wrap gap-3">
          <button
            onClick={handleAcceptAll}
            className="bg-blue-600 text-white px-6 py-2 rounded font-medium"
          >
            Alle akzeptieren
          </button>

          {showDetails && (
            <button
              onClick={handleAcceptSelected}
              className="bg-gray-200 text-gray-800 px-6 py-2 rounded font-medium"
            >
              Auswahl bestätigen
            </button>
          )}

          <button
            onClick={handleRejectOptional}
            className="bg-gray-100 text-gray-600 px-6 py-2 rounded"
          >
            Nur notwendige
          </button>
        </div>

        <div className="mt-4 text-xs text-gray-500">
          <a href="/datenschutz" className="underline">Datenschutzerklärung</a>
          {' • '}
          <a href="/impressum" className="underline">Impressum</a>
        </div>
      </div>
    </div>
  );
}

// Hilfsfunktionen
function getOrCreateSessionId(): string {
  let sessionId = sessionStorage.getItem('session_id');
  if (!sessionId) {
    sessionId = crypto.randomUUID();
    sessionStorage.setItem('session_id', sessionId);
  }
  return sessionId;
}

async function hashIP(): Promise<string> {
  // IP wird serverseitig gehasht (Client kennt eigene IP nicht)
  // Hier nur Placeholder - echte Implementation via API
  return 'hashed_ip_placeholder';
}

function applyCookieSettings(consent: CookieConsent) {
  // Google Analytics
  if (consent.analytics) {
    // gtag aktivieren
    window.gtag?.('consent', 'update', {
      'analytics_storage': 'granted'
    });
  } else {
    window.gtag?.('consent', 'update', {
      'analytics_storage': 'denied'
    });
  }

  // Marketing
  if (consent.marketing) {
    window.gtag?.('consent', 'update', {
      'ad_storage': 'granted',
      'ad_user_data': 'granted',
      'ad_personalization': 'granted'
    });
  } else {
    window.gtag?.('consent', 'update', {
      'ad_storage': 'denied',
      'ad_user_data': 'denied',
      'ad_personalization': 'denied'
    });
  }
}
```


#### Example



**Code:**
```typescript
// Liste der Sub-Processors (DSGVO Art. 28)
interface SubProcessor {
  name: string;
  purpose: string;
  location: string;
  dataCategories: string[];
  safeguards: string;           // SCCs, Angemessenheitsbeschluss
  avvLink?: string;             // Link zum AVV
}

const SUB_PROCESSORS: SubProcessor[] = [
  {
    name: "Google Cloud / Firebase",
    purpose: "Cloud-Infrastruktur, Datenbank, Auth",
    location: "EU (Frankfurt)",
    dataCategories: ["Alle Nutzerdaten"],
    safeguards: "EU-Datenresidenz, ISO 27001, SOC 2",
    avvLink: "https://cloud.google.com/terms/data-processing-addendum"
  },
  {
    name: "Stripe",
    purpose: "Zahlungsabwicklung",
    location: "USA (mit SCCs)",
    dataCategories: ["Zahlungsdaten", "Rechnungsadresse"],
    safeguards: "Standard Contractual Clauses (SCCs), PCI DSS Level 1",
    avvLink: "https://stripe.com/de/legal/dpa"
  },
  {
    name: "Vercel",
    purpose: "Hosting, CDN",
    location: "Global (Edge), Daten in EU",
    dataCategories: ["Technische Logs", "IP-Adressen (gehasht)"],
    safeguards: "SCCs, ISO 27001",
    avvLink: "https://vercel.com/legal/dpa"
  }
];
```


#### Example



**Code:**
```typescript
// services/gdpr/data-export.ts
import { collection, getDocs, query, where } from 'firebase/firestore';
import { ref, listAll, getDownloadURL } from 'firebase/storage';
import { db, storage } from '@/lib/firebase';
import JSZip from 'jszip';

interface ExportedData {
  profile: Record<string, any>;
  consents: any[];
  activities: any[];
  files: { name: string; url: string }[];
  exportDate: string;
  format: 'json' | 'csv';
}

export async function exportUserData(userId: string): Promise<Blob> {
  const zip = new JSZip();

  // 1. Profildaten
  const userDoc = await getDoc(doc(db, 'users', userId));
  const profile = userDoc.data();

  // Sensible Felder entfernen
  delete profile?.passwordHash;
  delete profile?.internalNotes;

  zip.file('profile.json', JSON.stringify(profile, null, 2));

  // 2. Consent-Historie
  const consentsSnap = await getDocs(
    collection(db, 'users', userId, 'consentHistory')
  );
  const consents = consentsSnap.docs.map(d => ({
    id: d.id,
    ...d.data()
  }));
  zip.file('consents.json', JSON.stringify(consents, null, 2));

  // 3. Aktivitäten
  const activitiesSnap = await getDocs(
    collection(db, 'users', userId, 'activities')
  );
  const activities = activitiesSnap.docs.map(d => ({
    id: d.id,
    ...d.data()
  }));
  zip.file('activities.json', JSON.stringify(activities, null, 2));

  // 4. Uploads
  const uploadsRef = ref(storage, `users/${userId}/uploads`);
  try {
    const uploadsList = await listAll(uploadsRef);
    const uploadsFolder = zip.folder('uploads');

    for (const item of uploadsList.items) {
      const url = await getDownloadURL(item);
      const response = await fetch(url);
      const blob = await response.blob();
      uploadsFolder?.file(item.name, blob);
    }
  } catch (e) {
    // Keine Uploads vorhanden
  }

  // 5. Audit-Log des Exports
  await addDoc(collection(db, 'users', userId, 'auditLogs'), {
    action: 'DATA_EXPORT',
    timestamp: serverTimestamp(),
    ipHash: await hashIP(),
    userAgent: navigator.userAgent
  });

  // 6. README hinzufügen
  zip.file('README.txt', `
Ihre Daten - Exportiert am ${new Date().toISOString()}

Diese ZIP-Datei enthält alle über Sie gespeicherten Daten gemäß
Art. 20 DSGVO (Recht auf Datenübertragbarkeit):

- profile.json: Ihre Profildaten
- consents.json: Ihre Einwilligungshistorie
- activities.json: Ihre Aktivitäten
- uploads/: Ihre hochgeladenen Dateien

Bei Fragen wenden Sie sich an: datenschutz@example.com
  `);

  return await zip.generateAsync({ type: 'blob' });
}

// API Route
// app/api/gdpr/export/route.ts
export async function POST(request: Request) {
  const { userId } = await request.json();

  // Auth prüfen
  const session = await getServerSession();
  if (!session || session.user.id !== userId) {
    return new Response('Unauthorized', { status: 401 });
  }

  const blob = await exportUserData(userId);

  return new Response(blob, {
    headers: {
      'Content-Type': 'application/zip',
      'Content-Disposition': `attachment; filename="meine-daten-${new Date().toISOString().split('T')[0]}.zip"`
    }
  });
}
```


#### Example



**Code:**
```typescript
// services/gdpr/data-deletion.ts
import {
  doc, deleteDoc, collection, getDocs,
  writeBatch, query, where, updateDoc, serverTimestamp
} from 'firebase/firestore';
import { ref, deleteObject, listAll } from 'firebase/storage';
import { db, storage, auth } from '@/lib/firebase';

interface DeletionRequest {
  userId: string;
  requestDate: Date;
  scheduledDeletion: Date;  // +30 Tage
  status: 'pending' | 'processing' | 'completed' | 'cancelled';
  reason?: string;
}

// Aufbewahrungsfristen nach Gesetz
const RETENTION_PERIODS = {
  invoices: { years: 10, law: '§ 147 AO' },          // Steuerrecht
  contracts: { years: 6, law: '§ 257 HGB' },         // Handelsrecht
  consents: { years: 3, law: 'DSGVO Nachweis' },     // Nachweispflicht
  auditLogs: { years: 3, law: 'DSGVO Nachweis' },
  supportTickets: { years: 3, law: 'Verjährung' }
};

export async function requestAccountDeletion(
  userId: string,
  reason?: string
): Promise<DeletionRequest> {
  const now = new Date();
  const scheduledDeletion = new Date(now);
  scheduledDeletion.setDate(scheduledDeletion.getDate() + 30);

  const request: DeletionRequest = {
    userId,
    requestDate: now,
    scheduledDeletion,
    status: 'pending',
    reason
  };

  // In DB speichern
  await setDoc(doc(db, 'deletionRequests', userId), {
    ...request,
    createdAt: serverTimestamp()
  });

  // Audit-Log
  await addDoc(collection(db, 'users', userId, 'auditLogs'), {
    action: 'DELETION_REQUESTED',
    scheduledFor: scheduledDeletion,
    timestamp: serverTimestamp()
  });

  // Bestätigungs-E-Mail senden
  await sendDeletionConfirmationEmail(userId, scheduledDeletion);

  return request;
}

export async function executeAccountDeletion(userId: string): Promise<void> {
  const batch = writeBatch(db);

  // 1. Aktive Sessions invalidieren
  await auth.currentUser?.delete();

  // 2. Benutzerdaten löschen (außer gesetzlich vorgeschrieben)
  const userRef = doc(db, 'users', userId);

  // Anonymisieren statt löschen (für Aufbewahrungspflichten)
  await updateDoc(userRef, {
    email: `deleted_${Date.now()}@anonymized.local`,
    name: 'Gelöschter Benutzer',
    phone: null,
    address: null,
    // Consent-History behalten (Nachweispflicht)
    deletedAt: serverTimestamp(),
    deletionCompleted: true
  });

  // 3. Aktivitäten löschen
  const activitiesSnap = await getDocs(
    collection(db, 'users', userId, 'activities')
  );
  activitiesSnap.docs.forEach(d => {
    batch.delete(d.ref);
  });

  // 4. Uploads löschen
  try {
    const uploadsRef = ref(storage, `users/${userId}/uploads`);
    const uploadsList = await listAll(uploadsRef);
    for (const item of uploadsList.items) {
      await deleteObject(item);
    }
  } catch (e) {
    // Keine Uploads oder bereits gelöscht
  }

  // 5. Batch ausführen
  await batch.commit();

  // 6. Finales Audit-Log (wird in anonymisierten Datensatz gespeichert)
  await addDoc(collection(db, 'deletionLog'), {
    anonymizedUserId: `deleted_${userId.substring(0, 8)}`,
    deletedAt: serverTimestamp(),
    retainedUntil: new Date(Date.now() + 3 * 365 * 24 * 60 * 60 * 1000) // 3 Jahre
  });
}

// Automatische Bereinigung (Cloud Function)
export async function cleanupScheduledDeletions(): Promise<void> {
  const now = new Date();

  const pendingDeletions = await getDocs(
    query(
      collection(db, 'deletionRequests'),
      where('status', '==', 'pending'),
      where('scheduledDeletion', '<=', now)
    )
  );

  for (const doc of pendingDeletions.docs) {
    const { userId } = doc.data();

    await updateDoc(doc.ref, { status: 'processing' });

    try {
      await executeAccountDeletion(userId);
      await updateDoc(doc.ref, {
        status: 'completed',
        completedAt: serverTimestamp()
      });
    } catch (error) {
      await updateDoc(doc.ref, {
        status: 'failed',
        error: error.message
      });
    }
  }
}
```


#### Example



**Code:**
```typescript
// services/audit/audit-logger.ts
import { collection, addDoc, serverTimestamp } from 'firebase/firestore';
import { db } from '@/lib/firebase';

type AuditAction =
  | 'USER_CREATED'
  | 'USER_LOGIN'
  | 'USER_LOGOUT'
  | 'CONSENT_GIVEN'
  | 'CONSENT_UPDATED'
  | 'CONSENT_WITHDRAWN'
  | 'DATA_ACCESSED'
  | 'DATA_EXPORTED'
  | 'DATA_MODIFIED'
  | 'DELETION_REQUESTED'
  | 'DELETION_COMPLETED'
  | 'PAYMENT_PROCESSED'
  | 'SUBSCRIPTION_CHANGED'
  | 'ADMIN_ACTION';

interface AuditEntry {
  action: AuditAction;
  userId: string;
  targetId?: string;           // Bei Aktionen auf andere Ressourcen
  details?: Record<string, any>;
  ipHash: string;
  userAgent: string;
  timestamp: Date;
  sessionId: string;
}

export async function logAuditEvent(
  action: AuditAction,
  userId: string,
  details?: Record<string, any>
): Promise<void> {
  const entry: Omit<AuditEntry, 'timestamp'> = {
    action,
    userId,
    details: sanitizeDetails(details),
    ipHash: await getHashedIP(),
    userAgent: typeof window !== 'undefined' ? navigator.userAgent : 'server',
    sessionId: getSessionId()
  };

  // Speichere in user-spezifischer Collection
  await addDoc(collection(db, 'users', userId, 'auditLogs'), {
    ...entry,
    timestamp: serverTimestamp()
  });

  // Kritische Aktionen zusätzlich global loggen
  const criticalActions: AuditAction[] = [
    'DELETION_REQUESTED',
    'DELETION_COMPLETED',
    'ADMIN_ACTION',
    'CONSENT_WITHDRAWN'
  ];

  if (criticalActions.includes(action)) {
    await addDoc(collection(db, 'globalAuditLog'), {
      ...entry,
      timestamp: serverTimestamp()
    });
  }
}

// Sensible Daten aus Details entfernen
function sanitizeDetails(details?: Record<string, any>): Record<string, any> | undefined {
  if (!details) return undefined;

  const sanitized = { ...details };

  // Sensible Felder entfernen
  const sensitiveFields = ['password', 'token', 'secret', 'creditCard', 'ssn'];
  for (const field of sensitiveFields) {
    if (field in sanitized) {
      sanitized[field] = '[REDACTED]';
    }
  }

  return sanitized;
}

// Wrapper für häufige Aktionen
export const AuditLogger = {
  login: (userId: string, method: 'email' | 'google' | 'apple') =>
    logAuditEvent('USER_LOGIN', userId, { method }),

  logout: (userId: string) =>
    logAuditEvent('USER_LOGOUT', userId),

  consentGiven: (userId: string, categories: string[]) =>
    logAuditEvent('CONSENT_GIVEN', userId, { categories }),

  dataExported: (userId: string) =>
    logAuditEvent('DATA_EXPORTED', userId),

  dataAccessed: (userId: string, dataType: string) =>
    logAuditEvent('DATA_ACCESSED', userId, { dataType })
};
```


#### Example



**Code:**
```typescript
// Vollständiger GDPR-konformer Onboarding Flow
async function onboardNewUser(email: string, password: string): Promise<void> {
  // 1. User erstellen
  const userCredential = await createUserWithEmailAndPassword(auth, email, password);
  const userId = userCredential.user.uid;

  // 2. Consent prüfen (aus Cookie-Banner)
  const consent = JSON.parse(localStorage.getItem('gdpr_consent') || '{}');

  if (!consent.necessary) {
    throw new Error('Consent required');
  }

  // 3. User-Dokument mit GDPR-Feldern erstellen
  await setDoc(doc(db, 'users', userId), {
    email,
    gdprConsent: true,
    gdprConsentDate: serverTimestamp(),
    gdprConsentVersion: "2.0",
    marketingConsent: consent.marketing || false,
    analyticsConsent: consent.analytics || false,
    createdAt: serverTimestamp(),
    updatedAt: serverTimestamp()
  });

  // 4. Consent-Historie starten
  await addDoc(collection(db, 'users', userId, 'consentHistory'), {
    type: 'INITIAL_CONSENT',
    consent,
    timestamp: serverTimestamp(),
    ipHash: await hashIP(),
    userAgent: navigator.userAgent
  });

  // 5. Audit-Log
  await AuditLogger.login(userId, 'email');

  // 6. Willkommens-E-Mail mit Datenschutz-Hinweisen
  await sendWelcomeEmail(email, {
    dataExportUrl: '/settings/privacy',
    deletionUrl: '/settings/delete-account',
    privacyPolicyUrl: '/datenschutz'
  });
}
```


#### Example



**Code:**
```typescript
// User ändert Marketing-Consent im Account
async function updateMarketingConsent(
  userId: string,
  newValue: boolean
): Promise<void> {
  const userRef = doc(db, 'users', userId);

  // 1. User-Dokument aktualisieren
  await updateDoc(userRef, {
    marketingConsent: newValue,
    marketingConsentDate: serverTimestamp(),
    updatedAt: serverTimestamp()
  });

  // 2. Consent-Historie ergänzen
  await addDoc(collection(db, 'users', userId, 'consentHistory'), {
    type: 'CONSENT_UPDATE',
    field: 'marketingConsent',
    oldValue: !newValue,
    newValue,
    timestamp: serverTimestamp(),
    source: 'account_settings'
  });

  // 3. Cookies entsprechend anpassen
  if (newValue) {
    window.gtag?.('consent', 'update', { 'ad_storage': 'granted' });
  } else {
    window.gtag?.('consent', 'update', { 'ad_storage': 'denied' });
    // Tracking-Cookies löschen
    document.cookie.split(';').forEach(c => {
      if (c.includes('_ga') || c.includes('_fbp')) {
        document.cookie = c.split('=')[0] + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
      }
    });
  }

  // 4. Audit-Log
  await logAuditEvent('CONSENT_UPDATED', userId, {
    field: 'marketingConsent',
    newValue
  });
}
```


#### Example



**Code:**
```markdown
## GDPR Compliance Checklist

### Infrastruktur
- [ ] Firebase in EU-Region (europe-west3)
- [ ] Firestore in EU-Region
- [ ] Backups in EU

### Rechtliche Dokumente
- [ ] Impressum (§5 TMG)
- [ ] Datenschutzerklärung (Art. 13 DSGVO)
- [ ] AGB
- [ ] Widerrufsbelehrung
- [ ] Cookie-Richtlinie
- [ ] AVV mit allen Sub-Processors

### Technisch
- [ ] Cookie-Banner mit Opt-in
- [ ] Consent-Logging
- [ ] Datenexport-Funktion
- [ ] Kontolöschung-Funktion
- [ ] Audit-Logging
- [ ] Verschlüsselung at rest

### Prozesse
- [ ] Datenpannen-Prozess (72h Meldung)
- [ ] Löschanfragen-Prozess
- [ ] Auskunftsanfragen-Prozess
- [ ] Regelmäßige Compliance-Reviews
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

<small>Source: `knowledge/patterns/gdpr-compliant-saas.md`</small>
