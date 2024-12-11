# Bitcoin Telegram Bot

This project is a **Bitcoin Telegram Bot** that monitors the current price of Bitcoin and sends updates to a specified Telegram chat when the price falls below a defined limit. The bot fetches Bitcoin's price using the CoinMarketCap API and sends alerts via the Telegram Bot API.

## Features

- Fetches the current price of Bitcoin in USD using the CoinMarketCap API.
- Sends price alerts to a specified Telegram chat when Bitcoin's price falls below a predefined limit.
- Runs continuously, checking the price at regular intervals.

---

## Prerequisites

### Requirements
- **Python 3.x**
- A valid **CoinMarketCap API key**
- A valid **Telegram Bot token** and **chat ID**
- Required Python libraries (installed via `pipenv`):
  - `requests`

### Accounts Needed
- Create a Telegram bot and obtain the bot token using the [Telegram BotFather](https://core.telegram.org/bots#botfather).
- Obtain a free or paid API key from [CoinMarketCap](https://pro.coinmarketcap.com/account).

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd telegram_bitcoin_bot
```

### Step 2: Set Up Environment Variables

Create a `.env` file in the project root (or use the provided `.env.example` as a template):

```bash
API_KEY=your_coinmarketcap_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
LIMIT=30000  # Replace with your desired Bitcoin price limit
TIME_INTERVAL=60  # Time interval (in seconds) between price checks
```

### Step 3: Build and Run the Docker Container

#### Using Docker Compose
1. Build the Docker image and run the container:
   ```bash
   docker-compose up --build
   ```

2. Verify the bot is running and monitoring the Bitcoin price.

#### Without Docker Compose
Alternatively, you can run the bot without Docker Compose by building and running the image manually:

```bash
docker build -t bitcoin_bot .
docker run --env-file .env bitcoin_bot
```

### Step 4: Run Locally (Optional)

If you prefer running the bot without Docker:

1. Install `pipenv` if not already installed:
   ```bash
   pip install pipenv
   ```

2. Install dependencies:
   ```bash
   pipenv install --deploy --ignore-pipfile
   ```

3. Run the bot:
   ```bash
   pipenv run python main.py
   ```

---

## Project Structure

```
telegram_bitcoin_bot/
├── constants.py     # Defines project-wide constants
├── .env.example              # Example environment variables file
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker build instructions
├── Pipfile                  # Dependency manager file (pipenv)
├── Pipfile.lock             # Locked dependency versions
├── README.md                # Project documentation
└── main.py                  # Main execution script
```

---

## Usage

1. The bot will continuously monitor Bitcoin's price at regular intervals (defined by `TIME_INTERVAL`).
2. If Bitcoin's price falls below the limit specified in the `LIMIT` environment variable, the bot will send a Telegram notification to the specified chat.
3. To stop the bot, terminate the Docker container or process manually.

---

## Example Output

When running the bot, you'll see logs similar to the following:

```bash
Loading .env environment variables...
Starting the bot...
Current Bitcoin price: 28,500.0
Bitcoin price now is 28,500.0
Sent message to Telegram: Bitcoin price now is 28,500.0
```

---

## Notes

- **Error Handling**: The script gracefully handles API errors (e.g., request failures, unexpected data) by logging error messages and continuing execution.
- **Custom Modifications**: Adjust the `LIMIT` and `TIME_INTERVAL` values in your `.env` file to customize behavior.
- **Scaling**: For large-scale usage, consider setting up API rate limits and monitoring tools.

---

## Troubleshooting

### Common Issues

1. **No Updates in Telegram**
   - Check if the `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are correct.
   - Confirm that the bot has access to the specified chat (e.g., add the bot to the chat).

2. **API Errors**
   - Ensure your `API_KEY` is valid and has sufficient quota.
   - Double-check the CoinMarketCap API plan to confirm that your subscription supports the required endpoints.

3. **Docker Build Errors**
   - Verify the `.env` file is properly configured and available during the build.

---

## Contributing

Contributions are welcome! If you'd like to report an issue or contribute to the project, feel free to open a pull request or submit an issue on the repository.

---

## Acknowledgments

- [CoinMarketCap API](https://pro.coinmarketcap.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

