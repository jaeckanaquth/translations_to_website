# Novel Translation and Publishing System

A comprehensive system for translating novels from Chinese to English and publishing them on WordPress. The system automates translation, content management, SEO optimization, and publishing workflows.

## Features

- Automated novel content extraction from source websites
- AI-powered translation using OpenAI's API
- WordPress integration for automated publishing
- SEO tag generation and management
- Custom RSS feed generation
- Chapter tracking and scheduling
- Google Drive integration for backup

## Components

The system consists of several key components:

### Content Extraction
- Novel content scraping from source sites
- Chapter metadata extraction
- Content cleaning and preprocessing

### Translation
- OpenAI API integration for translation
- Content chunking and batch processing
- Translation quality checks

### Publishing
- WordPress post creation and scheduling
- SEO tag management
- Custom RSS feed generation
- Chapter linking and navigation

### Management
- Translation progress tracking
- Chapter scheduling
- Update notifications
- Google Drive backup

## Setup

1. Clone the repository:
```bash
git clone https://github.com/jaeckanaquth/translations_to_website.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```
OPENAI_API_KEY=your_api_key
WP_USER=wordpress_username
WP_PASSWORD=wordpress_password
Website=your_domain.com
```

4. Run the main application:
```bash
python main.py
```

## Architecture

The system follows a modular architecture with clear separation of concerns:

- `main.py`: Application entry point and workflow orchestration
- `get_the_novel.py`: Novel content extraction
- `page_translator.py`: Translation processing
- `posting.py`: WordPress integration
- `novel_update.py`: Update management
- `add_tag.py`: SEO tag management
- `custom-feed.php`: RSS feed generation
- `functions.php`: WordPress customizations

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers directly.
