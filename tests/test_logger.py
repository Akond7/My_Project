from night_security_shift.settings import LOGS_DIR
from night_security_shift.utils.logger import setup_logger


def test_setup_logger_creates_log_file():
    logger = setup_logger("test_logger")

    logger.info("Test log message")

    for handler in logger.handlers:
        handler.flush()

    log_file = LOGS_DIR / "game.log"

    assert log_file.exists()
    assert "Test log message" in log_file.read_text(encoding="utf-8")