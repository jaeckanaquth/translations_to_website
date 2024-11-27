# Novel Translation and Publishing System

A web application for automating novel translations and WordPress publishing.

## Core Functionality
- Automated novel translation using OpenAI
- WordPress content management integration
- Custom RSS feeds and SEO optimization
- Chapter navigation system
- Scheduled posting capability

## Directory Structure
├── main.py                 # Main application entry point
├── page_translator.py      # Translation handling
├── posting.py             # WordPress posting logic
├── site_setup.md         # Site configuration
├── style.css             # Main stylesheet
├── custom-feed.php       # Custom RSS feed
└── old_code/            # Legacy code directory

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
4. Configure WordPress settings
5. Run the application: `python main.py`

## Contributing
- Fork the repository
- Create a feature branch
- Submit pull requests with detailed descriptions
- Follow the existing code style

## License
This project is under MIT license - see LICENSE file for details.
