# NERD: Neutralising the Economic Rewards of Disinformation

An end-to-end data pipeline that uses **GPT-4o Vision** to extract structured datasets from multilingual news website screenshots, combined with statistical analysis and NLP to map the advertising and monetization ecosystem of disinformation websites — specifically around the 2024 EU elections.

---

## What This Project Does

Disinformation websites generate revenue through advertisements, subscriptions, and donations. This project builds tooling to answer: *what ads run alongside disinformation content, and how do these sites monetize?*

The pipeline:
1. **Ingests** thousands of screenshots of EU election-related disinformation articles (stored in Google Drive)
2. **Extracts** structured data (ads, article text, sentiment, narrative, monetization strategies) using the GPT-4o Vision API
3. **Analyses** patterns: which advertisers appear on disinformation sites, what political narratives dominate, and how these sites earn money

---

## Key Technical Achievements

| Area | What was built |
|---|---|
| **Multi-modal AI pipeline** | GPT-4o Vision extracts structured data from multilingual screenshots — no OCR, no manual labeling |
| **Structured LLM outputs** | Pydantic models + OpenAI's `beta.chat.completions.parse` for reliable, typed API responses |
| **Google Drive integration** | Automated folder traversal, image download, and temp file management via Drive API |
| **Web scraping** | Selenium + BeautifulSoup to extract monetization data from live disinformation websites |
| **NLP & visualisation** | Sentiment/tone analysis, keyword frequency, t-SNE embedding visualisation of article themes |
| **Cross-dataset analysis** | Linked ad placements to article content, revealing which ad categories co-occur with specific disinformation narratives |

---

## Results

- Processed **700+ screenshots** of disinformation news articles across **13+ languages**
- Built three structured datasets: **ads**, **articles**, and **monetization** data
- Identified **political campaign ads** running alongside anti-EU disinformation narratives
- Mapped monetization methods (direct donations, subscriptions, product sales, advertising) across 250+ disinformation websites
- Uncovered sentiment and tone patterns (fear-mongering, persuasive language) correlated with specific ad categories

---

## Project Structure

```
nerd-data-analysis/
├── notebooks/
│   ├── ads_dataset_generation/
│   │   └── generate_articles_data_from_images.ipynb   # Core pipeline: screenshots → structured CSV
│   ├── monetization_dataset_generation/
│   │   └── extract_monetization_data.ipynb            # Scrapes monetization pages, extracts payment data
│   └── analysis/
│       ├── ads_dataset_statistics.ipynb               # Ad placement, product, company distribution
│       ├── articles_data_statistics.ipynb             # Article length, sentiment, tone, keyword analysis
│       └── combined_analysis.ipynb                    # Cross-dataset: ads ↔ article narrative correlation
├── utils/
│   ├── google_drive_utils.py                          # Drive API helpers: list folders, download files
│   └── temp_folder_utils.py                           # Temp directory lifecycle management
├── config/
│   └── prompts.json                                   # GPT-4o prompts for ad and article extraction
├── .env.example                                       # Environment variable template
└── requirements.txt
```

---

## Pipeline Overview

### 1. Data Extraction (`ads_dataset_generation`)

```
Google Drive (screenshot folders)
        ↓  google_drive_utils.py
Download images to temp folder
        ↓  GPT-4o Vision API
Extract ads + article data (Pydantic-validated)
        ↓
Save to CSV datasets/
```

Each screenshot folder represents one disinformation article. The pipeline:
- Lists all folders via the Drive API
- Downloads images to a local temp folder
- Sends all images for a given article to GPT-4o with structured prompts
- Parses the response into `Advertisement` and `NewsArticleData` Pydantic models
- Saves to CSV

### 2. Monetization Extraction (`monetization_dataset_generation`)

- Loads a curated list of disinformation website monetization URLs (donation pages, subscription pages, shop pages)
- Uses Selenium to render JavaScript-heavy pages
- Sends page text + links to GPT-4o-mini with a donation/product-sales prompt
- Extracts payment platforms, donation methods, subscription plans, etc.

### 3. Analysis (`analysis`)

- **Ads analysis**: top companies, products, ad placements, political ad filter
- **Articles analysis**: headline/text length distribution, publishing agencies, keyword frequency, t-SNE keyword clustering, sentiment/tone distribution
- **Combined analysis**: merge ads and articles by image URL to correlate ad content with article narrative

---

## Setup

### Prerequisites

- Python 3.9+
- A Google Cloud service account with Drive API access (download credentials as `config/credentials.json`)
- An OpenAI API key with GPT-4o access

### Installation

```bash
git clone <repository_url>
cd nerd-data-analysis
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env and fill in your API keys
```

The `.env` file needs:
```
DRIVE_CREDENTIALS="../config/credentials.json"
SCOPES="https://www.googleapis.com/auth/drive"
OPENAI_API_KEY="sk-..."
```

### Running the Notebooks

Start with `notebooks/ads_dataset_generation/generate_articles_data_from_images.ipynb` to generate the raw datasets, then run the analysis notebooks in `notebooks/analysis/`.

For the analysis notebooks, update the data path variables at the top of each notebook to point to your dataset files.

---

## Tech Stack

- **AI/ML**: OpenAI GPT-4o Vision, Sentence Transformers, scikit-learn (t-SNE)
- **Data**: pandas, numpy
- **Visualisation**: matplotlib, seaborn, plotly
- **APIs**: Google Drive API v3, OpenAI API
- **Web scraping**: Selenium, BeautifulSoup
- **Validation**: Pydantic v2
- **Infrastructure**: Google Colab / Jupyter, python-dotenv

---

## Background

This work is part of the **NERD (Neutralising the Economic Rewards of Disinformation)** research initiative, which studies how disinformation websites generate revenue and how those revenue streams can be disrupted. The dataset focuses on EU election-related disinformation content collected in May–June 2024.
