# Translations to Website

## Core Functionality
Automated system for translating novel chapters and posting to WordPress.

## Components
- `main.py`: Entry point and orchestration
- `page_translator.py`: Text translation handling 
- `posting.py`: WordPress integration
- `custom-feed.php`: RSS feed generation
- `style.css`: Theme styling

## Setup
1. Configure environment variables:
   - WP_USER: WordPress username
   - WP_APP_PASSWORD: WordPress application password
   - NOVEL_URL: Source novel URL

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License
MIT License
