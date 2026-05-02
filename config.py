import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for the trading bot"""
    
    # Alpaca API Settings
    ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
    ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
    ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL', 'https://paper-trading.alpaca.markets')
    
    # Trading Settings
    DEFAULT_SYMBOL = os.getenv('DEFAULT_SYMBOL', 'MNQ')
    DEFAULT_POSITION_SIZE = int(os.getenv('DEFAULT_POSITION_SIZE', 10))
    PAPER_TRADING = os.getenv('PAPER_TRADING', 'true').lower() == 'true'
    
    # Webhook Settings
    WEBHOOK_PORT = int(os.getenv('WEBHOOK_PORT', 5000))
    WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET', 'your_webhook_secret')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'trading_bot.log')
    
    # Risk Management
    MAX_POSITION_SIZE = int(os.getenv('MAX_POSITION_SIZE', 50))
    STOP_LOSS_PERCENT = float(os.getenv('STOP_LOSS_PERCENT', 2.0))
    TAKE_PROFIT_PERCENT = float(os.getenv('TAKE_PROFIT_PERCENT', 5.0))

config = Config()