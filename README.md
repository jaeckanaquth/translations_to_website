# Novel Translation and Publishing System

A web application that automates novel translations and publishing to WordPress using OpenAI integration.

## Core Components

- `page_translator.py`: Handles translation using OpenAI's API
- `posting.py`: Manages WordPress post creation and updates
- `main.py`: Core application logic and workflow orchestration
- `get_the_novel.py`: Novel content retrieval
- `novel_update.py`: Handles novel update processing
- `add_tag.py`: Manages SEO tags

## Features

- Novel translation automation
- WordPress integration for content publishing
- Custom RSS feeds via `custom-feed.php`
- SEO tag management
- Chapter navigation system
- Scheduled posting capability

## Directory Structure

```
├── main.py                 # Main application entry point
├── page_translator.py      # Translation handling
├── posting.py             # WordPress posting logic
├── get_the_novel.py      # Novel retrieval
├── novel_update.py       # Update processing
├── add_tag.py           # Tag management
├── site_setup.md         # Site configuration
├── style.css             # Main stylesheet
├── custom-feed.php       # Custom RSS feed
└── old_code/            # Legacy code directory
```

## Environment Setup

Required environment variables:
- `OPENAI_API_KEY`: For translation services
- `WP_USER`: WordPress username
- `WP_PASSWORD`: WordPress application password
- `Website`: Website domain

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env` file
4. Configure WordPress settings per `site_setup.md`
5. Run the application: `python main.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit pull requests with detailed descriptions
4. Follow the existing code style

## License

This project is under MIT license - see LICENSE file for details.
