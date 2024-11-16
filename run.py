import os
import logging
from app import create_app

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    try:
        logger.info('Starting Flask application...')
        logger.info('Server running on http://localhost:5000')
        app.run(debug=True, port=5000, host='0.0.0.0')
    except Exception as e:
        logger.error(f"Error starting Flask application: {str(e)}") 