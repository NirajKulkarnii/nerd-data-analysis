# Neutralising the Economic Rewards of Disinformation (NERD): Dataset Construction and Analysis

This repository contains the code and resources for the **Neutralising the Economic Rewards of Disinformation (NERD)** project. The project focuses on building datasets to analyze the economic impact of disinformation websites, focusing on their advertisements, articles, and monetization strategies. By exploring how these websites generate revenue and the associated disinformation narratives, this project aims to provide valuable insights into combating the spread of false information.

## Table of Contents
1. [Notebooks Folder](#notebooks-folder)
   1. [ads_dataset_generation](#ads_dataset_generation)
   2. [monetization_dataset_generation](#monetization_dataset_generation)
   3. [analysis](#analysis)
2. [utils Folder](#utils-folder)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Documentation](#documentation)



## Notebooks Folder

### 1. **ads_dataset_generation/**
This folder contains the Jupyter notebook for generating datasets related to ads and articles using screenshot data.

- **ads_dataset_generation.ipynb**: This notebook extracts ad-related data from screenshots and processes it into a structured format for analysis.

### 2. **monetization_dataset_generation/**
This folder contains notebooks related to monetization dataset generation, focusing on website data extraction.

- **monetization_dataset_generation.ipynb**: Extracts websites from the raw data and removes links that point to social media platforms like Facebook and X (formerly Twitter). This ensures only relevant websites are included in the monetization analysis.
- **generate_monetization_data.ipynb**: Generates monetization-related datasets from the filtered website data, focusing on how disinformation websites generate revenue.

### 3. **analysis/**
This folder contains Python notebooks for analyzing the datasets related to advertisements, articles, and combined data.

- **ads_analysis.ipynb**: Analyzes the ad-related dataset, focusing on ad placement, product distribution, company representation, and trends.
- **articles_analysis.ipynb**: Analyzes the article dataset, exploring publication sources, author information, and trends in article content.
- **combined_analysis.ipynb**: Combines the analysis of both ads and articles to identify correlations and patterns between advertisement content and article narratives.

## utils Folder

The `utils` folder contains various utility scripts that support the data extraction and processing pipeline.

- **google_drive_utils.py**: Provides functions for extracting folders and files from Google Drive, allowing for easy access to raw data.
- **temp_folder_utils.py**: Manages the creation and deletion of temporary folders during the data processing workflow.

## Configuration

The `config` folder contains configuration files such as `prompt.json`, which holds the prompts for extracting advertisement and article data to be passed to the GPT-4 API for further processing.

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>

2. Install the required dependencies:

    `pip install -r requirements.txt`

3. You can start by running the Jupyter notebooks in the notebooks/ folder, depending on which dataset you want to generate or analyze.


## Documentation
Detailed documentation explaining how the advertisement, article, and monetization-related datasets were generated, along with the methodology used, can be found in the docs/ folder