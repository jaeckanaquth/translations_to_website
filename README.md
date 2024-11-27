# Translations Website

A web application for translating and publishing novel chapters with automated workflows for content management and SEO optimization.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Code Structure](#code-structure)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

This repository contains code for a translations website that handles:
- Novel chapter translations
- WordPress content publishing
- SEO optimization
- RSS feed generation
- Chapter navigation
- Custom styling

## Features

### Translation Management
- Automated translation workflow using OpenAI API
- Chapter content formatting and structuring
- SEO tag generation and management
- Meta title/description generation

### Content Publishing
- WordPress integration for automated posting
- Custom RSS feed generation
- Chapter navigation with next/previous links
- Category and tag management

### Frontend
- Responsive chapter listing page
- Custom styling for content presentation
- Left sidebar navigation
- Novel series grid layout

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/username/translations_to_website.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:
```
OPENAI_API_KEY=your_api_key
WP_USER=wordpress_username 
WP_PASSWORD=wordpress_password
Website=your_domain.com
```

4. Setup WordPress:
- Install required plugins
- Configure custom RSS feed template
- Add custom functions to theme

## Code Structure

### Core Components

#### Translation (`page_translator.py`)
Handles translation using OpenAI API:
```python
def page_translate(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
```

#### Publishing (`posting.py`) 
Manages WordPress content posting with:
- Chapter formatting
- Navigation links
- Meta data
- SEO tags

#### Novel Updates (`novel_update.py`)
Tracks translation progress and manages chapter data

### Frontend Files

#### Chapter Template (`get_chapter.html`)
- Responsive chapter listing
- Navigation controls
- Custom styling

#### Styling (`style.css`)
Custom styles for:
- Chapter cards
- Navigation elements  
- RSS feed formatting

## Usage

1. Add new novel:
```python
python main.py --novel "Novel Name" --url "source_url"
```

2. Generate chapters:
```python
python get_the_novel.py --novel "Novel Name"
```

3. Publish content:
```python
python posting.py --novel "Novel Name"
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -am 'Add feature'`) 
4. Push branch (`git push origin feature/name`)
5. Create Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.