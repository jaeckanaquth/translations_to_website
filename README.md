# Novel Translation Automation System

A comprehensive system for automating the translation and publication of novels to WordPress sites.

## Features

- Automated novel content scraping
- AI-powered translation using OpenAI's API
- WordPress integration for automated posting
- SEO tag management and optimization
- RSS feed generation
- Scheduled post management

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure environment variables in .env file:
```
WP_USER=your_wordpress_username
WP_PASSWORD=your_wordpress_password
OPENAI_API_KEY=your_openai_api_key
Website=your_wordpress_domain
```

## Usage

1. Add novel source in main.py
2. Run the translation pipeline:
```bash
python main.py
```

## Components

- page_translator.py: Handles AI translation
- posting.py: Manages WordPress integration
- add_tag.py: Handles SEO tag management
- get_the_novel.py: Scrapes source content
- novel_update.py: Manages novel updates
- custom-feed.php: Generates RSS feeds

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
